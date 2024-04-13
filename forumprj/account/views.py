from django.shortcuts import redirect, render, HttpResponse
from . forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponse("current user is already authenticated")
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login_user')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, "account_forms.html", context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')