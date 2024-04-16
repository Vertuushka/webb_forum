from django.shortcuts import redirect, render, HttpResponse
from . forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_user(request):
    # if request.user.is_authenticated:
    #     return HttpResponse("current user is already authenticated")
    
    if request.method == "POST":
        #? request and request.POST???
        form = LoginUserForm(request, request.POST)
        # is_valid to check AF if 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return to page where user came from (after login)
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            # When user logged in, redirect to APP:forum to profile_view
            return redirect('profile_view', user.id)
    else:
        form = LoginUserForm()
    context = {'form':form, 'is_login_page':True}
    return render(request, "account_forms.html", context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

def create_user(request):
    if request.method == 'POST':
        # SignupUserForm -> forms.py
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = SignupUserForm()
    context = {'form':form}
    return render(request, "account_forms.html", context)