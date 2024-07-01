
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
    
class GetDashboardCountView(GenericAPIView):
    serializer_class = GetTotalTripCountSerilizsers 
    permission_classes = [IsAuthenticated]
    def get(self ,request ):
        connection = db_connection.get_connection()
        cursor = connection.cursor()
        

        data = request.data
        vehicalNumber = data.get('vehicalNumber')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if vehicalNumber and start_date:
            cursor.execute(f'''SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId ) as TotalTrips
                FROM   MTN_BusInformation INNER JOIN
                OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
                OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
                OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
                where OPR_SchedulingDetailsTrip.IsLost=0

                and MTN_BusInformation.VehicleNumber= '{vehicalNumber}' and OPR_Scheduling.SchedulingDate BETWEEN '{start_date}' AND '{end_date}' ''')
            
        else:
            cursor.execute('''SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId ) as TotalTrips
                        FROM   MTN_BusInformation INNER JOIN
                        OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
                        OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
                        OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
                        where OPR_SchedulingDetailsTrip.IsLost=0''')
            
        
        # routes
                        
        trip_count = cursor.fetchall()
        return Response(
            {
                "status": "success",
                "data": {
                    "TotalTrips": trip_count[0][0]
                }
            }
        )






