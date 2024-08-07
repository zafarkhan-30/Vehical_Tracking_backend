from database.models import *
import datetime
from django.contrib.gis.geos import Point
from typing import Dict, Any

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


def parse_timestamp(timestamp: Any):
    try:
        return datetime.datetime.fromtimestamp(timestamp) if timestamp else None
    except (ValueError, TypeError):
        return None

def parse_float(value: Any):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def create_master_device_details(device_instances: int, data: Dict[str, Any]):
    active = data.get("active")
    status = data.get("status")

    location_details = data.get("location", {})
    gps_time = parse_timestamp(location_details.get("gpsTime"))
    gprs_time = parse_timestamp(location_details.get("gprsTime"))

    device_lat = parse_float(location_details.get("latitude"))
    device_long = parse_float(location_details.get("longitude"))
    device_location = Point(device_long, device_lat, srid=4326)

    canInfo_details = data.get("canInfo", {})
    alerts_details = data.get("alerts", {})
    alert_lat = parse_float(alerts_details.get("latitude"))
    alert_long = parse_float(alerts_details.get("longitude"))
    alert_location = Point(alert_long, alert_lat, srid=4326)

    todayDrive_details = data.get("todaysDrive", {})
    links_details = data.get("links", {})
    dinputs_details = data.get("dinputs", {})

    return MasterDeviceDetails(
        device=device_instances,
        active=active,
        status=status,
        gpsTime=gps_time,
        gprsTime=gprs_time,
        device_location=device_location,
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
        timestamp=alerts_details.get('timestamp'),
        alert_location=alert_location,
        alert_address=alerts_details.get('address'),
        alarmType=alerts_details.get('alarmType'),
        limits=alerts_details.get('limit'),
        severity=alerts_details.get('severity'),
        todayKms=todayDrive_details.get("todayKms"),
        todayMovementTime=todayDrive_details.get("todayMovementTime"),
        todayIdleTime=todayDrive_details.get("todayIdleTime"),
        todayDriveCount=todayDrive_details.get("todayDriveCount"),
        embedUrl=links_details.get("embedUrl"),
        input_1=dinputs_details.get("1"),
        input_2=dinputs_details.get("2"),
        input_3=dinputs_details.get("3"),
        input_4=dinputs_details.get("4"),
        input_5=dinputs_details.get("5"),
        input_6=dinputs_details.get("6"),
        input_7=dinputs_details.get("7"),
    )

