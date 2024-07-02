

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .utils import *
from .serializers import *

    
class GetdashboardCountView(GenericAPIView):
    serializer_class = GetTotalTripCountSerilizsers 
    def get(self ,request ):
        
        data = request.data
        vehicalNumber = data.get('vehicalNumber')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        trip_count = Get_Trip_Count(vehicalNumber,start_date,end_date)
        distance_count = Get_Distance_Km(vehicalNumber,start_date,end_date)
        route_count = Get_route_count()
       
        return Response(
            {
                "status": "success",
                "data": {
                    "route_count": route_count[0][0],
                    "TotalTrips": round(trip_count[0][0]),
                    "DistanceBytrip_in_Km": round(distance_count[0][0]),
                    "DistanceByodometer_in_Km":round(distance_count[0][1])
                }
            }
        )









