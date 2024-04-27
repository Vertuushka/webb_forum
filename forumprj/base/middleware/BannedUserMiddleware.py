from django.shortcuts import render
from django.urls import reverse

class BannedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = request.path_info
        if request.user.is_authenticated and request.user.profile.is_banned and not path == ('/error/'):
            return render(request, 'error.html')
        return response