from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Dialog(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dialog_user_1")
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dialog_user_2")

    def __str__(self):
        return f'{self.user_1} - {self.user_2}'

class Private_Message(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_receiver")
    content = models.TextField()
    is_visible = models.BooleanField(default=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="PM_deleted_by")
    invis_reason = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    time_created = models.DateTimeField(default=datetime.now())
    time_changed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.content} - {self.sender}'