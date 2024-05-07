from django.urls import path

from .views import *

urlpatterns = [
    path('', messages_main, name="messages_main"),
    path('<int:id>', messages_dialog, name="messages_dialog"),
    path('send/<int:id>', send_private_message, name="send_private_message")
]