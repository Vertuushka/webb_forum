from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_redirecter),
    # slug - for more beautiful url 
    path('<slug:section>/', section, name='section'),
    path('<slug:section>/<slug:thread>.<int:thread_id>/', thread, name='thread'),
    path('<slug:section>.<int:section_id>/start_thread/', create_thread, name='create_thread'),
    path('<slug:section>/<slug:thread>.<int:thread_id>#<int:msg_id>/', msg_redirect, name='msg_redirect'),
    path('message/<int:msg_id>/report/', report_msg, name="report_msg"),
    path('thread/<int:thread_id>/close/', toggle_close_thread, name="toggle_close_thread"),
    path('thread/<int:thread_id>/delete/', toggle_thread_visibility, name="toggle_thread_visibility"),
    path('thread/<int:thread_id>/pin/', toggle_thread_pin, name="toggle_thread_pin"),
    path('message/<int:msg_id>/delete/', toggle_msg_visibility, name="toggle_msg_visibility")
]
