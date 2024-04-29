from django.conf import settings
from moderation.models import Report

def menuProcessor(request):
    shared_data = {
        "media_url": settings.MEDIA_URL
    }
    if request.user.is_authenticated:
        avatar_path = settings.MEDIA_URL + str(request.user.profile.profile_picture) 
        shared_data["avatar_path"] = avatar_path
    if request.user.has_perm("moderation.view_report"):
        active_reports_amount = Report.objects.filter(is_closed=False)
        assigned_reports = active_reports_amount.filter(assigned_to=request.user) 
        shared_data['reports_amount'] = len(active_reports_amount)
        shared_data['assigned_reports'] = len(assigned_reports)
    return shared_data