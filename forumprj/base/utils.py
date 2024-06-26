from users.models import Notification

def notify_user(user, notification_type, reason, notification):
    NOTIFICATIONS_TYPE = {
        'warning':          0,
        # 'private_message':  1,
        'report':           2,
        'message_delete':   3,
        'message_edit':     4,
        'profile_edit':     5,
        'thread_delete':    6,
        'thread_change':    7,
    }
    notif = Notification.objects.create(user=user, notification_type=NOTIFICATIONS_TYPE.get(notification_type), notification=notification)
    if notification_type == 'warning':
        notif.warning = reason
    if notification_type == 'message_delete' or notification_type == 'message_edit':
        notif.message = reason
    elif notification_type == 'thread_delete' or notification_type == 'thread_change':
        notif.thread = reason
    elif notification_type == 'report':
        notif.report = reason
    notif.save()
    user.profile.active_notifications += 1
    user.profile.save()

error_strings = {
    
}