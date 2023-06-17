import os

import pytest
from channels.testing import WebsocketCommunicator

from .consumers import PingConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "terminal.settings")


@pytest.mark.asyncio
async def test_ping_consumer():
    communicator = WebsocketCommunicator(PingConsumer.as_asgi(), "/ws/ping/")
    connected, _ = await communicator.connect()

    assert connected

    # Receive the first message
    response = await communicator.receive_output(timeout=2)
    assert response.get("text_data") == "Ping"

    # Close the connection
    await communicator.disconnect()
