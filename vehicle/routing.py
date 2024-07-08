from django.urls import path
from .consumers import GetDeviceData , GetDevice_Data , GetMBMTDevice_Data

websocket_urlpatterns = [
    
    path('ws/device-data/', GetDeviceData.as_asgi()),
    path('ws/get-divce-data/', GetDevice_Data.as_asgi()),
    # path('ws/get-MBMT-divce-data/', GetMBMTDevice_Data.as_asgi()),
]