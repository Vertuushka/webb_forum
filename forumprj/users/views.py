from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
import os
from . forms import *
from . models import *
from forum.models import *

def profile_view(request, id):
    try:
        account = User.objects.get(id=id)
    except:
        return render(request, 'error.html')
    dictionary = {
        "account": account
    }
    return render(request, "profile.html", dictionary)

def profile_edit(request, id):
    eUser = User.objects.get(id=id)
    if request.method == "POST":
        form = UpdateUserInfo(request.POST, instance=eUser)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                print(eUser)
                file_extension = os.path.splitext(image_file.name)[1]
                new_filename = f'{eUser.id}{file_extension}' 
                image_file.name = new_filename
                file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
                eUser.profile.profile_picture = new_filename
                eUser.profile.save()
                with open(file_path, 'wb+') as destination:
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

def profile_toggle_ban(request, id):
    account = User.objects.get(id=id)
    account.profile.is_banned = False if account.profile.is_banned else True
    account.profile.save()
    return redirect('profile_view', account.id)


