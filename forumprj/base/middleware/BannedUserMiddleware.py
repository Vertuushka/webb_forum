from django.shortcuts import redirect, render
from django.urls import reverse

class BannedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and request.user.profile.is_banned:
            return render(request, 'error.html')
        return response