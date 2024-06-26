from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from base import base_strings
from . models import *
from django.db.models import Q, Max
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
@login_required
def send_private_message(request, id):
    # add to dialog on new dialog start
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('profile_view', id)
        try:
            receiver = User.objects.get(id=id)
        except:
            return redirect('profile_view', id)
        content = request.POST.get('content')
        try:
            dialog = Dialog.objects.get(user_1=receiver, user_2=request.user)
        except:
            try:
                dialog = Dialog.objects.get(user_1=request.user, user_2=receiver)
            except:
                dialog = Dialog.objects.create(user_1=request.user, user_2=receiver)
                dialog.save()
        try:
            new_msg = Private_Message.objects.create(
                sender=request.user,
                receiver=receiver,
                content=content, 
                dialog=dialog
            )
            new_msg.save()
        except:
            return redirect('profile_view', id)
    return redirect('profile_view', id)

@login_required
def messages_main(request):
    user = request.user
    context = {}
    dialogs = Dialog.objects.filter(
        Q(user_1=user) |
        Q(user_2=user)
    ).annotate(latest_msg=Max('private_message__id')).order_by('-latest_msg')
    context["dialogs"] = dialogs
    return render(request, 'messages.html', context)

@login_required
def messages_dialog(request, id):
    user = request.user
    if id != user.id:
        try:
            account = User.objects.get(id=id)
        except:
            return render (request, 'error.html', {'error_str':base_strings.ERRORS['user_not_found']})
        dialogs = Dialog.objects.filter(
            Q(user_1=user) |
            Q(user_2=user)
        ).annotate(latest_msg=Max('private_message__id')).order_by('-latest_msg')
        try:
            dialog = Dialog.objects.get(
                Q(user_1=user, user_2=account) |
                Q(user_2=user, user_1=account)
            )
        except:
                context = {
                'messages': False,
                'dialogs': dialogs,
                'account': account,
                'current_dialog':True
            }
                return render(request, 'messages.html', context)
        messages = Private_Message.objects.filter(
            Q(sender=user, receiver=account) |
            Q(receiver=user, sender=account)
        ).order_by('-id')
        unread_msg = Private_Message.objects.filter(receiver=user, dialog=dialog, is_read=False)
        for msg in unread_msg:
            msg.is_read = True
            msg.save()
        context = {
            'messages':messages,
            'account': account,
            'dialogs': dialogs,
            'current_dialog': dialog
        }
        return render(request, 'messages.html', context)
    else:
        return render(request, 'error.html')