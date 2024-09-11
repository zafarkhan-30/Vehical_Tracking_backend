# from django.db import models
# import datetime
# from django.contrib.gis.db import models

# class ConfigCompanymaster(models.Model):
#     companyid = models.AutoField(db_column='CompanyId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     # organisationid = models.ForeignKey('ConfigOrganisationmaster', models.DO_NOTHING, db_column='OrganisationId', db_comment='Foreign Key')  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=200)  # Field name made lowercase.
#     companycode = models.CharField(db_column='CompanyCode', max_length=50)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=500)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=100)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     emailid = models.CharField(db_column='EmailId', max_length=200)  # Field name made lowercase.
#     contactno = models.IntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dateofregistration = models.DateField(db_column='DateOfRegistration')  # Field name made lowercase.
#     bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
#     bankaccountno = models.CharField(db_column='BankAccountNo', max_length=50)  # Field name made lowercase.
#     ifscode = models.CharField(db_column='IFSCode', max_length=50)  # Field name made lowercase.
#     swiscode = models.CharField(db_column='SWISCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pan = models.CharField(db_column='PAN', max_length=50)  # Field name made lowercase.
#     tin = models.CharField(db_column='TIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     gstrn = models.CharField(db_column='GSTRN', max_length=50)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True, db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CONFIG_CompanyMaster'

# class ConfigOrganisationmaster(models.Model):
#     organisationid = models.IntegerField(db_column='OrganisationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     organisationname = models.CharField(db_column='OrganisationName', max_length=200)  # Field name made lowercase.
#     organisationcode = models.CharField(db_column='OrganisationCode', max_length=50)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=500)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     emailid = models.CharField(db_column='EmailId', max_length=50)  # Field name made lowercase.
#     contactno = models.IntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dateofregistration = models.DateField(db_column='DateOfRegistration')  # Field name made lowercase.
#     bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
#     bankaccountno = models.CharField(db_column='BankAccountNo', max_length=50)  # Field name made lowercase.
#     ifscode = models.CharField(db_column='IFSCode', max_length=50)  # Field name made lowercase.
#     swiscode = models.CharField(db_column='SWISCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pan = models.CharField(db_column='PAN', max_length=50)  # Field name made lowercase.
#     tin = models.CharField(db_column='TIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     gstrn = models.CharField(db_column='GSTRN', max_length=50)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CONFIG_OrganisationMaster'


# class ConfigCompanymaster(models.Model):
#     companyid = models.AutoField(db_column='CompanyId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     organisationid = models.ForeignKey('ConfigOrganisationmaster', models.DO_NOTHING, db_column='OrganisationId', db_comment='Foreign Key')  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=200)  # Field name made lowercase.
#     companycode = models.CharField(db_column='CompanyCode', max_length=50)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=500)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=100)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     emailid = models.CharField(db_column='EmailId', max_length=200)  # Field name made lowercase.
#     contactno = models.IntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dateofregistration = models.DateField(db_column='DateOfRegistration')  # Field name made lowercase.
#     bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
#     bankaccountno = models.CharField(db_column='BankAccountNo', max_length=50)  # Field name made lowercase.
#     ifscode = models.CharField(db_column='IFSCode', max_length=50)  # Field name made lowercase.
#     swiscode = models.CharField(db_column='SWISCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pan = models.CharField(db_column='PAN', max_length=50)  # Field name made lowercase.
#     tin = models.CharField(db_column='TIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     gstrn = models.CharField(db_column='GSTRN', max_length=50)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True, db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CONFIG_CompanyMaster'


# class MtnChargermaster(models.Model):
#     chargermasterid = models.AutoField(db_column='ChargerMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     chargernumber = models.CharField(db_column='ChargerNumber', max_length=50)  # Field name made lowercase.
#     serialnumber = models.CharField(db_column='SerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     energyconsumption = models.FloatField(db_column='EnergyConsumption')  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.
#     odometer = models.FloatField(db_column='OdoMeter', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MTN_ChargerMaster'



# class MtnBuscharging(models.Model):
#     buschargingid = models.OneToOneField('self', models.DO_NOTHING, db_column='BusChargingId', primary_key=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     chargermasterid = models.IntegerField(db_column='ChargerMasterId')  # Field name made lowercase.
#     chargingdate = models.DateTimeField(db_column='ChargingDate')  # Field name made lowercase.
#     startodo = models.FloatField(db_column='StartODO', blank=True, null=True)  # Field name made lowercase.
#     startsoc = models.FloatField(db_column='StartSOC', blank=True, null=True)  # Field name made lowercase.
#     endsoc = models.FloatField(db_column='EndSOC', blank=True, null=True)  # Field name made lowercase.
#     starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
#     endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
#     sessiontime = models.CharField(db_column='SessionTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     energyconsumption = models.FloatField(db_column='EnergyConsumption', blank=True, null=True)  # Field name made lowercase.
#     buschargeemployee = models.IntegerField(db_column='BusChargeEmployee', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lastodo = models.FloatField(db_column='LastODO', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MTN_BusCharging'


