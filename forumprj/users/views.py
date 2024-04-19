from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
import os
from . forms import *
from . models import *

def profile_view(request, id):
    # All info from DB about user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    dictionary = {
        "media_url": settings.MEDIA_URL,
        "profile": profile,
        "account_id": id
    }
    # print(settings.MEDIA_URL + profile.profile_picture)
    return render(request, "profile.html", dictionary)

def profile_edit(request, id):
    if request.method == "POST":
        # built-in form in django to update user information 
        form = UpdateUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                eUser = User.objects.get(id=id)
                file_extension = os.path.splitext(image_file.name)[1]
                new_filename = slugify(f'{eUser.username}_avatar') + file_extension
                image_file.name = new_filename
                file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
                e_user = Profile.objects.get(user=eUser)
                e_user.profile_picture = image_file.name
                e_user.save()
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