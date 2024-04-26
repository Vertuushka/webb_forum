from django.shortcuts import render
from .models import *

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