from django.conf import settings
from users.models import Profile

def menuProcessor(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        if profile.profile_picture:
            avatar_path = settings.MEDIA_URL + profile.profile_picture
        else:
            avatar_path = None
        return {'avatar_path': avatar_path, 'currentUser':user}
    return {'avatar_path': None, "currentUser":None}