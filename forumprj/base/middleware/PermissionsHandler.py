from django.shortcuts import render
import re

class PermissionsHandler:
    def __init__(self, get_response):
        self.get_response = get_response
        self.required_permissions = {
            '/moderation/': 'moderation.view_report',
            r'/profile/\d+/warnings': 'moderation.view_warnings_history',
            r'/profile/\d+/edit': 'users.change_profile'
        }

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        for url, permission in self.required_permissions.items():
            if request.path.startswith(url) or re.match(url, request.path_info):
                if re.match(url, request.path_info):
                    if 'id' in view_kwargs:
                        profile_id = view_kwargs['id']
                        if request.user.id == profile_id:
                            return None
                if not (request.user.is_staff or request.user.has_perm(permission)):
                    return render(request, 'error.html')
        return None
