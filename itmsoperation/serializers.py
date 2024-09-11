# from rest_framework import serializers
# from .models import *

# class BusInformationSerializer(serializers.ModelSerializer):
#     latest_scheduling_date = serializers.DateField()
#     total_km_run_today = serializers.DecimalField(max_digits=10, decimal_places=2)
#     status = serializers.CharField()
#     last_odo = serializers.DecimalField(max_digits=10, decimal_places=2)
#     total_energy_consumed = serializers.DecimalField(max_digits=10, decimal_places=2)
#     today_energy_consumption = serializers.DecimalField(max_digits=10, decimal_places=2)
#     charging_cycles = serializers.DecimalField(max_digits=10, decimal_places=2)
#     morning_schedule_codes = serializers.CharField()
#     evening_schedule_codes = serializers.CharField()

#     class Meta:
#         model = MtnBusinformation
#         fields = [
#             'bus_information_id', 'bus_code', 'vehicle_number', 'latest_scheduling_date',
#             'total_km_run_today', 'status', 'last_odo', 'total_energy_consumed',
#             'today_energy_consumption', 'charging_cycles', 'morning_schedule_codes',
#             'evening_schedule_codes'
#         ]