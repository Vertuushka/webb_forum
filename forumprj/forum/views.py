from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from . forms import *
from . models import *

# Create your views here.

def profile_view(request, id):
    # All info from DB about user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    dictionary = {
        "media_url": settings.MEDIA_URL,
        "profile": profile,
        "account_id": id
    }
    print(settings.MEDIA_URL + profile.profile_picture)
    return render(request, "profile.html", dictionary)

def profile_edit(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        # built-in form in django to update user information 
        form = UpdateUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_view", id)
    else:
        form = UpdateUserInfo(instance=request.user)

    dictionary = {
        "form": form,
        "profile": profile,
        "media_url": settings.MEDIA_URL
    }
    
    return render(request, "profile_edit.html", dictionary)