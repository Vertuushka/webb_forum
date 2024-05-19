from django.urls import path
from .consumers import DialogConsumer

websocket_urlpatterns = [
    path('ws/dialog/<int:id>/', DialogConsumer.as_asgi(), name="ws_dialog"),
]