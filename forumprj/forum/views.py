from django.shortcuts import render
from django.contrib.auth.models import User

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