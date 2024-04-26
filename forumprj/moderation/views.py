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

def report_details(request, id):
    try:
        report = Report.objects.get(id=id)
    except:
        return render(request, 'error.html')
    context = {"report":report}
    return render(request, 'report_details.html', context)
