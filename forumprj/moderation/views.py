from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, Permission
from django.db.models import Q
from datetime import datetime
from base.views import notify_user
# Create your views here.
def moderation_main(request):
    try:
        active_reports = Report.objects.filter(is_closed=False).order_by('-time_changed')
    except:
        active_reports = False
    try:
        closed_reports = Report.objects.filter(is_closed=True).order_by('-time_changed')
    except:
        closed_reports = False
    context = {
        "active_reports":active_reports,
        "closed_reports":closed_reports
    }
    return render(request, 'moderation_main.html', context)

def report_details(request, id):
    try:
        report = Report.objects.get(id=id)
        desired_permissions = Permission.objects.filter(codename='change_report')
        users_with_permissions = User.objects.filter(
            Q(user_permissions__in=desired_permissions) | 
            Q(groups__permissions__in=desired_permissions) | 
            Q(is_staff=True)
        ).distinct()
    except:
        return render(request, 'error.html')
    if request.method == "POST":
        if request.method == "POST":
            status = request.POST.get('status')
            assigned_to = request.POST.get('assigned_to')
            is_notified = request.POST.get('is_notified', False)
            if status != 'open':
                if is_notified:
                    # add code to send notification
                    notification = request.POST.get('notification')
                    report.notification = notification
                    report.is_notified = True
                    notify_user(user=report.user, notification_type='report', reason=report, notification=notification)
                else:
                    report.is_notified = False
                
                closed_by = request.user
                report.is_closed = True
                report.is_rejected = (status == "reject")
                report.is_resolved = not report.is_rejected
                report.closed_by = closed_by
                report.time_changed = datetime.now()
                report.save()
            else:
                if assigned_to:
                    try:
                        report.assigned_to = User.objects.get(username=assigned_to)
                    except:
                        report.assigned_to = None
                else:
                    report.assigned_to = None
                report.save()
        return redirect('report_details', id)
    context = {
        "report":report,
        "moderators": users_with_permissions
        }
    return render(request, 'report_details.html', context)
