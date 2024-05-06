from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_redirecter),
    # slug - for more beautiful url 
    path('<slug:section>', section, name='section'),
    path('<slug:section>/<slug:thread>.<int:thread_id>', thread, name='thread'),
    path('<slug:section>.<int:section_id>/thread', create_thread, name='create_thread'),
    path('<slug:section>/<slug:thread>.<int:thread_id>#<int:msg_id>', msg_redirect, name='msg_redirect'),
    path('<int:msg_id>/report', report_msg, name="report_msg"),
    path('<int:thread_id>/close', toggle_close_thread, name="toggle_close_thread"),
    path('<int:thread_id>/delete', toggle_thread_visibility, name="toggle_thread_visibility")
]
