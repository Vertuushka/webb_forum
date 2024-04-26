# from django.shortcuts import render
# from django.urls import reverse

# class PermissionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.moderator_urls = [
#             '/protected/url1/',
#             '/protected/url2/',
#         ]

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if request.path in self.protected_urls:
#             if not request.user.has_perm('app.permission_required'):
#                 # Если нет, перенаправляем на страницу ошибки
#                 return HttpResponseRedirect(reverse('error_page'))
#         return None
