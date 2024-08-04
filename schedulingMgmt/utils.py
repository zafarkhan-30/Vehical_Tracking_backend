
from .db_connection import  DatabaseConnection
from database.models import MasterDeviceDetails
from .serializers import *
from datetime import  date
import random
from rest_framework.response import Response
import pyodbc
from VehicalTracking.settings import ITMS_SERVER , ITMS_DRIVER, ITMS_PASSWORD , ITMS_USERNAME , ITMS_DATABASE_NAME
# from .db_connection import DatabaseConnection


db_config = {
            'server': ITMS_SERVER,
            'database': ITMS_DATABASE_NAME,
            'username': ITMS_USERNAME,
            'password': ITMS_PASSWORD,
            'driver': ITMS_DRIVER
        }


db_connection  = DatabaseConnection(**db_config)

def get_db_cursor():
    try:
        connection = db_connection.get_connection()
        return connection.cursor()
    except Exception as e:
        return Response({"status": "error", "message":"Connection error, Try again in few minutes" ,
                         "error_message" : str(e) } , status= 400)


class ITMS:
    def __init__(self, cursor, user_group):
        """
            Initialize an instance of ITMS class.
            Parameters:
            cursor (object): A database cursor object to execute SQL queries.
            user_group (str): The user group for which the ITMS instance is being created.
            Returns:
            None
        """
        self.cursor = cursor
        self.company_id = self.get_company_id(user_group)

    def get_company_id(self, user_group):
        if user_group == 'MBMT':
            return 1
        elif user_group == 'Uber':
            return 2
        return None

    def get_route_list(self , date):
        self.cursor.execute(f'''
           SELECT 
            r.RouteId AS RouteId,
            r.Name AS Name,
            r.Code AS Code,
            os.SchedulingDate AS Date , 
            COUNT(DISTINCT osd.BusInformationId) AS NumberOfBuses,
            COUNT(DISTINCT o.Code) AS NumberOfScheduleCodes,
            SUM(o.TotalTrip) AS TotalTrip
            FROM 
                OPR_Scheduling os
            JOIN 
                OPR_SchedulingDetails osd ON os.SchedulingId = osd.SchedulingId
            JOIN 
                OPR_Schedule o ON osd.ScheduleId = o.ScheduleId
            JOIN 
                OPR_Route r ON o.RouteId = r.RouteId
            WHERE 
                os.SchedulingDate = '{date}' AND r.CompanyId = '{self.company_id}'
            GROUP BY 
                r.RouteId,
                r.Name,
                r.Code,
                os.SchedulingDate 
            ORDER BY 
                r.RouteId;
        ''')
        result = self.cursor.fetchall()
        return [{'route_id': row.RouteId, 'Name': row.Name, 
                 'Code': row.Code , 
                 'date' : row.Date ,
                 'NumberOfBuses': row.NumberOfBuses , 
                 'NumberOfSchedules' : row.NumberOfScheduleCodes,
                 'TotalTrip' : row.TotalTrip , 
                 'route_length' : random.randint(20,50) # need to update route length
                 } for row in result]

    def get_route_count(self):
        self.cursor.execute(f'''
            SELECT COUNT(DISTINCT Code) 
            FROM OPR_Route 
            WHERE CompanyId = '{self.company_id}';
        ''')
        return self.cursor.fetchone()[0]

    def get_buses_detail_list(self , date = None):
        to_get_the_status= self.cursor.execute(f'''
                        SELECT 
                        mtn.BusInformationId,
                        mtn.BusCode,
                        mtn.VehicleNumber,
                        MAX(osd.SchedulingDate) AS LatestSchedulingDate,
                        MAX(osd.StartODO) AS StartODO,
                        MAX(osd.EndODO) AS EndODO,
                        COALESCE(MAX(osd.EndODO) - MAX(osd.StartODO), 0) AS TotalKmRunToday,
                        CASE WHEN COUNT(osd.SchedulingId) > 0 THEN 'Active'
                            ELSE 'Not Scheduled'
                        END AS Status,
                        COALESCE(lastOdo.EndODO, 0) AS LastODO,
                        COALESCE(SUM(bc.EnergyConsumption), 0) AS TotalEnergyConsumed,
                        COALESCE(SUM(CASE 
                            WHEN bc.ChargingDate = '{date}' THEN bc.EnergyConsumption 
                            ELSE 0 
                        END), 0) AS TodayEnergyConsumption,
                        SUM(CASE 
	                    WHEN bc.EndSOC - bc.StartSOC > 0 THEN bc.EndSOC - bc.StartSOC 
                            ELSE 0 END) / 100.0 AS ChargingCycles
                    FROM 
                        MTN_BusInformation mtn
                    LEFT JOIN 
                        (
                            SELECT 
                                osd.BusInformationId,
                                osd.SchedulingId,
                                osd.StartODO,
                                osd.EndODO,
                                os.SchedulingDate
                            FROM 
                                OPR_SchedulingDetails osd
                            JOIN 
                                OPR_Scheduling os ON osd.SchedulingId = os.SchedulingId
                            WHERE 
                                os.SchedulingDate = '{date}' 
                                AND osd.IsDelete = 0
                                AND (os.IsDelete = 0 OR os.IsDelete IS NULL)
                        ) osd ON mtn.BusInformationId = osd.BusInformationId
                    LEFT JOIN 
                        (
                            SELECT 
                                BusInformationId, 
                                MAX(EndODO) AS EndODO
                            FROM 
                                OPR_SchedulingDetails
                            WHERE 
                                IsDelete = 0
                            GROUP BY 
                                BusInformationId
                        ) lastOdo ON mtn.BusInformationId = lastOdo.BusInformationId
                    LEFT JOIN 
                        MTN_BusCharging bc ON mtn.BusInformationId = bc.BusInformationId
                    WHERE 
                        mtn.CompanyId = 1
                    GROUP BY 
                        mtn.BusInformationId,
                        mtn.BusCode,
                        mtn.VehicleNumber,
                        lastOdo.EndODO
                    ORDER BY 
                        mtn.BusInformationId;
                    ''')
        
        result = to_get_the_status.fetchall()
        
        query_result =  [{'VehicleNumber': row.VehicleNumber , 'BusInformationId' : row.BusInformationId , 
                    'BusCode': row.BusCode , 'Status' : row.Status , 'TotalKmRunDay' : round(row.TotalKmRunToday),
                    "Charging_cycle": round(row.ChargingCycles),
                    'totalEnergyDay_KwH': round(row.TodayEnergyConsumption),
                    'TotalEnergyConsumed_kwH' : round(row.TotalEnergyConsumed),
                    'TotalKm' : round(row.LastODO)  } for row in result]
        return query_result


    def get_charger_detail_list(self , choice , date= None):
        
        if choice == 'Day':
            time_condition = "AND (CONVERT(TIME, bc.StartTime) BETWEEN '06:00:00' AND '21:59:59')"
        elif choice == 'Night':
            time_condition = """
                AND (
                    (CONVERT(TIME, bc.StartTime) BETWEEN '22:00:00' AND '23:59:59') OR
                    (CONVERT(TIME, bc.StartTime) BETWEEN '00:00:00' AND '05:59:59')
                )
                """
        elif choice == 'Total':
            time_condition = ""
        else:
            time_condition = ""
        
        self.cursor.execute(f'''
                SELECT 
                cm.ChargerMasterId,
                cm.ChargerNumber,
                cm.Status,
                cm.SerialNumber,
                MAX(bc.ChargingDate) AS LastChargingDate,
                COALESCE(COUNT(bc.BusInformationId), 0) AS TotalBusesChargedToday,
                COALESCE(SUM(bc.EnergyConsumption), 0) AS TotalEnergyConsumedToday,
                COALESCE(SUM(CAST(bc.SessionTime AS int)) / 60.00, 0) AS TotalOperationalHoursToday,
                (
                    SELECT COUNT(bc2.BusInformationId)
                    FROM MTN_BusCharging bc2
                    WHERE bc2.ChargerMasterId = cm.ChargerMasterId
                ) AS TotalBusesChargedTillDate,
                (
                    SELECT SUM(bc2.EnergyConsumption)
                    FROM MTN_BusCharging bc2
                    WHERE bc2.ChargerMasterId = cm.ChargerMasterId
                ) AS TotalEnergyConsumedTillDate,
                (
                    SELECT SUM(CAST(bc2.SessionTime AS int)) / 60.00
                    FROM MTN_BusCharging bc2
                    WHERE bc2.ChargerMasterId = cm.ChargerMasterId
                ) AS TotalOperationalHoursTillDate
            FROM 
                MTN_ChargerMaster cm
            LEFT JOIN 
                MTN_BusCharging bc ON cm.ChargerMasterId = bc.ChargerMasterId 
                AND bc.ChargingDate = '{date}' {time_condition}
            WHERE 
                cm.CompanyId = '{self.company_id}'
            GROUP BY 
                cm.ChargerMasterId, 
                cm.ChargerNumber, 
                cm.Status,
                cm.SerialNumber
            ORDER BY 
                cm.ChargerMasterId;
        ''')
    
        
        query = self.cursor.fetchall()
        query_result = [{
            "ChargerNumber" : row.ChargerNumber , 
            "id" : row.ChargerMasterId,
            'CPU_name' : 'Klick-Watt' , 
            'Charger_name'  : 'Shuzlon Energy' , 
            "Status" : row.Status,
            'Latest_data': {
                # "date" : row.LastChargingDate ,
                'BusesCharged' : row.TotalBusesChargedToday,
                'EnergyConsumed' : round(row.TotalEnergyConsumedToday),
                'OperationalHours' : row.TotalOperationalHoursToday
            },
            'Total' : {
                'BusesCharged': row.TotalBusesChargedTillDate ,
                'EnergyConsumed' : round(row.TotalEnergyConsumedTillDate),
                'OperationalHours' : round(row.TotalOperationalHoursTillDate)
            }
        } for row in query]
        return query_result
      
    def get_charger_Details(self, choice , date , charger_id):
        if choice == 'Day':
            time_condition = "AND (CONVERT(TIME, bc.StartTime) BETWEEN '06:00:00' AND '21:59:59')"
        elif choice == 'Night':
            time_condition = """
                AND (
                    (CONVERT(TIME, bc.StartTime) BETWEEN '22:00:00' AND '23:59:59') OR
                    (CONVERT(TIME, bc.StartTime) BETWEEN '00:00:00' AND '05:59:59')
                )
                """
        elif choice == 'Total':
            time_condition = ""
        else:
            time_condition = ""

        self.cursor.execute(f'''
                SELECT 
                cm.ChargerMasterId,
                cm.ChargerNumber,
                cm.Status,
                cm.SerialNumber,
                MAX(bc.ChargingDate) AS LastChargingDate,
                COALESCE(COUNT(bc.BusInformationId), 0) AS TotalBusesChargedToday,
                COALESCE(SUM(bc.EnergyConsumption), 0) AS TotalEnergyConsumedToday,
                COALESCE(SUM(CAST(bc.SessionTime AS int)) / 60.00, 0) AS TotalOperationalHoursToday,
                (
                    SELECT COUNT(bc2.BusInformationId)
                    FROM MTN_BusCharging bc2
                    WHERE bc2.ChargerMasterId = cm.ChargerMasterId
                ) AS TotalBusesChargedTillDate,
                (
                    SELECT SUM(bc2.EnergyConsumption)
                    FROM MTN_BusCharging bc2
                    WHERE bc2.ChargerMasterId = cm.ChargerMasterId
                ) AS TotalEnergyConsumedTillDate,
                (
                    SELECT SUM(CAST(bc2.SessionTime AS int)) / 60.00
                    FROM MTN_BusCharging bc2
                    WHERE bc2.ChargerMasterId = cm.ChargerMasterId
                ) AS TotalOperationalHoursTillDate
            FROM 
                MTN_ChargerMaster cm
            LEFT JOIN 
                MTN_BusCharging bc ON cm.ChargerMasterId = bc.ChargerMasterId 
                AND bc.ChargingDate = '{date}' {time_condition}
            WHERE 
                cm.CompanyId = '{self.company_id}' AND bc.ChargerMasterId = {charger_id}
            GROUP BY 
                cm.ChargerMasterId, 
                cm.ChargerNumber, 
                cm.Status,
                cm.SerialNumber
            ORDER BY 
                cm.ChargerMasterId;
        ''')
       
        
        query = self.cursor.fetchall()
        query_result = [{
            "ChargerNumber" : row.ChargerNumber , 
            "id" : row.ChargerMasterId,
            'CPU_name' : 'Klick-Watt' , 
            'Charger_name'  : 'Shuzlon Energy' , 
            "Status" : row.Status,
            'Latest_data': {
                # "date" : row.LastChargingDate ,
                'BusesCharged' : row.TotalBusesChargedToday,
                'EnergyConsumed' : round(row.TotalEnergyConsumedToday),
                'OperationalHours' : row.TotalOperationalHoursToday
            },
            'Total' : {
                'BusesCharged': row.TotalBusesChargedTillDate ,
                'EnergyConsumed' : round(row.TotalEnergyConsumedTillDate),
                'OperationalHours' : round(row.TotalOperationalHoursTillDate)
            }
        } for row in query]
        return query_result



    def Get_Schedule_Buses_List(self , scheduling_date = None , route_id= None):
        self.cursor.execute(f'''
                        SELECT o.RouteId as RouteId, osd.BusInformationId as BusInformationId , 
                        os.SchedulingDate as SchedulingDate , osd.BusCode as BusCode , o.Code as ScheduleCode
                        FROM OPR_Scheduling os
                        JOIN OPR_SchedulingDetails osd ON os.SchedulingId = osd.SchedulingId
                        JOIN OPR_Schedule o ON osd.ScheduleId = o.ScheduleId
                        WHERE os.SchedulingDate = '{scheduling_date}'  AND o.RouteId = {route_id} ;
                        ''')
        
        result = self.cursor.fetchall()
        buses_list = [{'RouteId': row.RouteId , 'BusInformationId' : row.BusInformationId , 
                    'BusCode': row.BusCode , 'ScheduleCode' : row.ScheduleCode } for row in result]
        
        return buses_list 
         
    


    def get_buses_count(self):
        self.cursor.execute(f'''
            SELECT COUNT(*)
            FROM MTN_BusInformation
            WHERE CompanyId = '{self.company_id}' AND Status = 'Running';
        ''')
        return self.cursor.fetchone()[0]

    def get_Operational_hours(self):
        self.cursor.execute(f'''
            SELECT 
            SUM( CASE 
                WHEN TRY_CAST(StartTime AS TIME) IS NOT NULL AND TRY_CAST(EndTime AS TIME) IS NOT NULL THEN
                    CASE 
                        WHEN TRY_CAST(EndTime AS TIME) < TRY_CAST(StartTime AS TIME) 
                        THEN DATEDIFF(MINUTE, 
                                    CAST(TRY_CAST(StartTime AS TIME) AS DATETIME), 
                                    DATEADD(DAY, 1, CAST(TRY_CAST(EndTime AS TIME) AS DATETIME)))
                        ELSE DATEDIFF(MINUTE, 
                                    CAST(TRY_CAST(StartTime AS TIME) AS DATETIME), 
                                    CAST(TRY_CAST(EndTime AS TIME) AS DATETIME))
                    END
                ELSE NULL
            END) / 60.00 AS DurationInHours
        FROM OPR_SchedulingDetailsTrip;''')

        return round(self.cursor.fetchone()[0]) 

    def get_charger_count(self):
        self.cursor.execute(f'''
                        SELECT 
                            COUNT(*) as ChargerCount
                        FROM MTN_ChargerMaster
                        WHERE CompanyId = '{self.company_id}';
                        ''')
        
        return self.cursor.fetchone()[0]
    
    def get_charging_hours(self):
        self.cursor.execute(f'''
            SELECT SUM(CAST(SessionTime AS int)) / 60.00 as TotalChargingHours
            FROM MTN_BusCharging ;
        ''')
        return round(self.cursor.fetchone()[0])
    

    def get_trip_count(self, vehicle_number=None, start_date=None, end_date=None):
        query = f'''
            SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId) AS TotalTrips
            FROM MTN_BusInformation
            INNER JOIN OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId
            INNER JOIN OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId
            INNER JOIN OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
            WHERE OPR_SchedulingDetailsTrip.IsLost = 0 AND MTN_BusInformation.CompanyId = {self.company_id}
        '''
        if vehicle_number and start_date and end_date:
            query += f" AND MTN_BusInformation.VehicleNumber = '{vehicle_number}' AND OPR_Scheduling.SchedulingDate BETWEEN '{start_date}' AND '{end_date}'"

        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def get_distance_km(self, vehicle_number=None, start_date=None, end_date=None):
        query = f'''
            SELECT SUM(OPR_SchedulingDetailsTrip.DistanceInKM) AS TotalKms
            FROM MTN_BusInformation
            INNER JOIN OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId
            INNER JOIN OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId
            INNER JOIN OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
            WHERE OPR_SchedulingDetailsTrip.IsLost = 0 AND MTN_BusInformation.CompanyId = {self.company_id}
        '''
        if vehicle_number and start_date and end_date:
            query += f" AND MTN_BusInformation.VehicleNumber = '{vehicle_number}' AND OPR_Scheduling.SchedulingDate BETWEEN '{start_date}' AND '{end_date}'"

        self.cursor.execute(query)
        distance_km = self.cursor.fetchone()[0] or 0
        return round(distance_km)


class Vehicletracking:
    def get_live_bus_details(all_devices):
        data_list = []
        if all_devices:
            today = date.today()
            for device in all_devices:
                device_details = LivedeviceDetailsSerialiser(device).data
                try:
                    instance = MasterDeviceDetails.objects.filter(device_id=device, created_at__date=today).latest("created_at")
                    device_data = LiveDeviceSeailizer(instance).data
                    device_details.update(device_data)
                except MasterDeviceDetails.DoesNotExist:
                    continue
                data_list.append(device_details)
    
        return data_list