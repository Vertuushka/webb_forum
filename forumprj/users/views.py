from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
import os
from . forms import *
from . models import *
from forum.models import *

def profile_view(request, id):
    account = User.objects.get(id=id)
    dictionary = {
        "account": account
    }
    return render(request, "profile.html", dictionary)

def profile_edit(request, id):
    account = User.objects.get(id=id)
    # print(account.id)
    # print(account)
    if request.user.id != id and not request.user.has_perm('users.can_change_profile'):
        return render(request, 'error.html')
    
    if request.method == "POST":
        form = UpdateUserInfo(request.POST, instance=account)
        if form.is_valid():
            print("valid")
            image_file = request.FILES.get('image')
            print(image_file)
            if image_file:
                # eUser = User.objects.get(id=id)
                file_extension = os.path.splitext(image_file.name)[1]
                new_filename = f'{account.id}{file_extension}' 
                image_file.name = new_filename
                file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
                account.profile.profile_picture = new_filename
                account.profile.save()
                with open(file_path, 'wb+') as destination:
                    for chunk in image_file.chunks():
                        destination.write(chunk)
            form.save()
            return redirect("profile_view", account.id)
    else:
        form = UpdateUserInfo(instance=account)

    dictionary = {
        "account":account,
        "form": form
    }
    
    return render(request, "profile_edit.html", dictionary)

def profile_content(request, id):
    account = User.objects.get(id=id)
    content = Message.objects.filter(user=account).order_by('-time_created')
    context = {
        'account':account,
        'profile_content': True,
        'content': content
    }
    return render(request, 'profile.html', context)

def profile_warnings(request, id):
    account = User.objects.get(id=id)
    warnings = Warnings_history.objects.filter(user=account).order_by('-time_warned')
    context = {
        'account': account,
        'warnings_history': True,
        'warnings': warnings  
    }
    return render(request, 'profile.html', context)

def profile_ban(request, id):
    account = User.objects.get(id=id)
    if request.user.has_perm('users.can_change_profile'):
        account.profile.is_banned = True
        account.profile.save()
    return redirect('profile_view', account.id)

def profile_unban(request, id):
    account = User.objects.get(id=id)
    if request.user.has_perm('users.can_change_profile'):
        account.profile.is_banned = False
        account.profile.save()
    return redirect('profile_view', account.id)


