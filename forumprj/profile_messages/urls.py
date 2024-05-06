from django.urls import path

from .views import *

urlpatterns = [
    path('send/<int:id>', send_private_message, name="send_private_message")
]