# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import httpx
from .utils import get_device_Data , refresh_access_token
import asyncio

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'location_group',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'location_group',
            self.channel_name
        )

    async def receive(self, text_data):
        pass  # No need to handle incoming messages from clients

    async def send_location_data(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))





class GetDeviceData(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "WebSocket connected"}))
        await self.fetch_data()
        # await self.accept()
        # await self.send(text_data=json.dumps({"message": "WebSocket connected"}))
        # self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())
        

    async def disconnect(self, close_code):
        await self.close()

    async def fetch_data(self):
        async with httpx.AsyncClient() as client:
            refresh_token = refresh_access_token()
            response = get_device_Data(refresh_token)
            # response = await client.get('https://timscan.transvolt.in/vehical/Get-AllMBMTDevice-Details/')
            data = response.json()
            print(data)
            await self.send(text_data=json.dumps(data))



class GetDevice_Data(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "WebSocket connected"}))
        self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())

    async def disconnect(self, close_code):
        self.fetch_data_task.cancel()

    async def fetch_data(self):
        async with httpx.AsyncClient() as client:
            try:
                refresh_token = refresh_access_token()
                response = get_device_Data(refresh_token)
                # response = await client.get('https://timscan.transvolt.in/vehical/Get-AllMBMTDevice-Details/')
                data = response.json()
                await self.send(text_data=json.dumps(data))
            except httpx.HTTPStatusError as e:
                await self.send(text_data=json.dumps({"error": str(e)}))
            except Exception as e:
                await self.send(text_data=json.dumps({"error": "An error occurred"}))

    async def fetch_data_periodically(self):
        while True:
            await self.fetch_data()
            await asyncio.sleep(60)  # Wait for 1 minute before fetching data again