from django.urls import path
from .views import *

urlpatterns = [ 


    # path('GetRoutelistView/', GetRoutelistView.as_view(),  ),
    path('get-dashboard-count/', GetDashboardCountView.as_view(),  ),

    
]