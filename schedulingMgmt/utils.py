
from .db_connection import DatabaseConnection
from database.models import MasterDeviceDetails
from .serializers import *
from datetime import date
import random
from rest_framework.response import Response
import pyodbc
from django.db.models import Sum
import math
from VehicalTracking.settings import ITMS_SERVER, ITMS_DRIVER, ITMS_PASSWORD, ITMS_USERNAME, ITMS_DATABASE_NAME
# from .db_connection import DatabaseConnection


db_config = {
    'server': ITMS_SERVER,
    'database': ITMS_DATABASE_NAME,
    'username': ITMS_USERNAME,
    'password': ITMS_PASSWORD,
    'driver': ITMS_DRIVER
}


db_connection = DatabaseConnection(**db_config)


class ITMS:

    def __init__(self, db_config, user_group):
        self.db_connection = DatabaseConnection(**db_config)
        self.company_id = self.get_company_id(user_group)

    def custom_round_up(self, n):
        return math.ceil(n)

    def get_company_id(self, user_group):
        if user_group == 'MBMT':
            return 1
        elif user_group == 'Uber':
            return 2
        return None

    def get_route_list(self, date=None, route_number='', page=None, page_size=None):
        date = date or datetime.date.today()
        pagination = f"""OFFSET {(int(page) - 1) * int(page_size)} ROWS FETCH NEXT {page_size} ROWS ONLY""" \
            if page and page_size else ""

        filter = f"""
                 AND r.CompanyId = '{self.company_id}' 
                 {f"AND r.Code LIKE '%{route_number}%' " if route_number else ''}
        
             """
        self.db_connection.connect()
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()

        try:
            # Count query
            count_query = cursor.execute(f'''
                SELECT 
                    COUNT(DISTINCT (r.Code))
                FROM 
                    OPR_Scheduling os
                JOIN 
                    OPR_SchedulingDetails osd ON os.SchedulingId = osd.SchedulingId
                JOIN 
                    OPR_Schedule o ON osd.ScheduleId = o.ScheduleId
                JOIN 
                    OPR_Route r ON o.RouteId = r.RouteId
                WHERE 
                    os.SchedulingDate = '{date}' {filter}
            ''').fetchone()[0]

            # Main query
            query = cursor.execute(f'''
                SELECT 
                    r.RouteId AS RouteId,
                    r.Name AS Name,
                    r.Code AS Code,
                    os.SchedulingDate AS Date, 
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
                    os.SchedulingDate = '{date}' {filter}
                GROUP BY 
                    r.RouteId,
                    r.Name,
                    r.Code,
                    os.SchedulingDate 
                ORDER BY 
                    r.RouteId
                {pagination}
            ''').fetchall()

            result = [{'route_id': row.RouteId, 'Name': row.Name,
                       'Code': row.Code,
                       'date': row.Date,
                       'NumberOfBuses': row.NumberOfBuses,
                       'NumberOfSchedules': row.NumberOfScheduleCodes,
                       'TotalTrip': row.TotalTrip,
                       'route_length': random.randint(50, 80)}  # Replace this with actual route length data
                      for row in query]

        finally:

            cursor.close()
            self.db_connection.close_connection()

        return result, count_query

    def get_buses_detail_list(self, date=None, vehicle_number='', page=None, page_size=None):
        date = date or datetime.date.today()  # Use today's date if no date is provided

        pagination = f"""OFFSET {(int(page) - 1) * int(page_size)} ROWS FETCH NEXT {page_size} ROWS ONLY""" \
            if page and page_size else ""

        # filter based on vehicle_number
        filter = f"""
            mtn.CompanyId = '{self.company_id}'
            {f"AND mtn.VehicleNumber LIKE '%{vehicle_number}%'" if vehicle_number else ''}
        """
        self.db_connection.connect()
        connection = self.db_connection.get_connection()
        # print(connection , "connection")
        cursor = connection.cursor()

        try:
            count_query = cursor.execute(f'''
                    SELECT 
                    COUNT(DISTINCT (mtn.BusInformationId))
                    FROM 
                        MTN_BusInformation mtn
                    LEFT JOIN 
                        (
                            SELECT 
                                osd.BusInformationId,
                                osd.SchedulingId,
                                osd.StartODO,
                                osd.EndODO,
                                os.SchedulingDate,
                                osd.ScheduleId  -- Include ScheduleId in subquery
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
                    WHERE {filter}
                ''').fetchone()[0]

            # total_count = count_query.fetchone()[0]
            query = cursor.execute(f'''
                            SELECT 
                            mtn.BusInformationId,
                            mtn.BusCode,
                            mtn.VehicleNumber,
                            MAX(osd.SchedulingDate) AS LatestSchedulingDate,
                            COALESCE(MAX(osd.EndODO) - MIN(osd.StartODO), 0) AS TotalKmRunToday,
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
                                ELSE 0 
                            END) / 100.0 AS ChargingCycles,
                            STUFF((
                                SELECT ', ' + o2.Code
                                FROM OPR_Schedule o2
                                JOIN OPR_SchedulingDetails osd2 ON o2.ScheduleId = osd2.ScheduleId
                                JOIN OPR_Scheduling os2 ON osd2.SchedulingId = os2.SchedulingId
                                WHERE osd2.BusInformationId = mtn.BusInformationId
                                AND os2.SchedulingDate = '{date}'
                                AND o2.Shift = 'Morning'
                                FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS MorningScheduleCodes,
                            STUFF((
                                SELECT ', ' + o2.Code
                                FROM OPR_Schedule o2
                                JOIN OPR_SchedulingDetails osd2 ON o2.ScheduleId = osd2.ScheduleId
                                JOIN OPR_Scheduling os2 ON osd2.SchedulingId = os2.SchedulingId
                                WHERE osd2.BusInformationId = mtn.BusInformationId
                                AND os2.SchedulingDate = '{date}'
                                AND o2.Shift = 'Evening'
                                FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS EveningScheduleCodes
                        FROM 
                            MTN_BusInformation mtn
                        LEFT JOIN 
                            (
                                SELECT 
                                    osd.BusInformationId,
                                    osd.SchedulingId,
                                    osd.StartODO,
                                    osd.EndODO,
                                    os.SchedulingDate,
                                    osd.ScheduleId  -- Include ScheduleId in subquery
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
                            {filter}
                        GROUP BY 
                            mtn.BusInformationId,
                            mtn.BusCode,
                            mtn.VehicleNumber,
                            lastOdo.EndODO
                        ORDER BY 
                            mtn.BusInformationId
                        {pagination}
                        
                        ''').fetchall()
            
            

            # result = query.fetchall()

            query_result = [{'VehicleNumber': row.VehicleNumber,
                             'BusInformationId': row.BusInformationId,
                             'BusCode': row.BusCode,
                             'Status': row.Status,
                             'MorningScheduleCodes': row.MorningScheduleCodes,
                             'EveningScheduleCodes': row.EveningScheduleCodes,
                             'TotalKmRunDay': round(row.TotalKmRunToday),
                             "Charging_cycle": round(row.ChargingCycles),
                             'totalEnergyDay_KwH': round(row.TodayEnergyConsumption),
                             'TotalEnergyConsumed_kwH': round(row.TotalEnergyConsumed),
                             'TotalKm': round(row.LastODO),
                             'total_Today_RegenerationEnergy': 0
                            #  MasterDeviceDetails.objects.filter(device__registrationNumber=row.VehicleNumber,
                            #  created_at__date=date).aggregate(total_energy=Sum('totalRegenerationEnergy'))['total_energy']
                             } 
                             for row in query]
        finally:
            # Close cursor and connection
            cursor.close()
            # print("cursor close")
            self.db_connection.close_connection()
            # print("connection close")

        return query_result, count_query

    def get_charger_detail_list(self, choice, date=None, charger_number='', page=None, page_size=None):

        date = date or datetime.date.today()
        pagination = f"""OFFSET {(int(page) - 1) * int(page_size)} ROWS FETCH NEXT {page_size} ROWS ONLY""" \
            if page and page_size else ""

        filter = f"""
             cm.CompanyId = '{self.company_id}'
            {f"AND cm.ChargerNumber LIKE '%{charger_number}%'" if charger_number else ''}
        """

        count_filter = f"""
             cm.CompanyId = '{self.company_id}'
            {f"AND ChargerNumber LIKE '%{charger_number}%'" if charger_number else ''}
        """

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

        count_filter = f"""
                CompanyId = '{self.company_id}' AND ChargerNumber LIKE '%{charger_number}%'

                """

        self.db_connection.connect()
        connection = self.db_connection.get_connection()
        # print(connection , "connection")
        cursor = connection.cursor()

        try:
            count_query = cursor.execute(f"""SELECT 
                COUNT(DISTINCT(ChargerMasterId)) AS totalcount
                FROM 
                    MTN_ChargerMaster 
            
                WHERE {count_filter}
                    """)
            total_count = count_query.fetchone()
            # #print(total_count)

            query = cursor.execute(f'''
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
                    {filter}
                GROUP BY 
                    cm.ChargerMasterId, 
                    cm.ChargerNumber, 
                    cm.Status,
                    cm.SerialNumber
                ORDER BY 
                    cm.ChargerMasterId
                {pagination}
                
            ''')

            query = query.fetchall()

            query_result = [{
                "ChargerNumber": row.ChargerNumber,
                "id": row.ChargerMasterId,
                'CPO_name': 'Klick-Watt',
                'Charger_name': 'Star Charge',
                "Status": row.Status,
                'Latest_data': {
                    # "date" : row.LastChargingDate ,
                    'BusesCharged': row.TotalBusesChargedToday,
                    'EnergyConsumed': round(row.TotalEnergyConsumedToday),
                    'OperationalHours': row.TotalOperationalHoursToday
                },
                'Total': {
                    'BusesCharged': row.TotalBusesChargedTillDate,
                    'EnergyConsumed': (row.TotalEnergyConsumedTillDate),
                    'OperationalHours': (row.TotalOperationalHoursTillDate)
                },
            } for row in query]

        finally:
            # Close cursor and connection
            cursor.close()
            # print("cursor close")
            self.db_connection.close_connection()
            # print("connection close")
        return query_result, total_count[0]

    def get_charger_Details(self, choice, date, charger_id):
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
            "ChargerNumber": row.ChargerNumber,
            "id": row.ChargerMasterId,
            'CPU_name': 'Klick-Watt',
            'Charger_name': 'Shuzlon Energy',
            "Status": row.Status,
            'Latest_data': {
                # "date" : row.LastChargingDate ,
                'BusesCharged': row.TotalBusesChargedToday,
                'EnergyConsumed': round(row.TotalEnergyConsumedToday),
                'OperationalHours': row.TotalOperationalHoursToday
            },
            'Total': {
                'BusesCharged': row.TotalBusesChargedTillDate,
                'EnergyConsumed': round(row.TotalEnergyConsumedTillDate),
                'OperationalHours': round(row.TotalOperationalHoursTillDate)
            }
        } for row in query]
        return query_result

    def Get_Schedule_Buses_List(self, scheduling_date=None, route_id=None):
        self.cursor.execute(f'''
                        SELECT o.RouteId as RouteId, osd.BusInformationId as BusInformationId , 
                        os.SchedulingDate as SchedulingDate , osd.BusCode as BusCode , o.Code as ScheduleCode
                        FROM OPR_Scheduling os
                        JOIN OPR_SchedulingDetails osd ON os.SchedulingId = osd.SchedulingId
                        JOIN OPR_Schedule o ON osd.ScheduleId = o.ScheduleId
                        WHERE os.SchedulingDate = '{scheduling_date}'  AND o.RouteId = {route_id} ;
                        ''')

        result = self.cursor.fetchall()
        buses_list = [{'RouteId': row.RouteId, 'BusInformationId': row.BusInformationId,
                       'BusCode': row.BusCode, 'ScheduleCode': row.ScheduleCode} for row in result]

        return buses_list


