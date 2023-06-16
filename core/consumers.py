import asyncio

from channels.generic.websocket import WebsocketConsumer


class PingConsumer(WebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await asyncio.sleep(1)
            await self.send(text_data="Ping")
