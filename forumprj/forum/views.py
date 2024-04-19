from django.shortcuts import render, redirect

def forum_main(request):
    return render(request, "forum_main.html")

