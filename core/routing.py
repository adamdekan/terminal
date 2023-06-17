from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/host$", consumers.HostnameConsumer.as_asgi()),
    re_path(r"ws/ping$", consumers.PingConsumer.as_asgi()),
]
