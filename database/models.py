from django.db import models
import datetime
from django.contrib.gis.db import models

import pytz

# Create your models here.



class devices(models.Model):
    device_id = models.IntegerField()
    name = models.CharField(max_length=100 , blank = True , null =True )
    registrationNumber  = models.CharField(max_length= 255, blank=True  , null =  True )
    deviceType = models.CharField(max_length = 255, blank=True , null = True    )
    chassisNumber = models.CharField(max_length = 255, blank=True , null    = True )
    trackingCode = models.CharField(max_length = 255, blank=True , null = True ) 
    created_at = models.DateTimeField(auto_now=True)


class deviceStatus(models.Model):
    device = models.ForeignKey(devices , related_name="deviceStatus" , on_delete=models.CASCADE) 
    transactionId = models.CharField(max_length=100 , null = False , blank = False)
    active = models.BooleanField(default=False)
    status = models.CharField(max_length= 100 , blank=True , null = True )
    created_at = models.DateTimeField(auto_now=True)

class deviceLocation(models.Model):
    device = models.ForeignKey(devices , related_name="deviceLocation" , on_delete=models.CASCADE , null = True )
    transactionId = models.CharField(max_length=100 , null = False , blank = False)
    gpsTime = models.DateTimeField( )
    gprsTime = models.DateTimeField()
    latitude = models.DecimalField(max_digits=20, decimal_places=18)
    longitude = models.DecimalField(max_digits=20, decimal_places=18)
    location = models.PointField(null= True , blank= True)
    altitude = models.IntegerField()
    heading = models.IntegerField()
    speedKph = models.IntegerField()
    address = models.CharField(max_length= 1000 )
    odometer = models.BigIntegerField()
    gpsSignal = models.IntegerField()
    created_at = models.DateTimeField(auto_now= True)

class canInfo( models.Model):
    device = models.ForeignKey(devices , related_name = "canInfo_devices" , on_delete = models.CASCADE , null = True)
    transactionId = models.CharField(max_length=100 , null = False , blank = False)
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
    created_at = models.DateTimeField(auto_now= True)

class alerts(models.Model):
    device = models.ForeignKey(devices , related_name= "device_alerts" , on_delete = models.CASCADE , null = True)
    transactionId = models.CharField(max_length=100 , null = False , blank = False)
    timestamp = models.BigIntegerField(null = True)
    latitude= models.DecimalField(max_digits=20, decimal_places=18 ,null = True)
    longitude= models.DecimalField(max_digits=20, decimal_places=18 , null = True)
    location = models.PointField(null= True , blank= True)
    address = models.CharField(max_length=1000 )
    alarmType = models.IntegerField(null = True)
    limit = models.IntegerField(null = True)
    severity = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now=True)


class todaysDrive(models.Model):
    device = models.ForeignKey(devices , related_name = "device_todaysDrive" , on_delete = models.CASCADE)
    transactionId = models.CharField(max_length=100 , null = False , blank = False)
    todayKms = models.IntegerField(null = True)
    todayMovementTime =  models.IntegerField(null = True)
    todayIdleTime =  models.IntegerField(null = True)
    todayDriveCount =  models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now=True)

class links(models.Model):
    device = models.ForeignKey(devices , related_name = "device_links" , on_delete = models.CASCADE)
    transactionId = models.CharField(max_length=100 , null = False , blank = False)
    embedUrl = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

class dinputs(models.Model):
    device = models.ForeignKey(devices , related_name = "device_dinputs" , on_delete = models.CASCADE , null = True) 
    transactionId = models.CharField(max_length=100 , null = False , blank = False)
    input_1 = models.IntegerField(null = True)
    input_2 = models.IntegerField(null = True)
    input_3 = models.IntegerField(null = True)
    input_4 = models.IntegerField(null = True)
    input_5 = models.IntegerField(null = True)
    input_6 = models.IntegerField(null = True)
    input_7 = models.IntegerField(null = True)
    
    created_at = models.DateTimeField(auto_now=True)











