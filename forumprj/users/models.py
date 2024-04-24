from django.db import models
from django.contrib.auth.models import User
from forum.models import Message
from django.conf import settings

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.CharField(max_length=225, null=True, blank=True, default=None)
#     info = models.CharField(max_length=200, null=True, blank=True, default=None)

#     def __str__(self):
#         return self.user.first_name

# class Warning(models.Model):

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.CharField(max_length=225, null=True, blank=True    )
    warnings = models.SmallIntegerField(default=0)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class cWarning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Message, on_delete=models.CASCADE, limit_choices_to={'user':models.OuterRef('user')})
    warned_by = models.ForeignKey(User, on_delete=models.SET_NULL, editable=False, related_name='moderator', null=True)
    details = models.TextField()

    def __str__(self):
        return f'{self.warned_by.username} warning to {self.user.username}'