from rest_framework import serializers



class GetTotalTripCountSerilizsers(serializers.Serializer):
    vehicalNumber = serializers.CharField(max_length=100 , required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)

class GetTotalDistanceSerilizsers(serializers.Serializer):
    vehicalNumber = serializers.CharField(max_length=100 , required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)