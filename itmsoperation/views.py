# from django.shortcuts import render
# from .models import ConfigCompanymaster
# from rest_framework.generics import GenericAPIView
# # Create your views here.

# from django.db.models import Max, Min, Sum, F, Q, Case, When, Value , OuterRef , Subquery
# from rest_framework.response import Response
# from rest_framework import status
# from .models import *
# from django.db.models.functions import Coalesce
# from .serializers import BusInformationSerializer
# from rest_framework.permissions import IsAuthenticated
# from vehicle.permissions import IsMBMT
# from schedulingMgmt.permissions import IsUber










# class GetBussesList(GenericAPIView):
#     serializer_class =BusInformationSerializer
#     permission_classes = [IsAuthenticated , IsUber | IsMBMT ]

#     def post(self, request, *args, **kwargs):
#         date = request.query_params.get('date', None)
#         vehicle_number = request.query_params.get('vehicle_number', '')
#         page = int(request.query_params.get('page', 1))
#         page_size = int(request.query_params.get('page_size', 10))
#         user_group = str(request.user.groups.first())
#         # print(OprSchedulingdetails.objects.using('itms').all())
#         latest_scheduling_date_subquery = OprScheduling.objects.using('itms').filter(
#             schedulingid=OuterRef('schedulingid'),
#             schedulingdate=date  # Filter by the specific date
#         ).first()


        
#         # print(latest_scheduling_date_subquery)
#         buses_qs = MtnBusinformation.objects.using('itms').filter(
#             companyid_id=1
#         ).annotate(

            
#            latest_scheduling_date = OprSchedulingdetails.objects.using('itms').filter(
#                 businformationid=F('businformationid')
#             ).annotate(
#                 latest_scheduling_date=Coalesce(
#                   latest_scheduling_date_subquery = OprScheduling.objects.using('itms').filter(
#                             schedulingid=OuterRef('schedulingid'),
#                             schedulingdate=date  # Filter by the specific date
#                         ),
            
#                 )
#                 ).values('latest_scheduling_date'),
#             # total_km_run_today=Coalesce(
#             #     Sum(F('schedulingdetails__end_odo') - F('schedulingdetails__start_odo')),
#             #     Value(0)
#             # ),
#             # status=Case(
#             #     When(SchedulingDetails__isnull=False, then=Value('Active')),
#             #     default=Value('Not Scheduled'),
#             #     output_field=models.CharField()
#             # ),
#             # last_odo=Coalesce(
#             #     OprSchedulingdetails.objects.filter(businformationid=F('businformationid'))
#             #     .values('endodo').latest('endodo'), Value(0)
#             # ),
#             # total_energy_consumed=Coalesce(Sum('buscharging__energy_consumption'), Value(0)),
#             # today_energy_consumption=Coalesce(
#             #     Sum(Case(When(buscharging__charging_date=date, then=F('buscharging__energy_consumption')))),
#             #     Value(0)
#             # ),
#             # charging_cycles=Coalesce(
#             #     Sum(Case(When(F('buscharging__end_soc') - F('buscharging__start_soc') > 0, then=F('buscharging__end_soc') - F('buscharging__start_soc')))) / 100.0,
#             #     Value(0)
#             # )
#         )
#         print(buses_qs)
#         if vehicle_number:
#             buses_qs = buses_qs.filter(vehicle_number__icontains=vehicle_number)

#         total_count = buses_qs.count()

#         buses_qs = buses_qs[(page - 1) * page_size: page * page_size]

#         serializer = BusInformationSerializer(buses_qs, many=True)
        
#         result = {
#             "status": "success",
#             "data": {
#                 'buses_list': serializer.data,
#                 'total_count': total_count,
#                 'total_page_count': (total_count + page_size - 1) // page_size,
#                 'page': page,
#                 'page_size': page_size
#             }
#         }
#         return Response(result)
