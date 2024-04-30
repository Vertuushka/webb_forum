from django.db import models
from django.contrib.auth.models import User
from forum.models import Message, Thread
from datetime import datetime
from moderation.models import Report

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.CharField(max_length=225, null=True, blank=True)
    warnings = models.SmallIntegerField(default=0)
    active_notifications = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Warnings_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Message, on_delete=models.CASCADE)
    warned_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='moderator', null=True)
    details = models.TextField()
    time_warned = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.warned_by.username} warning to {self.user.username}'
    
class Preference(models.Model):
    PROFILE_VISIBILITY = (
        (0, 'Everyone can see profile'),
        (1, 'Only forum members can see profile'),
        (2, 'Nobody can see profile (beside administrators/moderators)'),
    )

    PRIVATE_MESSAGES = (
        (0, 'Everyone can send dms'),
        (1, 'Administrators/moderators only'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color_theme = models.SmallIntegerField(default=0)
    account_visibility = models.SmallIntegerField(choices=PROFILE_VISIBILITY, default=0)
    private_messages = models.SmallIntegerField(choices=PRIVATE_MESSAGES, default=1)
    

    def __str__(self):
        return self.user.username
    
class Notification(models.Model):
    NOTIFICATIONS_TYPE = (
        (0, 'warning'),
        # (1, 'private_message'), unused
        (2, 'report'),
        (3, 'message_delete'),
        (4, 'message_edit'),
        (5, 'profile_edit'),
        (6, 'thread_delete')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.SmallIntegerField(choices=NOTIFICATIONS_TYPE)
    notification = models.TextField()
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, blank=True)
    thread = models.ForeignKey(Thread, on_delete=models.SET_NULL, null=True, blank=True)
    warning = models.ForeignKey(Warnings_history, on_delete=models.SET_NULL, null=True, blank=True)
    report = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_report")
    time_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.user.username} - {self.get_notification_type_display()}'