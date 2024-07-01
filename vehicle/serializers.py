from rest_framework import serializers
from database.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



def get_group_choice():
	"""
	The function "get_group_choice" returns all the available group names in the database as a tuple of
	tuples.
	:return: a tuple of tuples, where each inner tuple contains a group name as both the key and the
	value.
	"""
	group_names = list(Group.objects.values_list("name",flat=True))
	return tuple((i,i) for i in group_names)



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type':'password'},write_only = True)
    confirm_password = serializers.CharField(style = {'input_type':'password'},write_only = True)
    groups = serializers.ChoiceField(choices = get_group_choice(),required = True)
    class Meta:
        model = User
        fields = ('username','password' , 'confirm_password' , 'groups')

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if username == "" or username == None:
            raise serializers.ValidationError('email can not be empty')
        if not password == confirm_password:
            raise serializers.ValidationError('Password and confirm password must be same')
             
        return data
    
    def create(self,validated_data):
        validated_data.pop("confirm_password")
        validated_data.pop("groups")
        return User.objects.create_user(**validated_data)
    


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
		# model = CustomUser
        fields = ('username','password')




class logoutSerializer(serializers.Serializer):
    token = serializers.CharField(max_length = 255 , required =True)

class deviceDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = devices
        fields = ["device_id" , "name" , "registrationNumber" , "deviceType" , "chassisNumber" , "trackingCode"]

class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = deviceStatus
        fields = ["active" , "status"  ]


class DeviceLocationSerializer(GeoFeatureModelSerializer):
    device_name = serializers.SerializerMethodField()
    registrationNumber = serializers.SerializerMethodField()
    trackingCode = serializers.SerializerMethodField()
    stateOfCharge = serializers.SerializerMethodField()
    class Meta:     
        model = deviceLocation
        # fields = "__all__"
        # exclude = ["transactionId" , "id" , ]
        fields = ["gpsTime" , "gprsTime" , "altitude" , "heading" ,  "speedKph" ,"address",
                   "odometer" , "gpsSignal" , "created_at" , "device_name" ,"registrationNumber" ,
                   "trackingCode" , "stateOfCharge"]
        geo_field='location'

    def get_device_name(self , value):
        try:
            data = value.device.name
        except:
            data = None
        return data
    
    def get_registrationNumber(self, value):
        try:
            data = value.device.registrationNumber
        except:
            data = None
        return data
    
    def get_trackingCode(self, value):
        try:
            data = value.device.trackingCode
        except:
            data = None
        return data
    
    def get_stateOfCharge(self, value):
        try:
            can_info_queryset = value.device.canInfo_devices.all()
            state_of_charge_values = can_info_queryset.latest("created_at").stateOfCharge
        except:
            state_of_charge_values = None
      
        return state_of_charge_values
       
        
class CanInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = canInfo
        # fields = ["vehicleBattery" , "stateOfCharge" , "AMinCellVolt" , "AMinCellVolt" "APackVoltageValue" ,] 
        exclude = ["id" , "device" , "AMinCellVolt" ,
                   "BMaxCellVolt" , "AMaxCellVolt" , "BMinCellVolt" , "transactionId"]
        

class AlertsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = alerts
        exclude = [  "device" , "transactionId"]
        geo_field= 'location'


class TodaysDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = todaysDrive
        exclude = ["id"  , "device" , "transactionId"]


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = links
        exclude = ["id" ,  "device" , "transactionId"]


class DinputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = dinputs
        exclude = ["id" , "device" , "transactionId"]




# class MBMTDeviceLocationSerializer(GeoFeatureModelSerializer):
#     # device_name = serializers.SerializerMethodField()
#     # registrationNumber = serializers.SerializerMethodField()
#     # trackingCode = serializers.SerializerMethodField()
#     stateOfCharge = serializers.SerializerMethodField()
#     class Meta:     
#         model = deviceLocation
#         # fields = "__all__"
#         # exclude = ["transactionId" , "id" , ]
#         fields = ["gpsTime" , "gprsTime" , "altitude" , "heading" ,  "speedKph" ,"address",
#                    "odometer" , "gpsSignal" , "created_at" ,  "stateOfCharge"]
#         geo_field='location'

    def get_stateOfCharge(self, value):
        try:
            can_info_queryset = value.device.canInfo_devices.all()
            state_of_charge_values = can_info_queryset.latest("created_at").stateOfCharge
        except:
            state_of_charge_values = None
      
        return state_of_charge_values
    

# class post_test_deviceserialzier(serializers.ModelSerializer):
#     class Meta:
#         model = test_models
#         fields = "__all__"



class DataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterDeviceDetails
        exclude = ("id" ,'device')
        
        depth = 1


class getDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterDeviceDetails
        exclude = ("id" , )

        depth = 1
    
class MBMTDeviceLocationSerializer(GeoFeatureModelSerializer):
    # device_name = serializers.SerializerMethodField()
    # registrationNumber = serializers.SerializerMethodField()
    # trackingCode = serializers.SerializerMethodField()
    # stateOfCharge = serializers.SerializerMethodField()
    class Meta:     
        model = MasterDeviceDetails
        # fields = "__all__"
        # exclude = ["transactionId" , "id" , ]
        fields = ["gpsTime" , "gprsTime" , "altitude" , "heading" ,  "speedKph" ,"address",
                   "odometer" , "gpsSignal" , "created_at" ,  "stateOfCharge"]
        geo_field='device_location'




     
class NoidaExtenToIncedointellectRouteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = NoidaExtenToIncedointellectRoute
        fields = ("name" ,)
        geo_field = "geom"
         

class NoidaExtenToIncedointellectStopsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = NoidaExtenToIncedointellectStops
        fields = ("name" ,)
        geo_field = "geom"