import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.db import database_sync_to_async
import json
# from django.contrib.auth import get_user_model
import time
from django.utils import timezone
from datetime import datetime

# User = get_user_model()

MSG_TYPE_MESSAGE = 0  # For standard messages


# Example taken from:
# https://github.com/andrewgodwin/channels-examples/blob/master/multichat/chat/consumers.py
class WsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        await self.accept()
        print("Connection successful")
        # let everyone connect. But limit read/write to authenticated users

        # while True:
        #     await self.send(text_data=str(timezone.now()))
        #     print(str(timezone.now()))
        #     time.sleep(1)

    async def disconnect(self, code):
        pass
        """
        Called when the WebSocket closes for any reason.
        """
        # leave the room

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['message'] == 'Start':
            for x in range(1, int(data['value']) + 1):
                await self.send(str(x))
                await asyncio.sleep(1)  # for async, you need to use asyncio.sleep() not time.sleep()


    """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
    # Messages will have a "command" key we can switch on


'''
class WsConsumer(WebsocketConsumer):

    def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        self.accept()
        print("Connection successful")
        # let everyone connect. But limit read/write to authenticated users

        for x in range(1, 7):
            self.send(str(x))
            time.sleep(1)
        # while True:
        #     await self.send(text_data=str(timezone.now()))
        #     print(str(timezone.now()))
        #     time.sleep(1)

    def disconnect(self, code):
        pass
        """
        Called when the WebSocket closes for any reason.
        """
        # leave the room

    def receive(self, text_data):
        print(text_data)

        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        # Messages will have a "command" key we can switch on

'''
