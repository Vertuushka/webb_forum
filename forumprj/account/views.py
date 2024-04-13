from django.shortcuts import redirect, render, HttpResponse
from . forms import *
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return HttpResponse("current user is already authenticated")
    context = {}
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login_user')
    else:
        form = AuthenticationForm()
    context['form'] = form
    return render(request, "account_forms.html", context)