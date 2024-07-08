from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .utils import *
from .permissions import IsUber
from .serializers import *
from vehicle.permissions import IsMBMT
from rest_framework import status
import json



class GetRouteList(GenericAPIView):
    serializer_class =None
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]

    def get(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        RouteList = get_route_list(user_group)

        return Response(
            {
                "status": "success",
                "data": {
                    'route_list' : RouteList
            }
            } , status= status.HTTP_200_OK
        )




class GetScheduleBusesList(GenericAPIView):
    permission_classes= [IsAuthenticated , IsUber | IsMBMT ]
    serializer_class = None
    def get(self , request, scheduling_date , route_id , *args, **kwargs):
        # user_group = str(request.user.groups.first())
        Buses_list = Get_Buses_List(scheduling_date ,route_id)

        return Response(
            {
                "status": "success",
                "data": {
                    'buses_list' : Buses_list
            }
            } , status= status.HTTP_200_OK
        )









class GetBussesList(GenericAPIView):
    serializer_class = None
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]
    def get(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        print(user_group)
        if user_group == 'MBMT':
            buses_list = get_MBMT_busses_list() 

        elif user_group == 'Uber':
            buses_list = get_Uber_busses_list()
        
        return Response(
            {
                "status": "success",
                "data": {
                    'buses_list' : buses_list
            }
            } , status= status.HTTP_200_OK
        )


class GetdashboardCountView(GenericAPIView):
    serializer_class = GetTotalTripCountSerilizsers
    permission_classes = [IsAuthenticated , IsUber | IsMBMT]

    def get(self ,request ):
        user_groups = str(request.user.groups.first())
        data = request.data
        vehicalNumber = data.get('vehicalNumber')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        trip_count = Get_Trip_Count(vehicalNumber,start_date,end_date , user_groups)
        distance = Get_Distance_Km(vehicalNumber,start_date,end_date , user_groups)
        route_count = Get_route_count(user_groups)
        buses_count = Get_Buses_count(user_groups)

        return Response(
            {
                "status": "success",
                "data": {
                    "route_count": route_count,
                    "Bus_count" : buses_count,
                    "TotalTrips": trip_count,
                    "DistanceBytrip_in_Km": distance,
                    # "DistanceByodometer_in_Km":round(distance_count[0][1])
                }
            }
        )









