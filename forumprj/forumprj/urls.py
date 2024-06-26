from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
from forum import views
from base import views as baseviews
from base import api
from users.views import notifications, profile_settings

handler404 = 'base.views.custom_404_page'

urlpatterns = [
    path('', views.forum_main, name='forum_main'),
    path('', include('account.urls')),
    path('profile/', include('users.urls')),
    path('base/', include('base.urls')),
    path('forum/', include('forum.urls')),
    path('moderation/', include('moderation.urls')),
    path('error/', baseviews.error_page, name='error_page'),
    path('admin/', admin.site.urls, name="admin_url"),
    path('message/', include('profile_messages.urls')),
    path('notifications/', notifications, name='notifications'),
    path('settings/<int:id>/', profile_settings, name='profile_settings'),
    path('bookmarks/', include('bookmarks.urls')),
    path('api.msg_warning/<int:msg_id>/', api.get_warning_by_message)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


