import requests
import psycopg2
import csv
from datetime import datetime, timedelta
import os
from django.conf import settings



def run_device_details_view():
    url = "https://timscan.transvolt.in/api/vehical/post-Master-Device-Data/"
    headers = {"Content-Type": "application/json"}
    log_file = "/tmp/cron_job_output.log"

    try:
        response = requests.get(url, headers=headers , verify=False)
        with open(log_file, "a") as f:
            if response.status_code == 200:
                f.write("Device details successfully updated.\n")
            else:
                f.write(f"Failed to update device details. Status code: {response.status_code}\n")
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"An error occurred: {str(e)}\n")


SOURCE_DB_CONFIG = {
            'dbname': settings.DATABASES['default']['NAME'],
            'user': settings.DATABASES['default']['USER'],
            'password': settings.DATABASES['default']['PASSWORD'],
            'host': settings.DATABASES['default']['HOST'],
            'port': settings.DATABASES['default']['PORT'],
        }

TARGET_DB_CONFIG = {
    'dbname': settings.BACKUP_DATABASE_NAME,
    'user': settings.BACKUP_DATABASE_USER,
    'password': settings.BACKUP_DATABASE_PASSWORD,
    'host': settings.BACKUP_DATABASE_HOST,
    'port': settings.BACKUP_DATABASE_PORT,

}


# DEVICE_DETAIL_TMP_FILE = os.path.join(settings.MEDIA_ROOT, 'backup', 'DEVICE_DETAIL_data.csv')
# MASTER_DEVICE_DETAIL_TMP_FILE = os.path.join(settings.MEDIA_ROOT, 'backup', 'MASTER_DEVICE_DETAIL_data.csv')
DEVICE_DETAIL_TMP_FILE = os.path.join('/home/ubuntu/Vehical_Tracking_backend/media/', 'backup/', 'DEVICE_DETAIL_data.csv')
MASTER_DEVICE_DETAIL_TMP_FILE = os.path.join('/home/ubuntu/Vehical_Tracking_backend/media/', 'backup/', 'MASTER_DEVICE_DETAIL_data.csv')


# Ensure the directory exists
os.makedirs(os.path.dirname(DEVICE_DETAIL_TMP_FILE), exist_ok=True)
os.makedirs(os.path.dirname(MASTER_DEVICE_DETAIL_TMP_FILE), exist_ok=True)

def fetch_old_data_and_backup():
    conn = psycopg2.connect(**SOURCE_DB_CONFIG)
    cursor = conn.cursor()
    
    device_table_query = """
    COPY (SELECT * FROM public.database_devices)
    TO STDOUT WITH CSV HEADER
    """

    # >= '2024-06-12 00:00:00' AND created_at < '2024-06-13 00:00:00';
    # < NOW() - INTERVAL '21 days'

    masterdevicedetails_table_query = """
    COPY (SELECT * FROM public.database_masterdevicedetails
        WHERE created_at < NOW() - INTERVAL '2 days'
    )
    TO STDOUT WITH CSV HEADER
    """

    with open(DEVICE_DETAIL_TMP_FILE, 'w', newline='') as f:
        cursor.copy_expert(device_table_query, f)
    
    with open(MASTER_DEVICE_DETAIL_TMP_FILE, 'w', newline='') as f:
        cursor.copy_expert(masterdevicedetails_table_query, f)
    
    cursor.close()
    conn.close()


