from django.shortcuts import render
from rest_framework import generics 
from rest_framework.response import Response
import json
from database.models import *
from .database_opertaions import *
import time
from .utils import *
from .serializers import *
import uuid
from rest_framework.views import APIView
from datetime import  date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser
from .permissions import *

class UserRegister(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]    

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                group_name = serializer.validated_data.get('groups')
                usergroup = Group.objects.get(name= group_name)
            
                user = serializer.save()
        
                if usergroup:
                    user.groups.add(usergroup)
                

                return Response({'message': 'Registration Successfull' , 
                                    "status" : "success" }, status=200)
            except:
                return Response({'message': 'Please select any one group',
                                 "status" : "error"}, status=400)
        else:
            key, value =list(serializer.errors.items())[0]
            try:
                key , value = list(value[0].items())[0]
                error_message =  str(value[0])
            except Exception as e:
                try:
                     error_message = str(key) + " ," +str(value[0])
                except:
                    key , value = list(value[1].items())[0]
                    error_message = str(key) + " ," +str(value[0])
            
            return Response({'message': error_message, 
                             "status" : "error"}, status=400)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # parser_classes = [JSONParser]

    def post(self , request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
           
            user = authenticate(username=username , password=password)
            if user is not None:
                user1 = User.objects.filter(username=username)
                serializer2 = RegisterSerializer(user1 ,many=True)
                try:
                    token = Token.objects.create(user=user)
                except:
                    token = Token.objects.get(user=user)

                return Response({
                                'Token':token.key,
                                } , 
                                status=200)
            else:
                return Response({'status': 'error',
                                'message': "username or password is not valid , Please try again."} , status=status.HTTP_400_BAD_REQUEST)
        else:
            # print(serializer.errors)
            return Response({'status': 'error',
                            'message': "username or password is not valid , Please try again."} , status=status.HTTP_400_BAD_REQUEST)


class PostMasterDeviceData(APIView):

    def get(self , request):
        refresh_token = refresh_access_token()
        response = get_device_Data(refresh_token)
        # print(response)

        if response.status_code == 200:

            devices_data = json.loads(response.content).get('data')
            # print(devices_data)

            master_data_list = []

            for data in devices_data:
                device_id = data.get("id")

                if "deviceDetails" in data:
                    create_device_object(data)
                
                master_data_list.append(create_master_device_details(device_id , data))
                
            master_object = MasterDeviceDetails.objects.bulk_create(master_data_list)

            return Response({"message": "device data created successfully"}, status=200)

        else:
            return Response(response.content, status=response.status_code)
 

class PostDeviceDetailsView(APIView):

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
        
        
class ViewDeviceAllDetails(APIView):
    permission_classes = [IsAuthenticated , IsAchargeZone  | IsBattery_IQ | IsAmnex ]
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
        
        queryset = devices.objects.none()  # Initialize an empty queryset
        if name:
            queryset |= devices.objects.filter(name__icontains='MBMT')
        else:
           queryset |= devices.objects.all()
            
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

        all_devices = self.get_queryset()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if all_devices:
            
            for device in all_devices:
                device_details_serailizer = deviceDetailsSerialiser(device).data
                today = date.today()
                if start_date and end_date:
                    try:
                        master_data_list = MasterDeviceDetails.objects.filter(device_id = device , created_at__range=[start_date , end_date]).latest("created_at")
                        
                    except:
                        continue
                else:
                    try:
                        master_data_list = MasterDeviceDetails.objects.filter(device_id = device , created_at__date=today).latest("created_at")
                    except:
                        continue

                data_list_serializer = DataListSerializer(master_data_list).data
                data_list.append({
                    'data' : data_list_serializer

                })

        if len(data_list) ==0:
            return Response({'status': 'error' , 'message': 'No data available'} , status= 200)
        else:
         
             return Response(data_list)
             
class ViewAllMBMTDeviceDetails(generics.GenericAPIView):
    permission_classes = [IsAuthenticated , IsMBMT | IsAmnex]

    # throttle_classes = [AnonRateThrottle]
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
        queryset = devices.objects.none()
       
        if name:
            queryset |= devices.objects.filter(name__icontains='MBMT')
        else:
            queryset |= devices.objects.filter(name__icontains='MBMT')
            
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
        # print(all_devices)
        if all_devices:
          
            for device in all_devices:
                device_details_serailizer = deviceDetailsSerialiser(device).data
                today = date.today()
                print(device)
                
                try:
                    device_location = MasterDeviceDetails.objects.filter(device_id=device, created_at__date=today).latest("created_at")
                    
                    device_location_serializer = MBMTDeviceLocationSerializer(device_location).data
                except:
                    continue

                # try:
                #     canInfo_detail = canInfo.objects.filter(device_id = device , created_at__date=today).latest("created_at")
                #     canInfo_serializer = CanInfoSerializer(canInfo_detail).data
                # except canInfo.DoesNotExist:
                #     canInfo_serializer = {}

            
                data_list.append({
                    'device_details' : device_details_serailizer,
                    'device_location': device_location_serializer,
                    
                    })
        else: 
            return Response({'status': 'error' , 'message': 'No data available'} , status= 200)
         
        return Response(data_list)
    
class ViewAmnexDeviceDetails(APIView):
    permission_classes = [IsAuthenticated , IsAmnex | IsBattery_IQ]

    def get_queryset(self):
        
        # name = self.request.query_params.get('name')
        
        # queryset = devices.objects.none()  # Initialize an empty queryset
        # if name:
        #     queryset |= devices.objects.filter(name__icontains='MBMT')
        # else:
        queryset = devices.objects.filter(name__icontains='MBMT')
            
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
        # print(all_devices)
        if all_devices:
          
            for device in all_devices:
                device_details_serailizer = deviceDetailsSerialiser(device).data
                today = date.today()
                
                # try:
                #     # device_location = deviceLocation.objects.filter(device=device ,created_at = datetime.datetime.today()).latest("created_at")
                #     device_location = deviceLocation.objects.filter(device=device, created_at__date=today).latest("created_at")
                #     device_location_serializer = DeviceLocationSerializer(device_location).data
                # except deviceLocation.DoesNotExist:
                #     device_location_serializer ={}

                # try:
                #     device_status = deviceStatus.objects.filter(device_id=device , created_at__date=today).latest("created_at")
                #     device_status_serializer = DeviceStatusSerializer(device_status).data
                # except deviceStatus.DoesNotExist:
                #     device_status_serializer = {}


                # try:
                #     canInfo_detail = canInfo.objects.filter(device_id = device , created_at__date=today).latest("created_at")
                #     canInfo_serializer = CanInfoSerializer(canInfo_detail).data
                # except canInfo.DoesNotExist:
                #     canInfo_serializer = {}

                # try:
                #     alerts_detail = alerts.objects.filter(device_id = device , created_at__date=today).latest("created_at")
                #     alerts_serializer = AlertsSerializer(alerts_detail).data
                # except alerts.DoesNotExist:
                #     alerts_serializer = {}
                
                # try:
                #     todaysDrive_detail = todaysDrive.objects.filter(device_id = device , created_at__date=today).latest("created_at")
                #     todaysDrive_serializer = TodaysDriveSerializer(todaysDrive_detail).data
                # except todaysDrive.DoesNotExist:
                #     todaysDrive_serializer = {}
                
                # try:
                #     links_detail = links.objects.filter(device_id = device , created_at__date=today).latest("created_at")
                #     links_serializer = LinksSerializer(links_detail).data

                # except links.DoesNotExist:
                #     links_serializer = {}
                # try:
                #     dinputs_detail = dinputs.objects.filter(device_id = device , created_at__date = today).latest("transactionId")
                #     dinputs_serializer = DinputsSerializer(dinputs_detail).data
                # except dinputs.DoesNotExist:
                #     dinputs_serializer = {}

                try:
                    master_data_list = MasterDeviceDetails.objects.filter(device_id = device , created_at__date=today).latest("created_at")
                    data_list_serializer = DataListSerializer(master_data_list).data
                except:
                    continue

                data_list.append({
                    'device_details' : device_details_serailizer,
                    'data' : data_list_serializer
                    # 'device_status': device_status_serializer,
                    # 'device_location': device_location_serializer,
                    # 'canInfo' : canInfo_serializer,
                    # "alerts" : alerts_serializer , 
                    # "todaysDrive" : todaysDrive_serializer,
                    # "links" : links_serializer,
                    # "dinputs" : dinputs_serializer

                })
        else: 
            return Response({'status': 'error' , 'message': 'No data available'} , status= 200)
         
        return Response(data_list)
    



class GetDeviceParametersDetails(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = deviceDetailsSerialiser
    queryset = devices.objects.all()



# class post_test_device(generics.GenericAPIView):
#     serializer_class = post_test_deviceserialzier
#     parser_classes = [MultiPartParser]
#     def post(self, request):
#         serializer = self.get_serializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