# dashboard API Functions

    def _execute_query(self, query, params=None):
        # try:
        self.db_connection.connect()
        connection = self.db_connection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        result = cursor.fetchone()
        return result[0] if result else None

        # finally:
        #     if cursor:
        #         cursor.close()
        #     self.db_connection.close_connection()

    def get_route_count(self):
        query = "SELECT COUNT(DISTINCT Code) FROM OPR_Route WHERE CompanyId = ?"
        return self._execute_query(query, (self.company_id,))

    def get_buses_count(self):
        query = "SELECT COUNT(*) FROM MTN_BusInformation WHERE CompanyId = ?"
        return self._execute_query(query, (self.company_id,))

    def get_Operational_hours(self):
        query = """
        SELECT SUM(
            CASE 
                WHEN TRY_CAST(StartTime AS TIME) IS NOT NULL AND TRY_CAST(EndTime AS TIME) IS NOT NULL 
                THEN 
                    CASE 
                        WHEN TRY_CAST(EndTime AS TIME) < TRY_CAST(StartTime AS TIME) 
                        THEN DATEDIFF(MINUTE, CAST(TRY_CAST(StartTime AS TIME) AS DATETIME), DATEADD(DAY, 1, CAST(TRY_CAST(EndTime AS TIME) AS DATETIME)))
                        ELSE DATEDIFF(MINUTE, CAST(TRY_CAST(StartTime AS TIME) AS DATETIME), CAST(TRY_CAST(EndTime AS TIME) AS DATETIME))
                    END
                ELSE NULL
            END
        ) / 60.00 FROM OPR_SchedulingDetailsTrip
        """
        return round(self._execute_query(query))

    def get_charger_count(self):
        query = "SELECT COUNT(*) FROM MTN_ChargerMaster WHERE CompanyId = ?"
        return self._execute_query(query, (self.company_id,))

    def get_charging_hours(self):
        query = "SELECT SUM(CAST(SessionTime AS int)) / 60.00 FROM MTN_BusCharging"
        return round(self._execute_query(query))

    def get_trip_count(self, vehicle_number=None, start_date=None, end_date=None):
        query = """
        SELECT COUNT(OPR_SchedulingDetailsTrip.SchedulingDetailsTripId)
        FROM MTN_BusInformation
        INNER JOIN OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId
        INNER JOIN OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId
        INNER JOIN OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
        WHERE OPR_SchedulingDetailsTrip.IsLost = 0 AND MTN_BusInformation.CompanyId = ?
        """
        params = [self.company_id]
        if vehicle_number and start_date and end_date:
            query += " AND MTN_BusInformation.VehicleNumber = ? AND OPR_Scheduling.SchedulingDate BETWEEN ? AND ?"
            params.extend([vehicle_number, start_date, end_date])
        return self._execute_query(query, params)

    def get_distance_km(self, vehicle_number=None, start_date=None, end_date=None):
        query = """
        SELECT SUM(OPR_SchedulingDetailsTrip.DistanceInKM)
        FROM MTN_BusInformation
        INNER JOIN OPR_SchedulingDetails ON MTN_BusInformation.BusInformationId = OPR_SchedulingDetails.BusInformationId
        INNER JOIN OPR_SchedulingDetailsTrip ON OPR_SchedulingDetails.SchedulingDetailsId = OPR_SchedulingDetailsTrip.SchedulingDetailsId
        INNER JOIN OPR_Scheduling ON OPR_SchedulingDetails.SchedulingId = OPR_Scheduling.SchedulingId
        WHERE OPR_SchedulingDetailsTrip.IsLost = 0 AND MTN_BusInformation.CompanyId = ?
        """
        params = [self.company_id]
        if vehicle_number and start_date and end_date:
            query += " AND MTN_BusInformation.VehicleNumber = ? AND OPR_Scheduling.SchedulingDate BETWEEN ? AND ?"
            params.extend([vehicle_number, start_date, end_date])
        return round(self._execute_query(query, params) or 0)


class Vehicletracking:
    def get_live_bus_details(all_devices):
        data_list = []
        if all_devices:
            today = date.today()
            for device in all_devices:
                device_details = LivedeviceDetailsSerialiser(device).data
                try:
                    instance = MasterDeviceDetails.objects.filter(
                        device_id=device, created_at__date=today).latest("created_at")
                    device_data = LiveDeviceSeailizer(instance).data
                    device_details.update(device_data)
                except MasterDeviceDetails.DoesNotExist:
                    continue
                data_list.append(device_details)

        return data_list
