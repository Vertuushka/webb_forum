from django.shortcuts import render
from users.models import Notification

# Create your views here.
def index(request):

    print(request.META.get('HTTP_USER_AGENT'))
    
    return render(request, 'base.html')

def error_page(request):
    return render(request, 'error.html')

def custom_404_page(request, exception):
    return render(request, 'error.html')

def notify_user(user, notification_type, reason, notification):
    NOTIFICATIONS_TYPE = {
        'warning':          0,
        # 'private_message':  1,
        'report':           2,
        'message_delete':   3,
        'message_edit':     4,
        'profile_edit':     5,
        'thread_delete':    6,
    }
    notif = Notification.objects.create(user=user, notification_type=NOTIFICATIONS_TYPE.get(notification_type), notification=notification)
    if notification_type == 'message_delete' or notification_type == 'message_edit':
        notif.message = reason
    elif notification_type == 'thread_delete':
        notif.thread = reason
    elif notification_type == 'report':
        notif.report = reason
    notif.save()
    user.profile.active_notifications += 1
    user.profile.save()