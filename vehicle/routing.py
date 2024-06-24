from django.urls import path
from .consumers import GetDeviceData , GetUberDevice_Data

websocket_urlpatterns = [
    
    path('ws/device-data/', GetDeviceData.as_asgi()),
    path('ws/get-uber-divce-data/', GetUberDevice_Data.as_asgi()),
]