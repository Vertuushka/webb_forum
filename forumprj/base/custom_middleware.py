from django.shortcuts import render
from django.urls import resolve

class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            try:
                resolve(request.path_info)
            except:
                return render(request, 'error.html')
        return response