
from .db_connection import  DatabaseConnection


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



def Get_Buses_List(scheduling_date , route_id):

    cursor.execute(f'''
                    SELECT o.RouteId as RouteId, osd.BusInformationId as BusInformationId , os.SchedulingDate as SchedulingDate , osd.BusCode as BusCode , o.Code as ScheduleCode
                    FROM OPR_Scheduling os
                    JOIN OPR_SchedulingDetails osd ON os.SchedulingId = osd.SchedulingId
                    JOIN OPR_Schedule o ON osd.ScheduleId = o.ScheduleId
                    WHERE os.SchedulingDate = '{scheduling_date}'  AND o.RouteId = {route_id} ;
                    ''')
     
    result = cursor.fetchall()
    buses_list = [{'RouteId': row.RouteId , 'BusInformationId' : row.BusInformationId , 
                   'BusCode': row.BusCode , 'ScheduleCode' : row.ScheduleCode } for row in result]
    
    return buses_list

def Get_Charger_count(user_group):
    if user_group == 'MBMT':
            company_id = 1
    elif user_group == 'Uber':
        company_id = 2

    cursor.execute(f'''
                    SELECT COUNT(*) as ChargerCount
                    FROM MTN_ChargerMaster
                    WHERE CompanyId = '{company_id}';
                    ''')
    
    charger_count = cursor.fetchall()
    return charger_count[0][0]



def get_route_list(user_group):
    if user_group == 'MBMT':
            company_id = 1
    elif user_group == 'Uber':
        company_id = 2

    cursor.execute(f'''
                    SELECT RouteId ,Name , Code FROM OPR_Route WHERE CompanyId = '{company_id}';
                    ''')
    result = cursor.fetchall()
    route_list = [{'route_id': row.RouteId , 'Name': row.Name , 'Code': row.Code} for row in result]
    return route_list


def get_MBMT_busses_list():
    cursor.execute('''
                    SELECT BusCode, VehicleNumber, ChasisNumber
                    FROM MTN_BusInformation
                    WHERE CompanyId=1;
                    ''')
        
    MBMT_busses_list = cursor.fetchall()
    
    buses_list = [{'BusCode': row.BusCode, 'VehicleNumber': row.VehicleNumber, 
                   'ChasisNumber': row.ChasisNumber} for row in MBMT_busses_list]
    return buses_list 


def get_Uber_busses_list():
    cursor.execute('''
                    SELECT BusCode, VehicleNumber, ChasisNumber
                    FROM MTN_BusInformation
                    WHERE CompanyId=2;
                    ''')
        
        
    Uber_busses_list = cursor.fetchall()
    buses_list = [{'BusCode': row.BusCode, 'VehicleNumber': row.VehicleNumber, 
                   'ChasisNumber': row.ChasisNumber} for row in Uber_busses_list]
    return buses_list 




def Get_route_count(user_group):
    if user_group == 'MBMT':
            company_id = 1
    elif user_group == 'Uber':
        company_id = 2

    cursor.execute(f'''
                    SELECT COUNT(DISTINCT(Code)) FROM OPR_Route WHERE CompanyId = '{company_id}';
                    ''')
        
        
    route_count = cursor.fetchall()
    return route_count[0][0]


def Get_Buses_count(user_group):
    if user_group == "MBMT":
        bus_count = cursor.execute('''
                        SELECT COUNT(*) FROM  MTN_BusInformation
                        WHERE CompanyId=1 ;
                        ''')   

    elif user_group == "Uber":  
        bus_count = cursor.execute('''
                        SELECT COUNT(*) FROM MTN_BusInformation
                        WHERE CompanyId=2 ;
                        ''') 


    buses_count = bus_count.fetchone()
    return buses_count[0]
    
  
def Get_Trip_Count(vehicalNumber , start_date , end_date , user_group):
    if user_group == 'MBMT':
            company_id = 1
    elif user_group == 'Uber':
        company_id = 2


    if vehicalNumber and start_date and end_date:
        
             
        trip= cursor.execute(f'''SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId ) as TotalTrips
            FROM   MTN_BusInformation INNER JOIN
            OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
            OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
            OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
            where OPR_SchedulingDetailsTrip.IsLost=0 and MTN_BusInformation.CompanyId = {company_id}
            and MTN_BusInformation.VehicleNumber= '{vehicalNumber}' and OPR_Scheduling.SchedulingDate BETWEEN '{start_date}' AND '{end_date}' ''')

    else:
        trip = cursor.execute(f'''SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId ) as TotalTrips
                    FROM   MTN_BusInformation INNER JOIN
                    OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
                    OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
                    OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
                    where OPR_SchedulingDetailsTrip.IsLost=0 and MTN_BusInformation.CompanyId = {company_id}''')
        
    
    trip_count = trip.fetchall()
    return trip_count[0][0]



def Get_Distance_Km(vehicalNumber , start_date , end_date , user_group):

    if user_group == 'MBMT':
            company_id = 1
    elif user_group == 'Uber':
        company_id = 2
    if vehicalNumber and start_date and end_date:
            
        #query written by gaurav jain
        '''SELECT SUM(OPR_SchedulingDetailsTrip.DistanceInKM ) as TotalKms
        FROM   MTN_BusInformation INNER JOIN
        OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
        OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
        OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
        where OPR_SchedulingDetailsTrip.IsLost=0
        and MTN_BusInformation.VehicleNumber='MH04LQ5736' and OPR_Scheduling.SchedulingDate='2024-06-01' '''
     
        distance = cursor.execute(f'''SELECT SUM(OPR_SchedulingDetailsTrip.DistanceInKM ) as TotalKms
            FROM   MTN_BusInformation INNER JOIN
            OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN
            OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN
            OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
            where OPR_SchedulingDetailsTrip.IsLost=0 and MTN_BusInformation.CompanyId = {company_id}
            and MTN_BusInformation.VehicleNumber='{vehicalNumber}' and OPR_Scheduling.SchedulingDate BETWEEN '{start_date}' AND '{end_date}' ''')
        

    else:
        
        distance = cursor.execute(f'''SELECT SUM(OPR_SchedulingDetailsTrip.DistanceInKM ) as TotalKms

                        FROM  MTN_BusInformation INNER JOIN

                        OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId INNER JOIN

                        OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId INNER JOIN

                        OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId

                        where OPR_SchedulingDetailsTrip.IsLost=0 and MTN_BusInformation.CompanyId = {company_id}''' )
        
        
    distance_Km = distance.fetchall()
    distance_ = distance_Km[0][0]
    if distance_ is None:
        distance_Km = 0
    else:
        distance_Km = distance_
    
    return round(distance_Km)