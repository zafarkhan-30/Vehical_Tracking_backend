from django.urls import path
from .consumers import  GetDevice_Data



websocket_urlpatterns = [
    
    path('ws/get-divce-data/', GetDevice_Data.as_asgi()),
]