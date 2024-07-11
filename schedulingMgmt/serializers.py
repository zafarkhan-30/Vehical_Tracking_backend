from rest_framework import serializers
from database.models import *


class GetTotalTripCountSerilizsers(serializers.Serializer):
    vehicalNumber = serializers.CharField(max_length=100 , required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)

class GetTotalDistanceSerilizsers(serializers.Serializer):
    vehicalNumber = serializers.CharField(max_length=100 , required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)


class LiveDeviceSeailizer(serializers.ModelSerializer):
    class Meta:
        model = MasterDeviceDetails
        fields = ('odometer' , 'stateOfCharge' , 'todayKms' )


class LivedeviceDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = devices
        fields = ["name" , "registrationNumber" , "deviceType" , "chassisNumber"]