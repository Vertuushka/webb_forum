from django.db import models
from django.contrib.auth.models import User
from forum.models import Message
from datetime import datetime

# Create your models here.
class Report(models.Model):
    content = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)
    is_declined = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, related_name="assigned_to", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    closed_by = models.ForeignKey(User, related_name="closed_by", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    is_notified = models.BooleanField(default=False)
    notification = models.CharField(max_length=250)
    time_changed = models.DateTimeField()
    time_created = models.DateTimeField(default=datetime.now())

    def __init__(self):
        return f'{self.content.user.username} - {self.content.thread.title}'