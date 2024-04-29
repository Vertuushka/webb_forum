from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Profile)
admin.site.register(Warnings_history)
admin.site.register(Preferences)
admin.site.register(Notifications)