from django.urls import path
from .views import *

urlpatterns = [ 

    path('GetRouteList/', GetRouteList.as_view(), ),
    path('GetRouteListjson/', GetRouteListForPartik.as_view(), ),
    path('GetRouteList/', GetRouteList.as_view(), ),
    path('GetallBussesList/', GetBussesList.as_view(), ),
    path('GetallBussesListjson/', GetBussesListForPartik.as_view(), ),
    path('GetChargersList/', GetChargersList.as_view(), ),
    path('GetChargerDetail/', GetChargerDetail.as_view(), ),
    path('GetBussesList/<str:scheduling_date>/<int:route_id>/', GetScheduleBusesList.as_view(), ),
    path('get-dashboard-count/', GetdashboardCountView.as_view(),),



]