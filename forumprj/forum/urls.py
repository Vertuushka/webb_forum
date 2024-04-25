from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_redirecter),
    path('<slug:section>', section, name='section'),
    path('<slug:section>/<slug:thread>.<int:thread_id>', thread, name='thread')
]
