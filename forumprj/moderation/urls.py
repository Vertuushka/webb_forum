from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', moderation_main, name='moderation_main'),
    path('<int:id>', moderation_report_details, name='moderation_report_detail')
]
