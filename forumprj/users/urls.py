from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.profile_view, name='profile_view'),
    path('<int:id>/edit', views.profile_edit, name="profile_edit"),
]