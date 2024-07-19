# myapp/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
import httpx
import asyncio
from asgiref.sync import sync_to_async
from .views import get_devices_details_view 



class GetDevice_Data(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query_params = None
        self.user = None

    async def connect(self):
        await self.accept()
        self.user = self.scope['user'] 
        await self.send(text_data=json.dumps({"message": "Connected"}))

    async def disconnect(self, close_code):
        if hasattr(self, 'fetch_data_task'):
            self.fetch_data_task.cancel()

    async def receive(self, text_data):
        data = json.loads(text_data)
        self.query_params = data.get('query_params', {})
        
        if not hasattr(self, 'fetch_data_task'):
            self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())

    async def fetch_data(self):
        async with httpx.AsyncClient() as client:
            try:
                if self.query_params:
                    user_group = self.user.groups.first()
                    response = await sync_to_async(get_devices_details_view)(self.query_params ,user_group)
                else:
                    response = await sync_to_async(get_devices_details_view)()

                await self.send(text_data=json.dumps(response))
            except httpx.HTTPStatusError as e:
                await self.send(text_data=json.dumps({"error_message": str(e)}))
            except Exception as e:
                await self.send(text_data=json.dumps({"status": "error",
                                                      'error_message': str(e)}))

    async def fetch_data_periodically(self):
        while True:
            await self.fetch_data()
            await asyncio.sleep(20) 




