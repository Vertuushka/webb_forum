from django.shortcuts import redirect, render
from . forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from users.models import Profile, Preference

def login_user(request):
    # if user authenticated - send him to his profile page
    if request.user.is_authenticated:
        return redirect('profile_view', request.user.id)
    
    if request.method == "POST":
        # LoginUserForm -> forms.py 
        form = LoginUserForm(request, request.POST)
        # is_valid for checking for correct data
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # When user logged in, redirect to APP:forum to profile_view
            return redirect('profile_view', user.id)
    else:
        # get - render LogIn page
        form = LoginUserForm()
    context = {'form':form, 'is_login_page':True}
    return render(request, "account_forms.html", context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

def create_user(request):
    # if user authenticated - send him to his profile page
    if request.user.is_authenticated:
        return redirect('profile_view', request.user.id)
    if request.method == 'POST':
        # SignupUserForm -> forms.py
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            newuser = User.objects.get(username=username)
            newProfile = Profile.objects.create(user=newuser)
            newProfile.save()
            newPreferences = Preference.objects.create(user=newuser)
            newPreferences.save()
            return redirect('login_user')
    else:
        # get - render SignUp page
        form = SignupUserForm()
    context = {'form':form}
    return render(request, "account_forms.html", context)