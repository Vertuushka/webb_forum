from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.CharField(max_length=225, null=True, blank=True, default=None)
#     info = models.CharField(max_length=200, null=True, blank=True, default=None)

#     def __str__(self):
#         return self.user.first_name

# class Warning(models.Model):
