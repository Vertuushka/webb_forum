from django.db import models
from django.contrib.auth.models import User
from forum.models import Message
# Create your models here.
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum_msg = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s note"