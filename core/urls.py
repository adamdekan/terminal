from django.urls import path

from . import consumers, views

namespace = "main"

urlpatterns = [
    path("", views.index, name="index"),
]

websocket_urlpatterns = [
    path("ws/ping/", consumers.PingConsumer.as_asgi()),
]
