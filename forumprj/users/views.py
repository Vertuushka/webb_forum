from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User

import os
from . forms import *
from . models import *
from profile_messages.models import Private_Message
from forum.models import *

def profile_view(request, id):
    try:
        account = User.objects.get(id=id)
        dictionary = {
        "account": account
        }
    except:
        return render(request, 'error.html')
    if request.user == account or request.user.has_perm('users.view_profile') or account.preference.account_visibility == 0 or (account.preference.account_visibility == 1 and request.user.is_authenticated):
        
        return render(request, "profile.html", dictionary)
    else:
        return render(request, 'error.html')
    

def profile_edit(request, id):
    try:
        eUser = User.objects.get(id=id)
    except:
        return render(request, 'error.html')
    if request.method == "POST":
        form = UpdateUserInfo(request.POST, instance=eUser)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                # print(eUser)
                file_extension = os.path.splitext(image_file.name)[1]
                new_filename = f'{eUser.id}{file_extension}' 
                image_file.name = new_filename
                file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
                eUser.profile.profile_picture = new_filename
                eUser.profile.save()
                with open(file_path, 'wb+') as destination:
                    #  chunk() instead of using read() ensures that large files don’t overwhelm your system’s memory.
                    for chunk in image_file.chunks():
                        destination.write(chunk)
            form.save()
            return redirect("profile_view", eUser.id)
    else:
        form = UpdateUserInfo(instance=eUser)

    dictionary = {
        "form": form,
        "account": eUser
    }
    
    return render(request, "profile_edit.html", dictionary)

def profile_content(request, id):
    try:
        account = User.objects.get(id=id)
    except:
        return render(request, 'error.html')
    content = Message.objects.filter(user=account).order_by('-time_created')
    context = {
        'account':account,
        'profile_content': True,
        'content': content
    }
    return render(request, 'profile.html', context)

def profile_warnings(request, id):
    try:
        account = User.objects.get(id=id)
    except:
        return render(request, 'error.html')
    warnings = Warnings_history.objects.filter(user=account).order_by('-time_warned')
    context = {
        'account': account,
        'warnings_history': True,
        'warnings': warnings  
    }
    return render(request, 'profile.html', context)

def profile_toggle_ban(request, id):
    try:
        account = User.objects.get(id=id)
    except:
        return render(request, 'error.html')
    account.profile.is_banned = False if account.profile.is_banned else True
    account.profile.banned_by = request.user
    account.profile.save()
    return redirect('profile_view', account.id)

def profile_settings(request, id):
    try:
        account = User.objects.get(id=id)
    except:
        return render(request, 'error.html')
    if request.user != account:
        return render(request, 'error.html')
    if request.method == "POST":
        form = UserPreferences(request.POST, instance=account.preference)
        if form.is_valid():
            form.save()
            return redirect('profile_view', account.id)
    form = UserPreferences(instance=account.preference)
    context = {
        "account": account,
        "form": form
    }
    return render(request, 'profile_settings.html', context)

def notifications(request):
    try:
        notifs = Notification.objects.filter(user=request.user).order_by('-time_created')
    except:
        return render(request, 'error.html')
    context = {
        "notifications":notifs
    }
    request.user.profile.active_notifications = 0
    request.user.profile.save()
    return render(request, 'notifications.html', context)

