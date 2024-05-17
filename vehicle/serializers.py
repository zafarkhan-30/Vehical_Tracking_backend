from rest_framework import serializers
from database.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class deviceDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = devices
        fields = ["device_id" , "name" , "registrationNumber" , "deviceType" , "chassisNumber" , "trackingCode"]

class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = deviceStatus
        fields = ["active" , "status"  ]


class DeviceLocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = deviceLocation
        # fields = "__all__"
        # exclude = ["transactionId" , "id" , ]
        fields = ["gpsTime" , "gprsTime" , "latitude" , "longitude" , "altitude" , "heading" ,  "speedKph" ,"address",
                   "odometer" , "gpsSignal" , "created_at"]
        geo_field='location'
        
class CanInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = canInfo
        # fields = ["vehicleBattery" , "stateOfCharge" , "AMinCellVolt" , "AMinCellVolt" "APackVoltageValue" ,] 
        exclude = ["id" , "transactionId" , "created_at" , "device" , "AMinCellVolt" ,
                   "BMaxCellVolt" , "AMaxCellVolt" , "BMinCellVolt"]
        

class AlertsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = alerts
        exclude = [  "transactionId" , "created_at" , "device"]
        geo_field= 'location'


class TodaysDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = todaysDrive
        exclude = ["id" , "transactionId" , "created_at" , "device"]


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = links
        exclude = ["id" , "transactionId" , "created_at" , "device"]


class DinputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = dinputs
        exclude = ["id" , "transactionId"  , "device"]
