from django.shortcuts import redirect, render, HttpResponse
from . forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_user(request):
    # if request.user.is_authenticated:
    #     return HttpResponse("current user is already authenticated")
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('login_user')
    else:
        form = AuthenticationForm()
    context = {'form':form, 'is_login_page':True}
    return render(request, "account_forms.html", context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

def create_user(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = SignupUserForm()
    context = {'form':form}
    return render(request, "account_forms.html", context)