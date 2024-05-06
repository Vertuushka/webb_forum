from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
from forum import views
from base import views as baseviews

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
    path('message/', include('profile_messages.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


