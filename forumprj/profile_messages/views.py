from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import *

# Create your views here.

def send_private_message(request, id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('profile_view', id)
        try:
            receiver = User.objects.get(id=id)
        except:
            return redirect('profile_view', id)
        content = request.POST.get('content')
        new_msg = Private_Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )
        new_msg.save()
    return redirect('profile_view', id)