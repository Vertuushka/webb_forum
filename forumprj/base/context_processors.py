from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User

def menuProcessor(request):
    if request.user.is_authenticated:
        avatar_path = settings.MEDIA_URL + str(request.user.profile.profile_picture) 
        return {'avatar_path': avatar_path, "media_url": settings.MEDIA_URL,}
    return {'avatar_path': None, "media_url": settings.MEDIA_URL,}