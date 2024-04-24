from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
import os
from . forms import *
from . models import *

def profile_view(request, id):
    account = User.objects.get(id=id)
    dictionary = {
        "account": account
    }
    return render(request, "profile.html", dictionary)

def profile_edit(request, id):
    if request.user.id != id:
        return render(request, 'error.html')
    if request.method == "POST":
        form = UpdateUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                eUser = User.objects.get(id=id)
                file_extension = os.path.splitext(image_file.name)[1]
                new_filename = f'{eUser.id}{file_extension}' 
                image_file.name = new_filename
                file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
                eUser.profile.avatar_path = new_filename
                eUser.profile.save()
                with open(file_path, 'wb+') as destination:
                    for chunk in image_file.chunks():
                        destination.write(chunk)
            form.save()
            return redirect("profile_view", id)
    else:
        form = UpdateUserInfo(instance=request.user)

    dictionary = {
        "form": form
    }
    
    return render(request, "profile_edit.html", dictionary)
