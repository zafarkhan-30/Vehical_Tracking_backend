from database.models import *
import datetime
from django.contrib.gis.geos import Point,GEOSGeometry
def create_device_object(device_detail):
        if not devices.objects.filter(device_id = device_detail["id"]).exists():
            device_details = device_detail.get("deviceDetails", {})
            devices.objects.create(
                device_id=device_detail["id"],
                name=device_details.get("name"),
                registrationNumber=device_details.get("registrationNumber"),
                deviceType=device_details.get("deviceType"),
                chassisNumber=device_details.get("chassisNumber"),
                trackingCode=device_details.get("trackingCode")
            )

def create_device_status(device_id , device_status_data , transactionId ):
    device_instance = devices.objects.get(device_id=device_id)
    active = device_status_data.get("active")
    status = device_status_data.get("status")

    return deviceStatus(
        device = device_instance ,
        transactionId = transactionId ,
        active = active ,
        status = status
    )

def create_device_location(device_id, location_data , transactionId):
    
    device_instance = devices.objects.get(device_id=device_id)

    location_details = location_data.get("location", {})
    lat = float(location_details.get("latitude"))
    long = float(location_details.get("longitude"))
    location = Point(long, lat, srid=4326)
    

    return deviceLocation(
        device=device_instance,
        transactionId = transactionId ,
        gpsTime= datetime.datetime.fromtimestamp(location_details.get("gpsTime")),
        gprsTime= datetime.datetime.fromtimestamp(location_details.get("gprsTime")),
        location = location , 
        # latitude=location_details.get("latitude"),
        # longitude=location_details.get("longitude"),
        altitude=location_details.get("altitude"),
        heading=location_details.get("heading"),
        speedKph=location_details.get("speedKph"),
        address=location_details.get("address"),
        odometer=location_details.get("odometer"),
        gpsSignal=location_details.get("gpsSignal")
    )

def create_canInfo_object(device_id , can_info_data , transactionId):
    device_instance = devices.objects.get(device_id=device_id)
    canInfo_details = can_info_data.get("canInfo", {})
   
    return canInfo(
        device=device_instance,
        transactionId = transactionId ,
        vehicleBattery=can_info_data.get("vehicleBattery"),
        AMinCellVolt=canInfo_details.get("AMinCellVolt"),
        stateOfCharge=canInfo_details.get("stateOfCharge"),
        APackVoltageValue=canInfo_details.get("APackVoltageValue"),
        APackCurrentValue=canInfo_details.get("APackCurrentValue"),
        batteryTemperature=canInfo_details.get("batteryTemperature"),
        ASOCValue=canInfo_details.get("ASOCValue"),
        BFaultRank=canInfo_details.get("BFaultRank"),
        totalRegenerationEnergy=canInfo_details.get("totalRegenerationEnergy"),
        BPackCurrentValue=canInfo_details.get("BPackCurrentValue"),
        BMaxCellVolt=canInfo_details.get("BMaxCellVolt"),
        ChargerGunDetected2=canInfo_details.get("ChargerGunDetected2"),
        AMaxCellVolt=canInfo_details.get("AMaxCellVolt"),
        BMinCellVolt=canInfo_details.get("BMinCellVolt"),
        BPackVoltageValue=canInfo_details.get("BPackVoltageValue"),
        AFaultRank=canInfo_details.get("AFaultRank"),
        BSOCValue=canInfo_details.get("BSOCValue"),
        distanceToEmpty=canInfo_details.get("distanceToEmpty")
    )
     
def create_alerts_object(device_id , alerts_data , transactionId):
    device_instance = devices.objects.get(device_id=device_id)
    alerts_details = alerts_data.get("alerts", {})
    lat = float(alerts_details.get("latitude"))
    long = float(alerts_details.get("longitude"))
    location = Point(long, lat, srid=4326)
    # print(alerts_details)
    return alerts(
         device = device_instance ,
         transactionId = transactionId ,
         timestamp =alerts_details.get('timestamp'),
        #  latitude= alerts_details.get('latitude'),
        #  longitude=alerts_details.get('longitude'),
         location = location , 
         address=alerts_details.get('address'),
         alarmType =alerts_details.get('alarmType'),
         limit =alerts_details.get('limit'),
         severity =alerts_details.get('severity')

    )

def create_todaysDrive_object(device_id, todayDrive_data , transactionId):
    device_instance = devices.objects.get(device_id=device_id)
    todayDrive_details = todayDrive_data.get("todaysDrive", {})

    return todaysDrive(
         device = device_instance , 
         transactionId = transactionId ,
         todayKms =todayDrive_details.get("todayKms"),
         todayMovementTime =todayDrive_details.get("todayMovementTime"),
         todayIdleTime  =todayDrive_details.get("todayIdleTime"),
         todayDriveCount =todayDrive_details.get("todayDriveCount")
    )


