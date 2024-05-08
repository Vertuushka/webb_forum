from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', moderation_main, name="moderation_main"),
    path('<int:id>/', report_details, name="report_details")
]
