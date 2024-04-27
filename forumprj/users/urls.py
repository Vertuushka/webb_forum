from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.profile_view, name='profile_view'),
    path('<int:id>/edit', views.profile_edit, name="profile_edit"),
    path('<int:id>/content', views.profile_content, name="profile_content"),
    path('<int:id>/warnings', views.profile_warnings, name="profile_warnings"),
    path('<int:id>/ban', views.profile_toggle_ban, name="profile_toggle_ban"),
]
