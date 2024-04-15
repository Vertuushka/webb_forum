from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from . forms import UpdateUserInfo

# Create your views here.

def profile_view(request, username, id):
    # All info from DB about user
    user = User.objects.get(username = username)
    #TODO profile picture
    #TODO role (ex. designer)
    #TODO stuff member name
    #TODO forum/first name
    # userFirstName = user.first_name
    #TODO forum title
    # userLastName = user.last_name
    #TODO email
    # userEmail = user.email
    #TODO data joined
    # userDate = user.date_joined

    dictionary = {
        "user": user
    }
    # print(user)
    return render(request, "profile.html", dictionary)

def profile_edit(request, username, id):
    if request.method == "POST":
        # built-in form in django to update user information 
        form = UpdateUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_view", username, id)
    else:
        form = UpdateUserInfo(instance=request.user)

    dictionary = {
        "form": form
    }
    
    return render(request, "profile_edit.html", dictionary)