# class MtnBusinformation(models.Model):
#     businformationid = models.AutoField(db_column='BusInformationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     branchid = models.IntegerField(db_column='BranchId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     vehicletype = models.CharField(db_column='VehicleType', max_length=50)  # Field name made lowercase.
#     bustype = models.CharField(db_column='BusType', max_length=50)  # Field name made lowercase.
#     buscode = models.CharField(db_column='BusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dateofregistration = models.DateField(db_column='DateOfRegistration')  # Field name made lowercase.
#     dateofpurchase = models.DateField(db_column='DateOfPurchase')  # Field name made lowercase.
#     vehiclenumber = models.CharField(db_column='VehicleNumber', max_length=50)  # Field name made lowercase.
#     chasisnumber = models.CharField(db_column='ChasisNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     enginenumber = models.CharField(db_column='EngineNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     buscolour = models.CharField(db_column='BusColour', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     seatcapacity = models.IntegerField(db_column='SeatCapacity', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     wheelertypeid = models.IntegerField(db_column='WheelerTypeId', blank=True, null=True)  # Field name made lowercase.
#     fueltype = models.CharField(db_column='FuelType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     batterytype = models.CharField(db_column='BatteryType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fueltank1 = models.IntegerField(db_column='FuelTank1', blank=True, null=True)  # Field name made lowercase.
#     fueltank2 = models.IntegerField(db_column='FuelTank2', blank=True, null=True)  # Field name made lowercase.
#     oiltank = models.IntegerField(db_column='OilTank', blank=True, null=True)  # Field name made lowercase.
#     make = models.CharField(db_column='Make', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ownername = models.CharField(db_column='OwnerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hypothecation = models.CharField(db_column='Hypothecation', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     emiduedate = models.DateField(db_column='EMIDueDate', blank=True, null=True)  # Field name made lowercase.
#     manufacturingyear = models.CharField(db_column='ManufacturingYear', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bodytype = models.CharField(db_column='BodyType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     enginetype = models.CharField(db_column='EngineType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     settinglayout = models.CharField(db_column='SettingLayout', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lastodometer = models.FloatField(db_column='LastOdometer', blank=True, null=True)  # Field name made lowercase.
#     avlsdevice = models.CharField(db_column='AVLSDevice', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     purchaseinstitute = models.IntegerField(db_column='PurchaseInstitute', blank=True, null=True)  # Field name made lowercase.
#     customertype = models.CharField(db_column='CustomerType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fixavg = models.FloatField(db_column='FixAvg')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     vltdcertificateno = models.CharField(db_column='VLTDCertificateNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     vltdcertificatedate = models.DateField(db_column='VLTDCertificateDate', blank=True, null=True)  # Field name made lowercase.
#     isavailable = models.BooleanField(db_column='IsAvailable', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MTN_BusInformation'




# class OprRoute(models.Model):
#     routeid = models.AutoField(db_column='RouteId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     stagenumber = models.IntegerField(db_column='StageNumber')  # Field name made lowercase.
#     applicabledate = models.DateField(db_column='ApplicableDate')  # Field name made lowercase.
#     totalkm = models.IntegerField(db_column='TotalKM', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_Route'

# class OprSchedule(models.Model):
#     scheduleid = models.AutoField(db_column='ScheduleId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     routeid = models.ForeignKey(OprRoute, models.DO_NOTHING, db_column='RouteId', db_comment='Foreign Key')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
#     shift = models.CharField(db_column='Shift', max_length=50)  # Field name made lowercase.
#     applicabledate = models.DateField(db_column='ApplicableDate', blank=True, null=True)  # Field name made lowercase.
#     sfromtime = models.CharField(db_column='SFromTime', max_length=50)  # Field name made lowercase.
#     stotime = models.CharField(db_column='SToTime', max_length=50)  # Field name made lowercase.
#     totaltrip = models.IntegerField(db_column='TotalTrip', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     dfromstage = models.CharField(db_column='DFromStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dtostage = models.CharField(db_column='DToStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     totaldeadkm = models.FloatField(db_column='TotalDeadKM', blank=True, null=True)  # Field name made lowercase.
#     callingtime = models.CharField(db_column='CallingTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     minsoc = models.FloatField(db_column='MinSOC', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.
#     issubroute = models.BooleanField(db_column='IsSubRoute', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_Schedule'


# class OprScheduletrip(models.Model):
#     scheduletripid = models.AutoField(db_column='ScheduleTripId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     scheduleid = models.IntegerField(db_column='ScheduleId', db_comment='Foreign Key')  # Field name made lowercase.
#     starttime = models.CharField(db_column='StartTime', max_length=50)  # Field name made lowercase.
#     endtime = models.CharField(db_column='EndTime', max_length=50)  # Field name made lowercase.
#     fromstage = models.CharField(db_column='FromStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     tostage = models.CharField(db_column='ToStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     distanceinkm = models.FloatField(db_column='DistanceInKM', blank=True, null=True)  # Field name made lowercase.
#     isdead = models.BooleanField(db_column='IsDead', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.
#     routeid = models.IntegerField(db_column='RouteId', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_ScheduleTrip'


