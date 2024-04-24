from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.forum_main, name='forum_main'),
    path('<str:section>', views.section, name='section'),
    path('<str:section>/<str:thread>', views.thread, name='thread')
]
