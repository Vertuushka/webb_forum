from django.db import models
from django.contrib.auth.models import User
from forum.models import Message
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.CharField(max_length=225, null=True, blank=True    )
    warnings = models.SmallIntegerField(default=0)
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