import asyncio
import random
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor

from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.cache import cache


def execute_ping(hostname):
    try:
        # Run the ping command with the specified hostname or IP address
        result = subprocess.run(
            ["ping", "-c", "4", hostname], capture_output=True, text=True
        )

        if result.returncode == 0:
            # Ping was successful
            output = result.stdout
            return output
        else:
            # Ping failed
            error = result.stderr
            return error

    except subprocess.CalledProcessError as e:
        # An error occurred while running the ping command
        return str(e)


def random_string(length):
    return "".join(random.choices(string.ascii_uppercase, k=length))


class HostnameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await asyncio.sleep(0.1)
            await self.send(text_data=random_string(10))


class PingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        with ThreadPoolExecutor(max_workers=1) as executor:
            data = await asyncio.get_running_loop().run_in_executor(
                executor, execute_ping, cache.get("hostname")
            )
        await self.send(text_data=data)
