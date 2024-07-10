# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import httpx
from .utils import get_device_Data , refresh_access_token
import asyncio
from asgiref.sync import sync_to_async
from .views import get_devices_details_view 




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



class GetDevice_Data(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query_params = None

    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "WebSocket connected"}))

    async def disconnect(self, close_code):
        if hasattr(self, 'fetch_data_task'):
            self.fetch_data_task.cancel()

    async def receive(self, text_data):
        data = json.loads(text_data)
        self.query_params = data.get('query_params', {})
        # await self.send(text_data=json.dumps({"message": "Query parameters updated"}))

        # Start fetching data periodically after receiving the first query_params
        if not hasattr(self, 'fetch_data_task'):
            self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())

    async def fetch_data(self):
        async with httpx.AsyncClient() as client:
            try:
                if self.query_params:
                    response = await sync_to_async(get_devices_details_view)(self.query_params)
                else:
                    response = await sync_to_async(get_devices_details_view)()

                await self.send(text_data=json.dumps(response))
            except httpx.HTTPStatusError as e:
                await self.send(text_data=json.dumps({"error": str(e)}))
            except Exception as e:
                await self.send(text_data=json.dumps({"error": "An error occurred",
                                                      'error_message': str(e)}))

    async def fetch_data_periodically(self):
        while True:
            await self.fetch_data()
            await asyncio.sleep(2)  # Wait for 10 seconds before fetching data again




# class GetMBMTDevice_Data(AsyncWebsocketConsumer):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.query_params = None


#     async def connect(self):
#         await self.accept()
#         await self.send(text_data=json.dumps({"message": "WebSocket connected"}))
#         # self.query_params = None
#         # self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())

#     async def disconnect(self, close_code):
#         if hasattr(self, 'fetch_data_task'):
#             self.fetch_data_task.cancel()
        

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         self.query_params = data.get('query_params', {})
#         await self.send(text_data=json.dumps({"message": "Query parameters updated"}))

#         if not hasattr(self, 'fetch_data_task'):
#             self.fetch_data_task = asyncio.create_task(self.fetch_data_periodically())

#     async def fetch_data(self):
#         async with httpx.AsyncClient() as client:
#             try:
#                 if self.query_params:
#                     response_data = await sync_to_async(get_MBMT_device_details_view)(self.query_params)
#                 else:
#                     response_data = await sync_to_async(get_MBMT_device_details_view)()

#                 await self.send(text_data=json.dumps(response_data))
#             except httpx.HTTPStatusError as e:
#                 await self.send(text_data=json.dumps({"error": str(e)}))
#             except Exception as e:
#                 await self.send(text_data=json.dumps({"error": "An error occurred", 'error_message': str(e)}))

#     async def fetch_data_periodically(self):
#         while True:
#             await self.fetch_data()
#             await asyncio.sleep(10)  # Wait for 10 sec before fetching data again