from django.db import models
from django.contrib.auth.models import User
from forum.models import Message
# Create your models here.



class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    is_closed = models.BooleanField(default=False)
    is_declined = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None, related_name="assigned")

    def __str__(self):
        return f'{self.content.user} - {self.content.thread.title}'