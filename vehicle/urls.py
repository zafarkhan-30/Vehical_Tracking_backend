from django.urls import path
from .views import *

urlpatterns = [
    path('post-Device-Details/', DeviceDetailsView.as_view(),  ),
    path('Get-Device-Details/', ViewDeviceDetails.as_view(),  ),
    path('Get-AllMBMTDevice-Details/', ViewAllMBMTDeviceDetails.as_view(),  ),
    path('Get-AmnexDevice-Details/', ViewAmnexDeviceDetails.as_view(),  ),
]
