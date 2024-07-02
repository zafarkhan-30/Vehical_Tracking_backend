
from .db_connection import  DatabaseConnection
from rest_framework.response import Response
db_config = {
            'server': '103.248.60.42',
            'database': 'ITMS',
            'username': 'sa',
            'password': 'vtpl@123',
            'driver': '{ODBC Driver 17 for SQL Server}'
        }


db_connection  = DatabaseConnection(**db_config)
connection = db_connection.get_connection()
cursor = connection.cursor()



def Get_route_count():
    cursor.execute('''
                    SELECT COUNT(DISTINCT(Code)) FROM OPR_Route;
                    ''')
        
        
    route_count = cursor.fetchall()
    return route_count

def Get_Trip_Count(vehicalNumber , start_date , end_date):

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
    return trip_count



def Get_Distance_Km(vehicalNumber , start_date , end_date):
    if vehicalNumber and start_date and end_date:
            
            distance = cursor.execute(f'''SELECT sum(KML) AS DistanceBytrip, Sum(ODMeter) AS DistanceByOdometer  from (
                    Select  sum(T.DistanceInKM) As KML,(D.EndODO  -D.StartODO) As ODMeter From OPR_SchedulingDetailsTrip  As T  left join  
                    OPR_SchedulingDetails As D on T.SchedulingDetailsId=D.SchedulingDetailsId  where D.Businformationid  
                    in (Select Businformationid from MTN_BusInformation  where VehicleNumber='{vehicalNumber}') 
                    and  SchedulingId in (Select  SchedulingId From OPR_Scheduling where SchedulingDate BETWEEN '{start_date}' AND '{end_date}')
                    and T.IsLost <> 1 and T.IsDelete <>1  and  T.IsDead <>1
                    group by D.StartODO,D.EndODO)   X ''')
    else:
        
        distance = cursor.execute(f'''SELECT 
                SUM(T.DistanceInKM) AS KML,
                (SUM(D.EndODO) - SUM(D.StartODO)) AS ODMeter,
                COUNT(DISTINCT B.BusInformationId) AS TotalBuses
            FROM 
                OPR_SchedulingDetailsTrip AS T  
                LEFT JOIN OPR_SchedulingDetails AS D ON T.SchedulingDetailsId = D.SchedulingDetailsId  
                LEFT JOIN MTN_BusInformation AS B ON D.BusInformationId = B.BusInformationId
            WHERE 
                T.IsLost <> 1 
                AND T.IsDelete <> 1  
                AND T.IsDead <> 1;''')
        
    distance_Km = distance.fetchall()
    return distance_Km