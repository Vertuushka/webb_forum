from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>.<int:id>', views.profile_view, name='profile_view'),

]
