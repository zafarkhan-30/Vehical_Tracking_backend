from django.urls import path
from .consumers import LocationConsumer , GetDeviceData , GetDevice_Data

websocket_urlpatterns = [
    path('ws/location/', LocationConsumer.as_asgi()),
    path('ws/device-data/', GetDeviceData.as_asgi()),
    path('ws/GetDevice_Data/', GetDevice_Data.as_asgi()),
]