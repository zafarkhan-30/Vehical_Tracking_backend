from django.shortcuts import render
from rest_framework import generics 
import requests 
from rest_framework.response import Response
import json
from database.models import *
from .database_opertaions import *
import time
from .utils import *
from .serializers import *
import uuid
from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView
# Create your views here.
import datetime
from VehicalTracking import settings


class DeviceDetailsView(APIView):

    def get(self, request):
        refresh_token = refresh_access_token()
        response = get_device_Data(refresh_token)
        print(str(uuid.uuid4()))
        
        if response.status_code == 200:

            devices_data = json.loads(response.content).get('data')
            
            device_locations = []
            deviceStatus_details = []
            canInfo_details = []
            alerts_details = []
            todaysDrive_details = []
            links_details = []
            dinputs_details = []

            for data in devices_data:
                transactionId = str(uuid.uuid4())
                device_id = data.get("id")


                if "deviceDetails" in data:
                    create_device_object(data)
                try:
                    if "active" in data and "status" in data:
                        deviceStatus_details.append(create_device_status(device_id, data, transactionId))
                    else:
                        deviceStatus_details.append(create_device_status(device_id, data, transactionId))
                except:
                    pass

                if "location" in data:
                    device_locations.append(create_device_location(device_id, data , transactionId))
                if "canInfo" in data:
                    canInfo_details.append(create_canInfo_object(device_id, data, transactionId))
                if "alerts" in data:
                    alerts_details.append(create_alerts_object(device_id, data, transactionId))
                if "todaysDrive" in data:
                    todaysDrive_details.append(create_todaysDrive_object(device_id, data, transactionId))
                if "links" in data:
                    links_details.append(create_links_object(device_id, data, transactionId))
                if "dinputs" in data:
                    dinputs_details.append(create_dinputs_objects(device_id, data, transactionId))

            location_object = deviceLocation.objects.bulk_create(device_locations)
            deviceStatus_object = deviceStatus.objects.bulk_create(deviceStatus_details)
            canInfo_object = canInfo.objects.bulk_create(canInfo_details)
            alerts_object = alerts.objects.bulk_create(alerts_details)
            todaysDrive_object = todaysDrive.objects.bulk_create(todaysDrive_details)
            links_object = links.objects.bulk_create(links_details)
            dinputs_object = dinputs.objects.bulk_create(dinputs_details)

            return Response({"message": "device data created successfully"}, status=200)

        else:
            return Response(response.content, status=response.status_code)
        
        


class ViewDeviceDetails(generics.GenericAPIView):
    """
    This function is used to filter the queryset based on the 'name' query parameter.
    If 'name' is provided, it filters the devices with names containing the 'name'.
    If 'name' is not provided, it returns all the devices.

    Parameters:
    self (ViewDeviceDetails): The instance of the ViewDeviceDetails class.

    Returns:
    queryset (QuerySet): The filtered queryset of devices.
    """
    def get_queryset(self):
        
        name = self.request.query_params.get('name')
        if name:
           queryset = devices.objects.filter(name__icontains = name)
        else:
            queryset = devices.objects.all()
        return queryset
    

    """
    This function is used to retrieve and serialize device details.
    It fetches all related device details using prefetch_related and then serializes them.
    If no device details are found, it returns an empty response.

    Parameters:
    self (ViewDeviceDetails): The instance of the ViewDeviceDetails class.
    request (Request): The request object containing query parameters.

    Returns:
    Response: A response object containing serialized device details.
    """
    def get(self, request):
        data_list = []
        # all_devices = devices.objects.all()
        all_devices = self.get_queryset()
        if all_devices:
            for device in all_devices:
                device_details_serailizer = deviceDetailsSerialiser(device).data
            
                try:
                    device_location = deviceLocation.objects.filter(device=device).latest("created_at")
                    
                    device_location_serializer = DeviceLocationSerializer(device_location).data
                    print(device_location_serializer)
                except deviceLocation.DoesNotExist:
                    device_location_serializer ={}

                try:
                    device_status = deviceStatus.objects.filter(device_id=device).latest("created_at")
                    device_status_serializer = DeviceStatusSerializer(device_status).data
                except deviceStatus.DoesNotExist:
                    device_status_serializer = {}


                try:
                    canInfo_detail = canInfo.objects.filter(device_id = device).latest("created_at")
                    canInfo_serializer = CanInfoSerializer(canInfo_detail).data
                except canInfo.DoesNotExist:
                    canInfo_serializer = {}

                try:
                    alerts_detail = alerts.objects.filter(device_id = device).latest("-created_at")
                    alerts_serializer = AlertsSerializer(alerts_detail).data
                except alerts.DoesNotExist:
                    alerts_serializer = {}
                
                try:
                    todaysDrive_detail = todaysDrive.objects.filter(device_id = device).latest("created_at")
                    todaysDrive_serializer = TodaysDriveSerializer(todaysDrive_detail).data
                except todaysDrive.DoesNotExist:
                    todaysDrive_serializer = {}
                
                try:
                    links_detail = links.objects.filter(device_id = device).latest("created_at")
                    links_serializer = LinksSerializer(links_detail).data

                except links.DoesNotExist:
                    links_serializer = {}
                try:
                    dinputs_detail = dinputs.objects.filter(device_id = device).latest("transactionId")
                    dinputs_serializer = DinputsSerializer(dinputs_detail).data
                except dinputs.DoesNotExist:
                    dinputs_serializer = {}

                data_list.append({
                    'device_details' : device_details_serailizer,
                    'device_status': device_status_serializer,
                    'device_location': device_location_serializer,
                    'canInfo' : canInfo_serializer,
                    "alerts" : alerts_serializer , 
                    "todaysDrive" : todaysDrive_serializer,
                    "links" : links_serializer,
                    "dinputs" : dinputs_serializer

                })
        else: 
            return Response({'status': 'error' , 'message': 'No data available'} , status= 200)
         
        return Response(data_list)

        


        
        