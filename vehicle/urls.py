from django.urls import path
from .views import *

urlpatterns = [ 


    path('registeration/', UserRegister.as_view(),  ),
    path('token/', LoginView.as_view(),  ),
    path('post-Master-Device-Data/', PostMasterDeviceData.as_view(),  ),
    path('Get-Device-Details/', ViewDeviceAllDetails.as_view(),  ),
    path('Get-AllMBMTDevice-Details/', ViewAllMBMTDeviceDetails.as_view(),  ),
    path('Get-AmnexDevice-Details/', ViewAmnexDeviceDetails.as_view(),  ),
    path('Get-Device-parameters-Details/', GetDeviceParametersDetails.as_view(),  ),
    path('Get-Get-Device-data-Details/<str:device_name>/<str:start_date>/<str:end_date>/', GettimeRangedateData.as_view(),  ),

    
]
            