# class OprScheduling(models.Model):
#     schedulingid = models.AutoField(db_column='SchedulingId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     zoneid = models.IntegerField(db_column='ZoneId', db_comment='Foreign Key')  # Field name made lowercase.
#     zonecode = models.CharField(db_column='ZoneCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     shift = models.CharField(db_column='Shift', max_length=50)  # Field name made lowercase.
#     schedulingdate = models.DateField(db_column='SchedulingDate')  # Field name made lowercase.
#     extraconductor = models.IntegerField(db_column='ExtraConductor')  # Field name made lowercase.
#     extradriver = models.IntegerField(db_column='ExtraDriver')  # Field name made lowercase.
#     isapproved = models.BooleanField(db_column='IsApproved', blank=True, null=True)  # Field name made lowercase.
#     approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
#     isapproved1 = models.BooleanField(db_column='IsApproved1', blank=True, null=True)  # Field name made lowercase.
#     approvedby1 = models.CharField(db_column='ApprovedBy1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate1 = models.DateTimeField(db_column='ApprovedDate1', blank=True, null=True)  # Field name made lowercase.
#     isapproved2 = models.BooleanField(db_column='IsApproved2', blank=True, null=True)  # Field name made lowercase.
#     approvedby2 = models.CharField(db_column='ApprovedBy2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate2 = models.DateTimeField(db_column='ApprovedDate2', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.
#     onroadbuses = models.IntegerField(db_column='OnRoadBuses', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_Scheduling'
#         unique_together = (('schedulingdate', 'shift', 'zoneid'),)


# class OprSchedulingdetails(models.Model):
#     schedulingdetailsid = models.AutoField(db_column='SchedulingDetailsId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     schedulingid = models.IntegerField(db_column='SchedulingId', db_comment='Foreign Key')  # Field name made lowercase.
#     scheduleid = models.IntegerField(db_column='ScheduleId', db_comment='Foreign Key')  # Field name made lowercase.
#     starttime = models.CharField(db_column='StartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     endtime = models.CharField(db_column='EndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nooftrips = models.IntegerField(db_column='NoOfTrips')  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     buscode = models.CharField(db_column='BusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     conductorid = models.IntegerField(db_column='ConductorId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     conductorname = models.CharField(db_column='ConductorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     driverid = models.IntegerField(db_column='DriverId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     drivername = models.CharField(db_column='DriverName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     conductorcode = models.CharField(db_column='ConductorCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     updateremark = models.CharField(db_column='UpdateRemark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     startsoc = models.FloatField(db_column='StartSOC', blank=True, null=True)  # Field name made lowercase.
#     endsoc = models.FloatField(db_column='EndSOC', blank=True, null=True)  # Field name made lowercase.
#     startodo = models.FloatField(db_column='StartODO', blank=True, null=True)  # Field name made lowercase.
#     endodo = models.FloatField(db_column='EndODO', blank=True, null=True)  # Field name made lowercase.
#     lastodo = models.FloatField(db_column='LastODO', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     changebus = models.IntegerField(db_column='ChangeBus', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     islostremark = models.IntegerField(db_column='IsLostRemark', blank=True, null=True)  # Field name made lowercase.
#     islost = models.BooleanField(db_column='IsLost')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.
#     isclose = models.BooleanField(db_column='IsClose', blank=True, null=True)  # Field name made lowercase.
#     closeremark = models.CharField(db_column='CloseRemark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     closedate = models.DateTimeField(db_column='CloseDate', blank=True, null=True)  # Field name made lowercase.
#     istransfer = models.BooleanField(db_column='IsTransfer', blank=True, null=True)  # Field name made lowercase.
#     cstartsoc = models.FloatField(db_column='CStartSOC', blank=True, null=True)  # Field name made lowercase.
#     cendsoc = models.FloatField(db_column='CEndSOC', blank=True, null=True)  # Field name made lowercase.
#     cstartodo = models.FloatField(db_column='CStartODO', blank=True, null=True)  # Field name made lowercase.
#     cendodo = models.FloatField(db_column='CEndODO', blank=True, null=True)  # Field name made lowercase.
#     clastodo = models.FloatField(db_column='CLastODO', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_SchedulingDetails'
#         unique_together = (('scheduleid', 'schedulingid'),)


# class OprSchedulingdetailsbc(models.Model):
#     schedulingdetailsbcid = models.AutoField(db_column='SchedulingDetailsBCId', primary_key=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId', db_comment='Primery Key')  # Field name made lowercase.
#     startsoc = models.FloatField(db_column='StartSOC', blank=True, null=True)  # Field name made lowercase.
#     endsoc = models.FloatField(db_column='EndSOC', blank=True, null=True)  # Field name made lowercase.
#     startodo = models.FloatField(db_column='StartODO', blank=True, null=True)  # Field name made lowercase.
#     endodo = models.FloatField(db_column='EndODO', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_SchedulingDetailsBC'




