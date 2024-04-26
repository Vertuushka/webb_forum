from django.shortcuts import render
from .models import *

# Create your views here.
def moderation_main(request):
    if request.user.has_perm('users.can_view_reports'):
        active_reports = Report.objects.filter(is_closed=False).order_by('-time_created')
        closed_reports = Report.objects.filter(is_closed=True).order_by('-time_created')[:50]
        context = {
            'active_reports':active_reports,
            'closed_reports':closed_reports
        }
        return render(request, 'moderation_main.html', context)
    else:
        return render(request, 'error.html')
    
def moderation_report_details(request, id):
    if request.user.has_perm('user.can_view_reports'):
        report = Report.objects.get(id=id)
        context = {
            "report":report
        }
        return render(request, 'report_details.html', context)
    else:
        return render(request, 'error.html')