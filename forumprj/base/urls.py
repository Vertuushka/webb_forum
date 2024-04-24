from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('error/', error_page, name='error'),
]
