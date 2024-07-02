
from .db_connection import  DatabaseConnection
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *
db_config = {
            'server': '103.248.60.42',
            'database': 'ITMS',
            'username': 'sa',
            'password': 'vtpl@123',
            'driver': '{ODBC Driver 17 for SQL Server}'
        }


db_connection  = DatabaseConnection(**db_config)
    
class GetTripCountView(GenericAPIView):
    serializer_class = GetTotalTripCountSerilizsers 
    # permission_classes = [IsAuthenticated]
    def get(self ,request ):
        connection = db_connection.get_connection()
        cursor = connection.cursor()
        

        data = request.data
        vehicalNumber = data.get('vehicalNumber')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if vehicalNumber and start_date and end_date:
            trip= cursor.execute(f'''SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId ) as TotalTrips
                FROM   MTN_BusInformation INNER JOIN
                OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
                OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
                OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
                where OPR_SchedulingDetailsTrip.IsLost=0

                and MTN_BusInformation.VehicleNumber= '{vehicalNumber}' and OPR_Scheduling.SchedulingDate BETWEEN '{start_date}' AND '{end_date}' ''')

            
            
        else:
            trip = cursor.execute('''SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId ) as TotalTrips
                        FROM   MTN_BusInformation INNER JOIN
                        OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
                        OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
                        OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
                        where OPR_SchedulingDetailsTrip.IsLost=0''')
            
        
        trip_count = trip.fetchall()
      
        return Response(
            {
                "status": "success",
                "data": {
                    "TotalTrips": round(trip_count[0][0])
                }
            }
        )

class GetDistanceKmView(GenericAPIView):
    serializer_class = GetTotalDistanceSerilizsers

    def get(self, request):
        connection = db_connection.get_connection()
        cursor = connection.cursor()

        data = request.data
        vehicalNumber = data.get('vehicalNumber')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if vehicalNumber and start_date and end_date:
            
            distance = cursor.execute(f'''SELECT sum(KML) AS DistanceBytrip, Sum(ODMeter) AS DistanceByOdometer  from (
                    Select  sum(T.DistanceInKM) As KML,(D.EndODO  -D.StartODO) As ODMeter From OPR_SchedulingDetailsTrip  As T  left join  
                    OPR_SchedulingDetails As D on T.SchedulingDetailsId=D.SchedulingDetailsId  where D.Businformationid  
                    in (Select Businformationid from MTN_BusInformation  where VehicleNumber='{vehicalNumber}') 
                    and  SchedulingId in (Select  SchedulingId From OPR_Scheduling where SchedulingDate BETWEEN '{start_date}' AND '{end_date}')
                    and T.IsLost <> 1 and T.IsDelete <>1  and  T.IsDead <>1
                    group by D.StartODO,D.EndODO)   X ''')
        else:
            return Response({
                
                    "status": "error",
                    "message": "Please provide the required parameter"
                } , status= 400)
            
        distance_Km = distance.fetchall()
        print(distance_Km)
        return Response(
            {
                "status": "success",
                "data": {
                    "DistanceBytrip_in_Km": round(distance_Km[0][0]),
                    "DistanceByodometer_in_Km":round(distance_Km[0][1])
                }
            }
        )

class routeCount(GenericAPIView):
    serializer_class = None
    def get(self , request):

        connection = db_connection.get_connection()
        cursor = connection.cursor()
        cursor.execute('''
                    SELECT COUNT(DISTINCT(Code)) FROM OPR_Route;
                    ''')
        
        
        route_count = cursor.fetchall()
        print(route_count)
        return Response(
            {
                "status": "success",
                "data": {
                    "route_count": route_count[0][0]
                }
            }
        )

        






