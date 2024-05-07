from django.conf import settings
from moderation.models import Report
from profile_messages.models import Private_Message

def menuProcessor(request):
    shared_data = {
        "media_url": settings.MEDIA_URL
    }
    if request.user.is_authenticated:
        avatar_path = settings.MEDIA_URL + str(request.user.profile.profile_picture) 
        shared_data["avatar_path"] = avatar_path
        try:
            unread_messages = Private_Message.objects.filter(receiver=request.user, is_read=False)
            shared_data["msgs_amount"] = len(unread_messages)
        except:
             shared_data["msgs_amount"] = 0
    if request.user.has_perm("moderation.view_report"):
        active_reports_amount = Report.objects.filter(is_closed=False)
        assigned_reports = active_reports_amount.filter(assigned_to=request.user) 
        shared_data['reports_amount'] = len(active_reports_amount)
        shared_data['assigned_reports'] = len(assigned_reports)
    if request.path.startswith('/profile/'):
        shared_data["current_tab"] = 'profile'
    if request.path.startswith('/forum/'):
        shared_data["current_tab"] = 'forum'
    if request.path.startswith('/moderation/'):
        shared_data["current_tab"] = 'moderation'
    if request.path.startswith('/message/'):
        shared_data["current_tab"] = 'message'
    if 'notifications' in str(request.path):
        shared_data["current_tab"] = 'notifications'
    return shared_data