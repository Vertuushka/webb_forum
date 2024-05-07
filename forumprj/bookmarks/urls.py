from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', bookmarks_main, name='bookmarks_main'),
    path('<int:id>', add_msg_bookmark, name='add_msg_bookmark'),
    path('del/<int:id>', del_bookmark, name='del_bookmark'),
]