def create_device_table():
    conn = psycopg2.connect(**TARGET_DB_CONFIG)
    cursor = conn.cursor()

    # Create the main table
    create_device_table_query = """
    CREATE TABLE IF NOT EXISTS public.backup_devices (
        id SERIAL PRIMARY KEY,
        device_id INTEGER UNIQUE,
        name TEXT,
        registrationNumber TEXT,
        deviceType TEXT,
        chassisNumber TEXT,
        trackingCode INTEGER,
        created_at TIMESTAMP,
        status BOOLEAN
    )
    """
    
    cursor.execute(create_device_table_query)
    conn.commit()

    # Create a temporary table to load CSV data
    create_temp_table_query = """
    CREATE TEMP TABLE temp_backup_devices (
        id SERIAL PRIMARY KEY,
        device_id INTEGER UNIQUE,
        name TEXT,
        registrationNumber TEXT,
        deviceType TEXT,
        chassisNumber TEXT,
        trackingCode INTEGER,
        created_at TIMESTAMP,
        status BOOLEAN
    )
    """
    cursor.execute(create_temp_table_query)
    conn.commit()

    # Load data into temporary table
    with open(DEVICE_DETAIL_TMP_FILE, 'r') as f:
        cursor.copy_expert("""
        COPY temp_backup_devices FROM STDIN WITH CSV HEADER
        """, f)

    conn.commit()

    # Perform the UPSERT operation into the main table
    upsert_query = """
    INSERT INTO public.backup_devices (id, device_id, name, registrationNumber, deviceType, chassisNumber, trackingCode, created_at, status)
    SELECT id, device_id, name, registrationNumber, deviceType, chassisNumber, trackingCode, created_at, status
    FROM temp_backup_devices
    ON CONFLICT (id) DO NOTHING
    """
    cursor.execute(upsert_query)
    conn.commit()

    cursor.close()
    conn.close()


