from django.urls import path
from .views import *

urlpatterns = [ 

 
    path('GetRouteListjson/', GetRouteList.as_view(),),
    
    # path('GetRouteList/', GetRouteList.as_view(), ),
 
    path('GetallBussesListjson/', GetBussesList.as_view(), ),
   
    path('GetChargersListjson/', GetChargersList.as_view(), ),
  
    path('GetChargerDetailjson/', GetChargerDetailForPartik.as_view(), ),
    
    path('GetBussesList/<str:scheduling_date>/<int:route_id>/', GetScheduleBusesList.as_view(), ),


    path('get-dashboard-count/', GetdashboardCountView.as_view(),),



]