from django.urls import path
from .views import *

urlpatterns = [ 


    path('GetRoutelistView/', GetRoutelistView.as_view(),  ),
    
]