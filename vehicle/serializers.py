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
    class Meta:     
        model = MasterDeviceDetails
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




class GetRouteNo15BusStopsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RouteNo15BusStops
        fields = ("name" ,)
        geo_field = "geom"



class GetRoute15Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = RouteNo15
        fields = ("name" ,)
        geo_field = "geom"