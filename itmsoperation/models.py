from django.contrib.gis.db import models

class ConfigOrganisationmaster(models.Model):
    organisationid = models.IntegerField(db_column='OrganisationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
    organisationname = models.CharField(db_column='OrganisationName', max_length=200)  # Field name made lowercase.
    organisationcode = models.CharField(db_column='OrganisationCode', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=50)  # Field name made lowercase.
    contactno = models.IntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofregistration = models.DateField(db_column='DateOfRegistration')  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
    bankaccountno = models.CharField(db_column='BankAccountNo', max_length=50)  # Field name made lowercase.
    ifscode = models.CharField(db_column='IFSCode', max_length=50)  # Field name made lowercase.
    swiscode = models.CharField(db_column='SWISCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=50)  # Field name made lowercase.
    tin = models.CharField(db_column='TIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gstrn = models.CharField(db_column='GSTRN', max_length=50)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
    editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIG_OrganisationMaster'

class ConfigCompanymaster(models.Model):
    companyid = models.AutoField(db_column='CompanyId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
    organisationid = models.ForeignKey('ConfigOrganisationmaster', models.DO_NOTHING, db_column='OrganisationId', db_comment='Foreign Key')  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=200)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=200)  # Field name made lowercase.
    contactno = models.IntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofregistration = models.DateField(db_column='DateOfRegistration')  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
    bankaccountno = models.CharField(db_column='BankAccountNo', max_length=50)  # Field name made lowercase.
    ifscode = models.CharField(db_column='IFSCode', max_length=50)  # Field name made lowercase.
    swiscode = models.CharField(db_column='SWISCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=50)  # Field name made lowercase.
    tin = models.CharField(db_column='TIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gstrn = models.CharField(db_column='GSTRN', max_length=50)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
    entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True, db_comment='Insertion Date')  # Field name made lowercase.
    editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIG_CompanyMaster'



class ConfigBranchmaster(models.Model):
    branchid = models.AutoField(db_column='BranchId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
    companyid = models.ForeignKey('ConfigCompanymaster', models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
    contactno = models.IntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
    entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
    editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIG_BranchMaster'


class ConfigConfigration(models.Model):
    configationid = models.IntegerField(db_column='ConfigationId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    organisationid = models.ForeignKey('ConfigOrganisationmaster', models.DO_NOTHING, db_column='OrganisationId')  # Field name made lowercase.
    iscategory = models.BooleanField(db_column='IsCategory', blank=True, null=True)  # Field name made lowercase.
    isdivision = models.BooleanField(db_column='IsDivision', blank=True, null=True)  # Field name made lowercase.
    isemployeetype = models.BooleanField(db_column='IsEmployeeType', blank=True, null=True)  # Field name made lowercase.
    isgrade = models.BooleanField(db_column='IsGrade', blank=True, null=True)  # Field name made lowercase.
    isproject = models.BooleanField(db_column='IsProject', blank=True, null=True)  # Field name made lowercase.
    isunit = models.BooleanField(db_column='IsUnit', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
    entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIG_Configration'


class OprRoute(models.Model):
    routeid = models.AutoField(db_column='RouteId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
    companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stagenumber = models.IntegerField(db_column='StageNumber')  # Field name made lowercase.
    applicabledate = models.DateField(db_column='ApplicableDate')  # Field name made lowercase.
    totalkm = models.IntegerField(db_column='TotalKM', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
    entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
    editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPR_Route'


class MtnBusinformation(models.Model):
    businformationid = models.AutoField(db_column='BusInformationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
    companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
    vehicletype = models.CharField(db_column='VehicleType', max_length=50)  # Field name made lowercase.
    bustype = models.CharField(db_column='BusType', max_length=50)  # Field name made lowercase.
    buscode = models.CharField(db_column='BusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofregistration = models.DateField(db_column='DateOfRegistration')  # Field name made lowercase.
    dateofpurchase = models.DateField(db_column='DateOfPurchase')  # Field name made lowercase.
    vehiclenumber = models.CharField(db_column='VehicleNumber', max_length=50)  # Field name made lowercase.
    chasisnumber = models.CharField(db_column='ChasisNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enginenumber = models.CharField(db_column='EngineNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    buscolour = models.CharField(db_column='BusColour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seatcapacity = models.IntegerField(db_column='SeatCapacity', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=500, blank=True, null=True)  # Field name made lowercase.
    wheelertypeid = models.IntegerField(db_column='WheelerTypeId', blank=True, null=True)  # Field name made lowercase.
    fueltype = models.CharField(db_column='FuelType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    batterytype = models.CharField(db_column='BatteryType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fueltank1 = models.IntegerField(db_column='FuelTank1', blank=True, null=True)  # Field name made lowercase.
    fueltank2 = models.IntegerField(db_column='FuelTank2', blank=True, null=True)  # Field name made lowercase.
    oiltank = models.IntegerField(db_column='OilTank', blank=True, null=True)  # Field name made lowercase.
    make = models.CharField(db_column='Make', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hypothecation = models.CharField(db_column='Hypothecation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emiduedate = models.DateField(db_column='EMIDueDate', blank=True, null=True)  # Field name made lowercase.
    manufacturingyear = models.CharField(db_column='ManufacturingYear', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bodytype = models.CharField(db_column='BodyType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enginetype = models.CharField(db_column='EngineType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    settinglayout = models.CharField(db_column='SettingLayout', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastodometer = models.FloatField(db_column='LastOdometer', blank=True, null=True)  # Field name made lowercase.
    avlsdevice = models.CharField(db_column='AVLSDevice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purchaseinstitute = models.IntegerField(db_column='PurchaseInstitute', blank=True, null=True)  # Field name made lowercase.
    customertype = models.CharField(db_column='CustomerType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fixavg = models.FloatField(db_column='FixAvg')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
    vltdcertificateno = models.CharField(db_column='VLTDCertificateNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vltdcertificatedate = models.DateField(db_column='VLTDCertificateDate', blank=True, null=True)  # Field name made lowercase.
    isavailable = models.BooleanField(db_column='IsAvailable', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
    entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
    editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MTN_BusInformation'



class OprSchedulingdetailstrip(models.Model):
    schedulingdetailstripid = models.AutoField(db_column='SchedulingDetailsTripId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
    scheduleid = models.IntegerField(db_column='ScheduleId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
    scheduletripid = models.IntegerField(db_column='ScheduleTripId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
    schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId', db_comment='Foreign Key')  # Field name made lowercase.
    businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    astarttime = models.CharField(db_column='AStartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aendtime = models.CharField(db_column='AEndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fromstage = models.CharField(db_column='FromStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tostage = models.CharField(db_column='ToStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distanceinkm = models.FloatField(db_column='DistanceInKM', blank=True, null=True)  # Field name made lowercase.
    adistanceinkm = models.FloatField(db_column='ADistanceInKM', blank=True, null=True)  # Field name made lowercase.
    isdead = models.BooleanField(db_column='IsDead', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
    entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
    editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
    editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
    islost = models.BooleanField(db_column='IsLost')  # Field name made lowercase.
    isbuschange = models.BooleanField(db_column='IsBusChange', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.
    isshort = models.BooleanField(db_column='isShort', blank=True, null=True)  # Field name made lowercase.
    shortkm = models.FloatField(db_column='ShortKM', blank=True, null=True)  # Field name made lowercase.
    isdiversion = models.BooleanField(db_column='IsDiversion', blank=True, null=True)  # Field name made lowercase.
    diversionkm = models.FloatField(db_column='DiversionKM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPR_SchedulingDetailsTrip'