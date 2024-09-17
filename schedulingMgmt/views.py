from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import ITMS
from .permissions import IsUber
from .serializers import *
from vehicle.permissions import IsMBMT
from rest_framework import status
from database.models import *
from rest_framework.parsers import MultiPartParser
from VehicalTracking import settings
from vehicle.utils import format_error_message, error_simplifier
from .utils import db_config


class GetRouteList(GenericAPIView):
    serializer_class = GetRouteListSerializer
    permission_classes = [IsAuthenticated, IsUber | IsMBMT]

    def post(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        page = self.request.query_params.get('page')
        page_size = self.request.query_params.get('page_size')
        date = self.request.query_params.get('date')
        route_number = self.request.query_params.get('route_number')

        result = {"status": "error",
                  "message": "Unable to retrieve buses list"}

        try:
            itms = ITMS(db_config, user_group)
            RouteList = itms.get_route_list(
                date, route_number, page, page_size)

            result = {
                "status": "success",
                "data": {
                    'Route_list': RouteList[0]
                }
            }
            if page and page_size:
                total_count = RouteList[1]
                result['data'].update({
                    'total_count': total_count,
                    'total_page_count': itms.custom_round_up(total_count / int(page_size)),
                    'page': int(page),
                    'page_size': int(page_size)
                })

        except Exception as e:
            result['message'] = str(e)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


class GetScheduleBusesList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsUber | IsMBMT]
    serializer_class = None

    def get(self, request, scheduling_date, route_id, *args, **kwargs):
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
        Buses_list = itms.Get_Schedule_Buses_List(scheduling_date, route_id)

        return Response(
            {
                "status": "success",
                "data": {
                    'buses_list': Buses_list
                }
            }, status=status.HTTP_200_OK
        )


class GetBussesList(GenericAPIView):
    serializer_class = GetBussesListSerializer
    permission_classes = [IsAuthenticated, IsUber | IsMBMT]

    def post(self, request, *args, **kwargs):
        user_group = str(request.user.groups.first())
        date = self.request.query_params.get('date')
        vehicle_number = self.request.query_params.get('vehical')
        page = self.request.query_params.get('page')
        page_size = self.request.query_params.get('page_size')

        result = {"status": "error",
                  "message": "Unable to retrieve buses list"}

        try:
            # cursor = get_db_cursor()

            itms = ITMS(db_config, user_group)
            buses_list = itms.get_buses_detail_list(
                date, vehicle_number, page, page_size)
            # print (type(total_count))
            result = {
                "status": "success",
                "data": {
                    'buses_list': buses_list[0]
                }
            }

            if page and page_size:
                total_count = buses_list[1]
                result['data'].update({
                    'total_count': total_count,
                    'total_page_count': itms.custom_round_up(int(total_count) / int(page_size)),
                    'page': int(page),
                    'page_size': int(page_size)
                })

        except Exception as e:
            result['message'] = str(e)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


class GetChargersList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsUber | IsMBMT]
    # parser_classes = [MultiPartParser]
    # serializer_class = GetChargersListSerializer

    def post(self, request, *args, **kwargs):

        user_group = str(request.user.groups.first())
        charger_name = self.request.query_params.get('charger_name')
        choice = self.request.query_params.get('choice')
        date = self.request.query_params.get('date')
        page = self.request.query_params.get('page')
        page_size = self.request.query_params.get('page_size')

        result = {"status": "error",
                  "message": "Unable to retrieve buses list"}
        try:
            cursor = get_db_cursor()
            itms = ITMS(db_config, user_group)
            Charger_list = itms.get_charger_detail_list(
                choice, date, charger_name, page, page_size)
            result = {
                "status": "success",
                "data": {
                    'Charger_list': Charger_list[0]
                }
            }
            if page and page_size:
                total_count = Charger_list[1]
                result['data'].update({
                    'total_count': total_count,
                    'total_page_count': itms.custom_round_up(total_count / int(page_size)),
                    'page': int(page),
                    'page_size': int(page_size)
                })
        except Exception as e:
            result['message'] = str(e)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


class GetChargerDetail(GenericAPIView):
    serializer_class = ChargerDetailSerializer
    permission_classes = [IsAuthenticated, IsUber | IsMBMT]
    parser_classes = [MultiPartParser]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
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
            itms = ITMS(cursor, user_group)
            Charger_list = itms.get_charger_Details(choice, date, charger_id)
            return Response(
                {
                    "status": "success",
                    "data": {
                        'Charger_list': Charger_list
                    }
                }, status=status.HTTP_200_OK
            )
        else:
            # error_message = error_simplifier(serializer.errors)
            key, value = list(serializer.errors.items())[0]
            error_message = key + ", " + value[0]
            return Response({
                "status": "error",
                "message": error_message},
                status=status.HTTP_400_BAD_REQUEST)


class GetChargerDetailForPartik(GenericAPIView):
    serializer_class = ChargerDetailSerializer
    permission_classes = [IsAuthenticated, IsUber | IsMBMT]
    # parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
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
            itms = ITMS(cursor, user_group)
            Charger_list = itms.get_charger_Details(choice, date, charger_id)
            return Response(
                {
                    "status": "success",
                    "data": {
                        'Charger_list': Charger_list
                    }
                }, status=status.HTTP_200_OK
            )
        else:
            # error_message = error_simplifier(serializer.errors)
            key, value = list(serializer.errors.items())[0]
            error_message = key + ", " + value[0]
            return Response({
                "status": "error",
                "message": error_message},
                status=status.HTTP_400_BAD_REQUEST)


class GetdashboardCountView(GenericAPIView):
    serializer_class = GetTotalTripCountSerilizsers
    permission_classes = [IsAuthenticated, IsUber | IsMBMT]

    def get(self, request):
        user_group = str(request.user.groups.first())
        data = request.data
        vehicalNumber = data.get('vehicalNumber')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
    
        # try:

        itms = ITMS(db_config, user_group)
        
        return Response({
            "status": "success",
            "data": {
                "route_count": itms.get_route_count(),
                "Bus_count": itms.get_buses_count(),
                "Chargers": itms.get_charger_count(),
                "OperationalHour": itms.get_Operational_hours(),
                "TotalTrips": itms.get_trip_count(vehicalNumber, start_date, end_date),
                "DistanceBytrip_in_Km": itms.get_distance_km(vehicalNumber, start_date, end_date),
                "charging_hours": itms.get_charging_hours()
            }
        })
        # except Exception as e:
        #     return Response({
        #         "status": "error",
        #         "message": str(e)
        #     }, status=status.HTTP_400_BAD_REQUEST)
