
from .db_connection import  DatabaseConnection
from database.models import MasterDeviceDetails
from .serializers import *
from datetime import  date

db_config = {
            'server': '103.248.60.42',
            'database': 'ITMS',
            'username': 'sa',
            'password': 'vtpl@123',
            'driver': '{ODBC Driver 17 for SQL Server}'
        }


db_connection  = DatabaseConnection(**db_config)

def get_db_cursor():
    try:
        connection = db_connection.get_connection()
        return connection.cursor()
    except Exception as e:
        raise ConnectionError(f"An error occurred: {str(e)}")


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

    def get_route_list(self):
        self.cursor.execute(f'''
            SELECT RouteId, Name, Code 
            FROM OPR_Route 
            WHERE CompanyId = '{self.company_id}';
        ''')
        result = self.cursor.fetchall()
        return [{'route_id': row.RouteId, 'Name': row.Name, 
                 'Code': row.Code} for row in result]

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
                        END), 0) AS TodayEnergyConsumption
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
                    "SOC" : 50,
                    "Charging_cycle": 0,
                    'totalEnergyDay_KwH': round(row.TodayEnergyConsumption),
                    'TotalEnergyConsumed_kwH' : round(row.TotalEnergyConsumed),
                    'TotalKm' : round(row.LastODO)  } for row in result]
        return query_result




    def get_charger_detail_list(self , choice , date= None):
        self.cursor.execute(f'''
                    SELECT 
                mtn.BusInformationId,
                mtn.BusCode,
                MAX(osd.SchedulingDate) AS LatestSchedulingDate,
                CASE 
                    WHEN COUNT(osd.SchedulingId) > 0 THEN 'Active'
                    ELSE 'Not Scheduled'
                END AS Status
            --    MAX(osd.StartODO) AS StartODO,
            --    MAX(osd.EndODO) AS EndODO,
            --    COALESCE(MAX(osd.EndODO) - MIN(osd.StartODO), 0) AS KilometersRunToday,
                
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
                        os.SchedulingDate = '2024-07-22' 
                        AND osd.IsDelete = 0
                        AND (os.IsDelete = 0 OR os.IsDelete IS NULL)
                ) osd ON mtn.BusInformationId = osd.BusInformationId WHERE  mtn.CompanyId = 1
            GROUP BY 
                mtn.BusInformationId,
                mtn.BusCode
            ORDER BY 
                mtn.BusInformationId;
                ''')    

        
        # if choice == 'Day':
        #     time_condition = "AND (CONVERT(TIME, bc.StartTime) BETWEEN '06:00:00' AND '21:59:59')"
        # elif choice == 'Night':
        #     time_condition = """
        #         AND (
        #             (CONVERT(TIME, bc.StartTime) BETWEEN '22:00:00' AND '23:59:59') OR
        #             (CONVERT(TIME, bc.StartTime) BETWEEN '00:00:00' AND '05:59:59')
        #         )
        #         """
        # elif choice == 'Total':
        #     time_condition = ""

        
        # self.cursor.execute(f'''
        #                 SELECT 
        #                 cm.ChargerMasterId,
        #                 cm.ChargerNumber,
        #                 cm.Status ,
        #                 cm.SerialNumber,
        #                 MAX(bc.ChargingDate) AS LastChargingDate,
        #                 COUNT(bc.BusInformationId) AS TotalBusesChargedToday,
        #                 SUM(bc.EnergyConsumption) AS TotalEnergyConsumedToday,
        #                 SUM(CAST(bc.SessionTime AS int)) / 60.00 AS TotalOperationalHoursToday,
        #                 (
        #                     SELECT COUNT(bc2.BusInformationId)
        #                     FROM MTN_BusCharging bc2
        #                     WHERE bc2.ChargerMasterId = cm.ChargerMasterId
        #                 ) AS TotalBusesChargedTillDate,
        #                 (
        #                     SELECT SUM(bc2.EnergyConsumption)
        #                     FROM MTN_BusCharging bc2
        #                     WHERE bc2.ChargerMasterId = cm.ChargerMasterId
        #                 ) AS TotalEnergyConsumedTillDate,
        #                 (
        #                     SELECT SUM(CAST(bc2.SessionTime AS int)) / 60.00
        #                     FROM MTN_BusCharging bc2
        #                     WHERE bc2.ChargerMasterId = cm.ChargerMasterId
        #                 ) AS TotalOperationalHoursTillDate
        #             FROM 
        #                 MTN_BusCharging bc
        #             JOIN 
        #                 MTN_ChargerMaster cm ON bc.ChargerMasterId = cm.ChargerMasterId
        #             WHERE 
        #                 bc.ChargingDate = '{date}' AND cm.CompanyId = '{self.company_id}'
        #                 {time_condition}
        #             GROUP BY 
        #                 cm.ChargerMasterId, 
        #                 cm.ChargerNumber, 
        #                 cm.Status ,
        #                 cm.SerialNumber
        #             ORDER BY 
        #                 cm.ChargerMasterId;

        #                     ''')
        
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

        # Define the query to get charger details
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
        # Execute the query
        
        query = self.cursor.fetchall()
        query_result = [{
            "ChargerNumber" : row.ChargerNumber , 
            'CPU_name' : 'Klick-Watt' , 
            'Charger_name'  : 'Shuzlon Energy' , 
            "Status" : row.Status,
            'Latest_data': {
                "date" : row.LastChargingDate ,
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
            WHERE CompanyId = '{self.company_id}';
        ''')
        return self.cursor.fetchone()[0]


    def get_charger_count(self):
        self.cursor.execute(f'''
                        SELECT COUNT(*) as ChargerCount
                        FROM MTN_ChargerMaster
                        WHERE CompanyId = '{self.company_id}';
                        ''')
        
        return self.cursor.fetchone()[0]
    

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