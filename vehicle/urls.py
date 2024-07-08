from django.urls import path
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [ 


    path('registeration/', UserRegister.as_view(),  ),
    path('token/', LoginView.as_view(),  ),
    path('logout/', LogoutView.as_view() ),
    
    path('post-Master-Device-Data/', PostMasterDeviceData.as_view(),  ),
    path('Get-Device-Details/', ViewDeviceAllDetails.as_view(),  ),
    path('Get-AllMBMTDevice-Details/', ViewAllMBMTDeviceDetails.as_view(),  ),
    path('Get-AmnexDevice-Details/', ViewAmnexDeviceDetails.as_view() ),
    path('Get-Device-parameters-Details/', GetDeviceParametersDetails.as_view(),  ),
    path('Get-Get-Device-data-Details/<str:device_name>/<str:start_date>/<str:end_date>/', GettimeRangedateData.as_view(),  ),

    path('Get-NoidaExten-To-Incedointellect-Route', GetNoidaExtenToIncedointellectRouteView.as_view(),  ),
    path('Get-NoidaExten-To-Incedointellect-Stops', GetNoidaExtenToIncedointellectStopsView.as_view(),  ),
    path('Get-RouteNo15', GetRouteNo15View.as_view(),  ),
    path('Get-RouteNo15-BusStops', GetRouteNo15BusStopsView.as_view(),  ),

    

    
]
            