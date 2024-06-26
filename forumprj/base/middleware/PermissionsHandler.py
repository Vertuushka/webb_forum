from django.shortcuts import render
import re

class PermissionsHandler:
    def __init__(self, get_response):
        self.get_response = get_response
        # dictionary
        self.required_permissions = {
            # r for using \d+
            # \d+ is for int in urls
            '/moderation/': 'moderation.view_report',
            r'/moderation/\d+': 'moderation.view_report',
            r'/profile/\d+/warnings': 'moderation.view_warnings_history',
            r'/profile/\d+/edit': 'users.change_profile',
            r'/profile/\d+/ban': 'users.change_warning_history',
            r'/forum/thread/\d+/close': 'forum.change_thread',
            r'/forum/thread/\d+/delete': 'forum.change_thread',
            r'/forum/thread/\d+/pin': 'forum.change_thread',
            r'/forum/message/\d+/delete/': 'forum.change_message',
            r'/forum/message/\d+/warn/': 'users.change_warning_history'
        }

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # processing all views in all APP's
    def process_view(self, request, view_func, view_args, view_kwargs):
        if (not request.user.is_authenticated) and re.match(r'/\d+/report', request.path_info):
            return render(request, 'error.html')
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