def create_links_object(device_id , links_data , transactionId):
    device_instance = devices.objects.get(device_id=device_id)
    links_details = links_data.get("links", {})

    return links(
         device = device_instance ,
         transactionId = transactionId ,
         embedUrl = links_details.get("embedUrl")
    )
     
def create_dinputs_objects(device_id , dinputs_data , transactionId):
    device_instance = devices.objects.get(device_id=device_id)
    dinputs_details = dinputs_data.get("dinputs" , {})

    return dinputs(
         device = device_instance , 
         transactionId = transactionId ,
        input_1 = dinputs_details.get("1"),
        input_2= dinputs_details.get("2"),
        input_3 =dinputs_details.get("3"),
        input_4 =dinputs_details.get("4"),
        input_5 =dinputs_details.get("5"),
        input_6 =dinputs_details.get("6"),
        input_7 =dinputs_details.get("7"),

    )


def create_master_device_details(device_id , data):
    
    device_instance = devices.objects.get(device_id=device_id)
    active = data.get("active")
    status = data.get("status")

    location_details = data.get("location", {})
    lat = float(location_details.get("latitude"))
    long = float(location_details.get("longitude"))
    device_location = Point(long, lat, srid=4326)

    canInfo_details = data.get("canInfo", {})

    alerts_details = data.get("alerts", {})
    try:
        lat = float(alerts_details.get("latitude"))
        long = float(alerts_details.get("longitude"))
    except:
        lat =  0
        long = 0
    alert_location = Point(long, lat, srid=4326)

    todayDrive_details = data.get("todaysDrive", {})
    links_details = data.get("links", {})
    dinputs_details = data.get("dinputs" , {})

    return MasterDeviceDetails(
        device = device_instance,
        active = active ,
        status = status,

        gpsTime= datetime.datetime.fromtimestamp(location_details.get("gpsTime")),
        gprsTime= datetime.datetime.fromtimestamp(location_details.get("gprsTime")),
        device_location = device_location , 
   
        altitude=location_details.get("altitude"),
        heading=location_details.get("heading"),
        speedKph=location_details.get("speedKph"),
        address=location_details.get("address"),
        odometer=location_details.get("odometer"),
        gpsSignal=location_details.get("gpsSignal"),

        vehicleBattery=data.get("vehicleBattery"),
        AMinCellVolt=canInfo_details.get("AMinCellVolt"),
        stateOfCharge=canInfo_details.get("stateOfCharge"),
        APackVoltageValue=canInfo_details.get("APackVoltageValue"),
        APackCurrentValue=canInfo_details.get("APackCurrentValue"),
        batteryTemperature=canInfo_details.get("batteryTemperature"),
        ASOCValue=canInfo_details.get("ASOCValue"),
        BFaultRank=canInfo_details.get("BFaultRank"),
        totalRegenerationEnergy=canInfo_details.get("totalRegenerationEnergy"),
        BPackCurrentValue=canInfo_details.get("BPackCurrentValue"),
        BMaxCellVolt=canInfo_details.get("BMaxCellVolt"),
        ChargerGunDetected2=canInfo_details.get("ChargerGunDetected2"),
        AMaxCellVolt=canInfo_details.get("AMaxCellVolt"),
        BMinCellVolt=canInfo_details.get("BMinCellVolt"),
        BPackVoltageValue=canInfo_details.get("BPackVoltageValue"),
        AFaultRank=canInfo_details.get("AFaultRank"),
        BSOCValue=canInfo_details.get("BSOCValue"),
        distanceToEmpty=canInfo_details.get("distanceToEmpty"),


        timestamp =alerts_details.get('timestamp'),
        alert_location = alert_location , 
        alert_address=alerts_details.get('address'),
        alarmType =alerts_details.get('alarmType'),
        limit =alerts_details.get('limit'),
        severity =alerts_details.get('severity'),

        todayKms =todayDrive_details.get("todayKms"),
        todayMovementTime =todayDrive_details.get("todayMovementTime"),
        todayIdleTime  =todayDrive_details.get("todayIdleTime"),
        todayDriveCount =todayDrive_details.get("todayDriveCount"),

        embedUrl = links_details.get("embedUrl"),

        input_1 =dinputs_details.get("1"),
        input_2= dinputs_details.get("2"),
        input_3 =dinputs_details.get("3"),
        input_4 =dinputs_details.get("4"),
        input_5 =dinputs_details.get("5"),
        input_6 =dinputs_details.get("6"),
        input_7 =dinputs_details.get("7"),




    )

