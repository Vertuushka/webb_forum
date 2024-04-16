from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import *

# Create your views here.

def profile_view(request, id):
    # All info from DB about user
    user = User.objects.get(id=id)
    dictionary = {
        "user": user,
        "account_id": id
    }
    return render(request, "profile.html", dictionary)

def profile_edit(request, id):
    if request.method == "POST":
        # built-in form in django to update user information 
        form = UpdateUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_view", id)
    else:
        form = UpdateUserInfo(instance=request.user)

    dictionary = {
        "form": form
    }
    
    return render(request, "profile_edit.html", dictionary)