def insert_backup_data():
    conn = psycopg2.connect(**TARGET_DB_CONFIG)
    cursor = conn.cursor()
    
    create_master_device_table_query = """
    CREATE TABLE IF NOT EXISTS public.backup_masterdevicedetails (
    id SERIAL PRIMARY KEY,
    active BOOLEAN,
    status TEXT,
    gpsTime TIMESTAMP,
    gprsTime TIMESTAMP,
    device_location GEOMETRY(Point, 4326),
    altitude FLOAT,
    heading FLOAT,
    speedKph FLOAT,
    address TEXT,
    odometer FLOAT,
    gpsSignal INTEGER,
    vehicleBattery FLOAT,
    stateOfCharge FLOAT,
    AMinCellVolt FLOAT,
    APackVoltageValue FLOAT,
    APackCurrentValue FLOAT,
    batteryTemperature FLOAT,
    ASOCValue FLOAT,
    BFaultRank INTEGER,
    totalRegenerationEnergy FLOAT,
    BPackCurrentValue FLOAT,
    BMaxCellVolt FLOAT,
    ChargerGunDetected2 BOOLEAN,
    AMaxCellVolt FLOAT,
    BMinCellVolt FLOAT,
    BPackVoltageValue FLOAT,
    AFaultRank INTEGER,
    BSOCValue FLOAT,
    distanceToEmpty FLOAT,
    timestamp INTEGER,
    alert_location GEOMETRY(Point, 4326),
    alert_address TEXT,
    alarmType TEXT,
    limits INTEGER,
    severity INTEGER,
    todayKms FLOAT,
    todayMovementTime INTERVAL,
    todayIdleTime INTERVAL,
    todayDriveCount INTEGER,
    embedUrl TEXT,
    input_1 BOOLEAN,
    input_2 BOOLEAN,
    input_3 BOOLEAN,
    input_4 BOOLEAN,
    input_5 BOOLEAN,
    input_6 BOOLEAN,
    input_7 BOOLEAN,
    created_at TIMESTAMP,
    device_id INTEGER REFERENCES public.backup_devices(id)
    )
    """

    create_staging_master_device_table_query = """
    CREATE TEMP TABLE staging_masterdevicedetails (
        id SERIAL PRIMARY KEY,
        active BOOLEAN,
        status TEXT,
        gpsTime TIMESTAMP,
        gprsTime TIMESTAMP,
        device_location GEOMETRY(Point, 4326),
        altitude FLOAT,
        heading FLOAT,
        speedKph FLOAT,
        address TEXT,
        odometer FLOAT,
        gpsSignal INTEGER,
        vehicleBattery FLOAT,
        stateOfCharge FLOAT,
        AMinCellVolt FLOAT,
        APackVoltageValue FLOAT,
        APackCurrentValue FLOAT,
        batteryTemperature FLOAT,
        ASOCValue FLOAT,
        BFaultRank INTEGER,
        totalRegenerationEnergy FLOAT,
        BPackCurrentValue FLOAT,
        BMaxCellVolt FLOAT,
        ChargerGunDetected2 BOOLEAN,
        AMaxCellVolt FLOAT,
        BMinCellVolt FLOAT,
        BPackVoltageValue FLOAT,
        AFaultRank INTEGER,
        BSOCValue FLOAT,
        distanceToEmpty FLOAT,
        timestamp INTEGER,
        alert_location GEOMETRY(Point, 4326),
        alert_address TEXT,
        alarmType TEXT,
        limits INTEGER,
        severity INTEGER,
        todayKms FLOAT,
        todayMovementTime INTERVAL,
        todayIdleTime INTERVAL,
        todayDriveCount INTEGER,
        embedUrl TEXT,
        input_1 BOOLEAN,
        input_2 BOOLEAN,
        input_3 BOOLEAN,
        input_4 BOOLEAN,
        input_5 BOOLEAN,
        input_6 BOOLEAN,
        input_7 BOOLEAN,
        created_at TIMESTAMP,
        device_id INTEGER
    )
    """

    

    cursor.execute(create_master_device_table_query)
    cursor.execute(create_staging_master_device_table_query)
  

    with open(MASTER_DEVICE_DETAIL_TMP_FILE, 'r') as f:
        cursor.copy_expert("COPY staging_masterdevicedetails FROM STDIN WITH CSV HEADER", f)
    
    conn.commit()
    
    insert_master_device_query = """
    INSERT INTO public.backup_masterdevicedetails (
        active, status, gpsTime, gprsTime, device_location, altitude, heading,
        speedKph, address, odometer, gpsSignal, vehicleBattery, stateOfCharge,
        AMinCellVolt, APackVoltageValue, APackCurrentValue, batteryTemperature,
        ASOCValue, BFaultRank, totalRegenerationEnergy, BPackCurrentValue, BMaxCellVolt,
        ChargerGunDetected2, AMaxCellVolt, BMinCellVolt, BPackVoltageValue, AFaultRank,
        BSOCValue, distanceToEmpty, timestamp, alert_location, alert_address, alarmType,
        limits, severity, todayKms, todayMovementTime, todayIdleTime, todayDriveCount,
        embedUrl, input_1, input_2, input_3, input_4, input_5, input_6, input_7,
        created_at, device_id
    )
    SELECT
        active, status, gpsTime, gprsTime, device_location, altitude, heading,
        speedKph, address, odometer, gpsSignal, vehicleBattery, stateOfCharge,
        AMinCellVolt, APackVoltageValue, APackCurrentValue, batteryTemperature,
        ASOCValue, BFaultRank, totalRegenerationEnergy, BPackCurrentValue, BMaxCellVolt,
        ChargerGunDetected2, AMaxCellVolt, BMinCellVolt, BPackVoltageValue, AFaultRank,
        BSOCValue, distanceToEmpty, timestamp, alert_location, alert_address, alarmType,
        limits, severity, todayKms, todayMovementTime, todayIdleTime, todayDriveCount,
        embedUrl, input_1, input_2, input_3, input_4, input_5, input_6, input_7,
        created_at, device_id
    FROM
        staging_masterdevicedetails
    ON CONFLICT (id) DO NOTHING
    """
    
    cursor.execute(insert_master_device_query)
    conn.commit()
    cursor.close()
    conn.close()
    
def delete_old_data():
    conn = psycopg2.connect(**SOURCE_DB_CONFIG)
    cursor = conn.cursor()
    
    delete_query = """
    DELETE FROM public.database_masterdevicedetails
    WHERE created_at < NOW() - INTERVAL '2 days'
    """
    
    cursor.execute(delete_query)
    conn.commit()
    
    cursor.close()
    conn.close()


# backup_log_file = "/tmp/cron_job_output.log"
def Perform_backup():
    try:
        # 1 > fetched old data and crate a Backup excel file and one staging table in database
        fetch_old_data_and_backup()

        create_device_table()
        insert_backup_data()
        delete_old_data()

        # Remove the temporary file
        os.remove(DEVICE_DETAIL_TMP_FILE)
        os.remove(MASTER_DEVICE_DETAIL_TMP_FILE)
    except Exception as e:
        # with open(log_file, "a") as f:
        #     f.write(f"An error occurred: {str(e)}\n")

        print(f"An error occurred: {str(e)}")