from django.urls import path
from .views import *

urlpatterns = [ 

    path('GetBussesList/', GetBussesList.as_view(),  ),
    path('get-dashboard-count/', GetdashboardCountView.as_view(),  ),

    
]