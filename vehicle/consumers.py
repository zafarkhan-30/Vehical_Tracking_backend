# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import httpx
from .utils import get_device_Data , refresh_access_token
import asyncio
from asgiref.sync import sync_to_async
from .views import get_uber_devices_details_view , get_MBMT_device_details_view




class GetDeviceData(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "WebSocket connected"}))
        await self.fetch_data()
        

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



class GetUberDevice_Data(AsyncWebsocketConsumer):

        async def connect(self):
            await self.accept()
            await self.send(text_data=json.dumps({"message": "WebSocket connected"}))
            self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())

        async def disconnect(self, close_code):
            self.fetch_data_task.cancel()

        async def fetch_data(self):
            user = self.scope.user
            print(user)
            async with httpx.AsyncClient() as client:
                try:
                    response = await sync_to_async(get_uber_devices_details_view)()

                    # data = response.data
                    await self.send(text_data=json.dumps(response))
                except httpx.HTTPStatusError as e:
                    await self.send(text_data=json.dumps({"error": str(e)}))
                except Exception as e:
                    await self.send(text_data=json.dumps({"error": "An error occurred",
                                                        'error_message': str(e)}))

        async def fetch_data_periodically(self):
            while True:
                await self.fetch_data()
                await asyncio.sleep(60)  # Wait for 1 minute before fetching data again





class GetMBMTDevice_Data(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "WebSocket connected"}))
        self.query_params = None
        self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())

    async def disconnect(self, close_code):
        self.fetch_data_task.cancel()

    async def receive(self, text_data):
        data = json.loads(text_data)
        self.query_params = data.get('query_params', {})
        await self.send(text_data=json.dumps({"message": "Query parameters updated"}))

    async def fetch_data(self):
        async with httpx.AsyncClient() as client:
            try:
                if self.query_params:
                    response_data = await sync_to_async(get_MBMT_device_details_view)(self.query_params)
                else:
                    response_data = await sync_to_async(get_MBMT_device_details_view)()

                await self.send(text_data=json.dumps(response_data))
            except httpx.HTTPStatusError as e:
                await self.send(text_data=json.dumps({"error": str(e)}))
            except Exception as e:
                await self.send(text_data=json.dumps({"error": "An error occurred", 'error_message': str(e)}))

    async def fetch_data_periodically(self):
        while True:
            await self.fetch_data()
            await asyncio.sleep(60)  # Wait for 1 minute before fetching data again