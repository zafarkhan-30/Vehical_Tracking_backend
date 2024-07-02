from django.urls import path
from .views import *

urlpatterns = [ 


    # path('GetRoutelistView/', GetRoutelistView.as_view(),  ),
    path('get-trip-count/', GetTripCountView.as_view(),  ),
    path('get-distance-count/', GetDistanceKmView.as_view(),  ),
    path('get-route-count/', routeCount.as_view(),  ),

    
]