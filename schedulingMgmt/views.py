from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import ITMS , get_db_cursor , Vehicletracking
from .permissions import IsUber
from .serializers import *
from vehicle.permissions import IsMBMT
from rest_framework import status
from database.models import *
from rest_framework.parsers import MultiPartParser
from VehicalTracking import settings
from vehicle.utils import format_error_message , error_simplifier



class GetRouteList(GenericAPIView):
    serializer_class =None
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]

    def get(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        try:
            cursor = get_db_cursor()
        except Exception as e:
                return Response(
                    {
                        "status": "error",
                        "message": str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        itms = ITMS(cursor, user_group)
        RouteList = itms.get_route_list()
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
        user_group = str(request.user.groups.first())
        try:
            cursor = get_db_cursor()
        except Exception as e:
                return Response(
                    {
                        "status": "error",
                        "message": str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        itms = ITMS(cursor , user_group)
        Buses_list = itms.Get_Schedule_Buses_List(scheduling_date ,route_id)

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

    def get_queryset(self , user_group):
       
        queryset = devices.objects.filter(name__icontains=user_group)  
        return queryset
    
    def get(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        date = self.request.query_params.get('date')
        try:
            cursor = get_db_cursor()
        except Exception as e:
                return Response(
                    {
                        "status": "error",
                        "message": str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        itms = ITMS(cursor , user_group)
        distance = itms.get_distance_km()
        if date:
            buses_list = itms.get_buses_detail_list(date)
        else:
            all_devices = self.get_queryset(user_group)
            live = Vehicletracking.get_live_bus_details(all_devices)
            return Response({
                        "status": "success",
                        "data": {
                            'buses_list' : live
                    }
                    } , status= status.HTTP_200_OK)
        return Response(
            {
                "status": "success",
                "data": {
                    
                    'buses_list' : buses_list
            }
            } , status= status.HTTP_200_OK
        )


class GetChargersList(GenericAPIView):
    
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]
    parser_classes = [MultiPartParser]
    serializer_class = GetChargersListSerializer

    def get_queryset(self , user_group):
        queryset = devices.objects.filter(name__icontains=user_group)  
        return queryset
    
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            choice = serializer.validated_data.get('choice')
            date = serializer.validated_data.get('date')
            user_group = str(request.user.groups.first())
            try:
                cursor = get_db_cursor()
            except Exception as e:
                return Response(
                    {
                        "status": "error",
                        "message": str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            itms = ITMS(cursor , user_group)
        
            Charger_list = itms.get_charger_detail_list(choice, date)
            return Response(
                {
                    "status": "success",
                    "data": {
                        'Charger_list' : Charger_list
                }
                } , status= status.HTTP_200_OK
            )
        else:
            
            error_message = error_simplifier(serializer.errors)
            
            return Response({
                "status": "error",
                "message": error_message} ,
                status=status.HTTP_400_BAD_REQUEST)
    



class GetdashboardCountView(GenericAPIView):
    serializer_class = GetTotalTripCountSerilizsers
    permission_classes = [IsAuthenticated , IsUber | IsMBMT]

    def get(self ,request ):
        user_group = str(request.user.groups.first())
        data = request.data
        vehicalNumber = data.get('vehicalNumber')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        try:
            cursor = get_db_cursor()
        except Exception as e:
                return Response(
                    {
                        "status": "error",
                        "message": str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        itms = ITMS(cursor , user_group)

        trip_count = itms.get_trip_count(vehicalNumber,start_date,end_date )
        distance = itms.get_distance_km(vehicalNumber,start_date,end_date )
        route_count = itms.get_route_count()
        buses_count = itms.get_buses_count()
        Charger_count = itms.get_charger_count()


        return Response(
            {
                "status": "success",
                "data": {
                    "route_count": route_count,
                    "Bus_count" : buses_count,
                    "TotalTrips": trip_count,
                    "DistanceBytrip_in_Km": distance,
                    "Chargers": Charger_count,

                }
            }
        )










# from sqlalchemy import create_engine 
# import geopandas as gpd
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# import os


# class ImportShapeFile(GenericAPIView):
#     serializer_class = ImportShapeFileSerializer
#     parser_classes = [MultiPartParser]

#     def post(self, request):
#         db_settings = settings.DATABASES['default']
                
#         # Construct the connection string
#         user = db_settings['USER']
#         password = db_settings['PASSWORD']
#         host = db_settings['HOST']
#         port = db_settings['PORT']
#         database = db_settings['NAME']

#         conn = f"postgresql://{user}:{password}@{host}:{port}/{database}"
#         engine = create_engine(conn)

#         shape_file = request.FILES.get('shape_file')
        
#         if not shape_file:
#             return Response({"error": "No shapefile provided"}, status=status.HTTP_400_BAD_REQUEST)

#         # Save the uploaded file to the temporary directory
#         file_name = default_storage.save(shape_file.name, ContentFile(shape_file.read()))
#         file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        
       
#         # Read the shapefile using GeoPandas
#         gdf = gpd.read_file(file_path)
#         print(gdf)
        
#         # gdf.to_postgis(name="boundary", con=engine, schema="public", if_exists='replace')
#         return Response(None)