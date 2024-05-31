from django.urls import path
from .views import *

urlpatterns = [
    path('post-Device-Details/', PostDeviceDetailsView.as_view(),  ),
    path('Get-Device-Details/', ViewDeviceAllDetails.as_view(),  ),
    path('Get-AllMBMTDevice-Details/', ViewAllMBMTDeviceDetails.as_view(),  ),
    path('Get-AmnexDevice-Details/', ViewAmnexDeviceDetails.as_view(),  ),
    path('Get-Device-parameters-Details/', GetDeviceParametersDetails.as_view(),  ),
]
