from django.shortcuts import render
from django.urls import reverse

class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.moderator_urls = [
            '/moderation/',
        ]

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if any(request.path.startswith(url) for url in self.moderator_urls):
            if not (request.user.is_staff or request.user.groups.filter(name='Moderators').exists()):
                return render(request, 'error.html')
        return None
