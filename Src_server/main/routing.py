from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path('ws/review/<str:theme_slag>/', consumers.ReviewConsumer.as_asgi()),
]