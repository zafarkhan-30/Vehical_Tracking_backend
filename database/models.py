from django.db import models
import datetime
from django.contrib.gis.db import models
from django.db.utils import DataError
from decimal import Decimal


# Create your models here.



class devices(models.Model):
    device_id = models.IntegerField()
    name = models.CharField(max_length=100 , blank = True , null =True )
    registrationNumber  = models.CharField(max_length= 255, blank=True  , null =  True )
    deviceType = models.CharField(max_length = 255, blank=True , null = True    )
    chassisNumber = models.CharField(max_length = 255, blank=True , null    = True )
    trackingCode = models.CharField(max_length = 255, blank=True , null = True ) 
    status = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class MasterDeviceDetails(models.Model):
    device = models.ForeignKey(devices , related_name = "master_device_id" , on_delete = models.CASCADE, null = True)

    active = models.BooleanField(default=False)
    status = models.CharField(max_length= 100 , blank=True , null = True )

    gpsTime = models.DateTimeField( null = True )
    gprsTime = models.DateTimeField(null= True )
    device_location = models.PointField(null= True , blank= True)
    altitude = models.IntegerField(null = True)
    heading = models.IntegerField(null = True)
    speedKph = models.IntegerField(null = True)
    address = models.CharField(max_length= 1000 , blank = True , null = True )
    odometer = models.BigIntegerField(null = True)
    gpsSignal = models.IntegerField(null = True)

    vehicleBattery = models.BigIntegerField(null = True)
    stateOfCharge = models.IntegerField(null = True  )
    AMinCellVolt = models.BigIntegerField( null = True )
    APackVoltageValue= models.BigIntegerField( null = True )
    APackCurrentValue= models.BigIntegerField( null = True )
    batteryTemperature= models.BigIntegerField( null = True )
    ASOCValue= models.BigIntegerField( null = True )
    BFaultRank= models.BigIntegerField( null = True )
    totalRegenerationEnergy= models.BigIntegerField(null = True )
    BPackCurrentValue= models.BigIntegerField( null = True )
    BMaxCellVolt= models.BigIntegerField(null = True )
    ChargerGunDetected2= models.BigIntegerField(null = True )
    AMaxCellVolt= models.BigIntegerField(null = True )
    BMinCellVolt= models.BigIntegerField(null = True )
    BPackVoltageValue= models.BigIntegerField(null = True )
    AFaultRank= models.BigIntegerField(null = True )
    BSOCValue= models.BigIntegerField(null = True )
    distanceToEmpty = models.BigIntegerField(null = True )


    timestamp = models.BigIntegerField(null = True)
    alert_location = models.PointField(null= True , blank= True)
    alert_address = models.CharField(max_length=1000 , blank = True , null = True)
    alarmType = models.IntegerField(null = True)
    limits = models.IntegerField(null = True)
    severity = models.IntegerField(null = True)

    todayKms = models.IntegerField(null = True)
    todayMovementTime =  models.IntegerField(null = True)
    todayIdleTime =  models.IntegerField(null = True)
    todayDriveCount =  models.IntegerField(null = True)

    embedUrl = models.CharField(max_length=500 , null = True , blank= True )

    input_1 = models.IntegerField(null = True)
    input_2 = models.IntegerField(null = True)
    input_3 = models.IntegerField(null = True)
    input_4 = models.IntegerField(null = True)
    input_5 = models.IntegerField(null = True)
    input_6 = models.IntegerField(null = True)
    input_7 = models.IntegerField(null = True)
    
    created_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except DataError as e:
            if e.args[0].startswith('DETAIL: A field with precision 20, scale 18 must round to an absolute value less than 10^2'):
                self.latitude = Decimal(str(self.latitude).round(2))
                self.longitude = Decimal(str(self.longitude).round(2))
                super().save(*args, **kwargs)



class NoidaExtenToIncedointellectRoute(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noida exten_to_incedointellect_route'



class NoidaExtenToIncedointellectStops(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    folderpath = models.CharField(max_length=254, blank=True, null=True)
    symbolid = models.FloatField(blank=True, null=True)
    altmode = models.IntegerField(blank=True, null=True)
    base = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    snippet = models.CharField(max_length=254, blank=True, null=True)
    popupinfo = models.CharField(max_length=254, blank=True, null=True)
    haslabel = models.IntegerField(blank=True, null=True)
    labelid = models.FloatField(blank=True, null=True)
    geom = models.PointField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noida exten_to_incedointellect_route_stops'





class RouteNo15(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route no_15'




class RouteNo15BusStops(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route no_15_bus stops'



class Chargingsation(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chargingSation'