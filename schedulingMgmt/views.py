from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import ITMS , get_db_cursor 
from .permissions import IsUber
from .serializers import *
from vehicle.permissions import IsMBMT
from rest_framework import status
from database.models import *
from rest_framework.parsers import MultiPartParser
from VehicalTracking import settings
from vehicle.utils import format_error_message , error_simplifier



class GetRouteList(GenericAPIView):
    serializer_class =GetRouteListSerializer
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
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
            itms = ITMS(cursor, user_group)
            RouteList = itms.get_route_list(date)
            return Response(
                {
                    "status": "success",
                    "data": {
                        'route_list' : RouteList
                }
                } , status= status.HTTP_200_OK
            )
        else:
            key, value =list(serializer.errors.items())[0]
            error_message = key + ", " + value[0]
            return Response(
                {
                    "status": "error",
                    "message": error_message
                }, status=status.HTTP_400_BAD_REQUEST
            )



class GetRouteListForPartik(GenericAPIView):
    serializer_class =GetRouteListSerializer
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
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
            itms = ITMS(cursor, user_group)
            RouteList = itms.get_route_list(date)
            return Response(
                {
                    "status": "success",
                    "data": {
                        'route_list' : RouteList
                }
                } , status= status.HTTP_200_OK
            )
        else:
            key, value =list(serializer.errors.items())[0]
            error_message = key + ", " + value[0]
            return Response(
                {
                    "status": "error",
                    "message": error_message
                }, status=status.HTTP_400_BAD_REQUEST
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
    serializer_class = GetBussesListSerializer
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]
    parser_classes = [MultiPartParser]


    
    def get(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        # date = self.request.query_params.get('date')
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            date = serializer.validated_data.get('date')
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
        
            buses_list = itms.get_buses_detail_list(date)
            return Response(
                {
                    "status": "success",
                    "data": {
                        
                        'buses_list' : buses_list
                }
                } , status= status.HTTP_200_OK
            )
        else:
            key, value =list(serializer.errors.items())[0]
            error_message = key + ", " + value[0]
            return Response(
                {
                    "status": "error",
                    "message": error_message
                }, status=status.HTTP_400_BAD_REQUEST

            )


class GetBussesListForPartik(GenericAPIView):
    serializer_class = GetBussesListSerializer
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]
    # parser_classes = [MultiPartParser]


    
    def post(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        # date = self.request.query_params.get('date')
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            date = serializer.validated_data.get('date')
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
        
            buses_list = itms.get_buses_detail_list(date)
            return Response(
                {
                    "status": "success",
                    "data": {
                        
                        'buses_list' : buses_list
                }
                } , status= status.HTTP_200_OK
            )
        else:
            key, value =list(serializer.errors.items())[0]
            error_message = key + ", " + value[0]
            return Response(
                {
                    "status": "error",
                    "message": error_message
                }, status=status.HTTP_400_BAD_REQUEST
            )



class GetChargersList(GenericAPIView):
    
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]
    parser_classes = [MultiPartParser]
    serializer_class = GetChargersListSerializer

    
    
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
            try:
                Charger_list = itms.get_charger_detail_list(choice, date)
            except:
                return Response(Charger_list , status= 400)
            return Response(
                {
                    "status": "success",
                    "data": {
                        'Charger_list' : Charger_list
                }
                } , status= status.HTTP_200_OK
            )
        else:
            
            key, value =list(serializer.errors.items())[0]
            error_message = key + ", " + value[0]
            return Response(
                {
                    "status": "error",
                    "message": error_message
                }, status=status.HTTP_400_BAD_REQUEST
            )
    


class GetChargerDetail(GenericAPIView):
    serializer_class = ChargerDetailSerializer
    permission_classes = [IsAuthenticated , IsUber | IsMBMT ]
    parser_classes = [MultiPartParser]


    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            choice = serializer.validated_data.get('choice')
            date = serializer.validated_data.get('date')
            charger_id = serializer.validated_data.get('charger_id')
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
            Charger_list = itms.get_charger_Details(choice, date , charger_id)
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
        # bus_deployed = itms.get_buses_count()
        trip_count = itms.get_trip_count(vehicalNumber,start_date,end_date )
        distance = itms.get_distance_km(vehicalNumber,start_date,end_date )
        route_count = itms.get_route_count()
        buses_count = itms.get_buses_count()
        Charger_count = itms.get_charger_count()
        charging_hours = itms.get_charging_hours()
        OperationalHour = itms.get_Operational_hours()

        return Response(
            {
                "status": "success",
                "data": {

                    # "bus_deployed" : bus_deployed,
                    "route_count": route_count,
                    "Bus_count" : buses_count,
                    "Chargers": Charger_count,

                    "OperationalHour": OperationalHour ,
                    "TotalTrips": trip_count,
                    "DistanceBytrip_in_Km": distance,
                    "charging_hours": charging_hours

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