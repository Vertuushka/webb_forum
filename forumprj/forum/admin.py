from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Node)
admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(Attachment)