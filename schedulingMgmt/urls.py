from django.urls import path
from .views import *

urlpatterns = [ 


    # path('GetRoutelistView/', GetRoutelistView.as_view(),  ),
    path('get-dashboard-count/', GetdashboardCountView.as_view(),  ),
    # path('get-distance-count/', GetDistanceKmView.as_view(),  ),
    # path('get-route-count/', routeCount.as_view(),  ),

    
]