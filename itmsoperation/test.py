# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.contrib.gis.db import models


# class ConfigBranchmaster(models.Model):
#     branchid = models.AutoField(db_column='BranchId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey('ConfigCompanymaster', models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     branchname = models.CharField(db_column='BranchName', max_length=100)  # Field name made lowercase.
#     branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
#     contactno = models.IntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     emailid = models.CharField(db_column='EmailId', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
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
#         db_table = 'CONFIG_BranchMaster'


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


# class ConfigConfigration(models.Model):
#     configationid = models.IntegerField(db_column='ConfigationId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     organisationid = models.ForeignKey('ConfigOrganisationmaster', models.DO_NOTHING, db_column='OrganisationId')  # Field name made lowercase.
#     iscategory = models.BooleanField(db_column='IsCategory', blank=True, null=True)  # Field name made lowercase.
#     isdivision = models.BooleanField(db_column='IsDivision', blank=True, null=True)  # Field name made lowercase.
#     isemployeetype = models.BooleanField(db_column='IsEmployeeType', blank=True, null=True)  # Field name made lowercase.
#     isgrade = models.BooleanField(db_column='IsGrade', blank=True, null=True)  # Field name made lowercase.
#     isproject = models.BooleanField(db_column='IsProject', blank=True, null=True)  # Field name made lowercase.
#     isunit = models.BooleanField(db_column='IsUnit', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CONFIG_Configration'


# class ConfigNotificationdetails(models.Model):
#     notificationdetailsid = models.IntegerField(db_column='NotificationDetailsId', primary_key=True)  # Field name made lowercase.
#     notificationmasterid = models.ForeignKey('ConfigNotificationmaster', models.DO_NOTHING, db_column='NotificationMasterId')  # Field name made lowercase.
#     notificationtype = models.CharField(db_column='NotificationType', max_length=500)  # Field name made lowercase.
#     sender = models.CharField(db_column='Sender', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     senderid = models.IntegerField(db_column='SenderId')  # Field name made lowercase.
#     recipient = models.CharField(db_column='Recipient', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     recipientid = models.IntegerField(db_column='RecipientId')  # Field name made lowercase.
#     userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     mobileno = models.CharField(db_column='MobileNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     template = models.TextField(db_column='Template')  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CONFIG_NotificationDetails'


# class ConfigNotificationmaster(models.Model):
#     notificationmasterid = models.IntegerField(db_column='NotificationMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     moduleid = models.CharField(db_column='ModuleId', max_length=200)  # Field name made lowercase.
#     notificationname = models.CharField(db_column='NotificationName', max_length=200)  # Field name made lowercase.
#     createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
#     isemail = models.BooleanField(db_column='IsEmail')  # Field name made lowercase.
#     iswhatsapp = models.BooleanField(db_column='IsWhatsApp')  # Field name made lowercase.
#     isnotification = models.BooleanField(db_column='IsNotification')  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CONFIG_NotificationMaster'


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


# class CoreBankmaster(models.Model):
#     bankmasterid = models.AutoField(db_column='BankMasterId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     bankname = models.CharField(db_column='BankName', max_length=150)  # Field name made lowercase.
#     branchname = models.CharField(db_column='BranchName', max_length=150)  # Field name made lowercase.
#     branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
#     ifsccode = models.CharField(db_column='IFSCCode', max_length=100)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'CORE_BankMaster'


# class CoreFinancialyear(models.Model):
#     financialyearid = models.AutoField(db_column='FinancialYearId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     years = models.CharField(db_column='Years', max_length=25)  # Field name made lowercase.
#     yearstartdate = models.DateField(db_column='YearStartDate')  # Field name made lowercase.
#     yearenddate = models.DateField(db_column='YearEndDate')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'CORE_FinancialYear'


# class CoreCommon(models.Model):
#     commonid = models.AutoField(db_column='CommonId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
#     value = models.CharField(db_column='Value', max_length=50)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     module = models.CharField(db_column='Module', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Core_Common'


# class EmpBackgroundcheck(models.Model):
#     backgroundcheckid = models.AutoField(db_column='BackgroundCheckId', primary_key=True)  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId')  # Field name made lowercase.
#     referencename = models.CharField(db_column='ReferenceName', max_length=200)  # Field name made lowercase.
#     organizationname = models.CharField(db_column='OrganizationName', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     relation = models.CharField(db_column='Relation', max_length=100)  # Field name made lowercase.
#     designation = models.CharField(db_column='Designation', max_length=200)  # Field name made lowercase.
#     department = models.CharField(db_column='Department', max_length=200)  # Field name made lowercase.
#     mobileno = models.CharField(db_column='MobileNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     emailid = models.CharField(db_column='EmailId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_BackgroundCheck'


# class EmpBank(models.Model):
#     bankid = models.AutoField(db_column='BankId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey('EmpEmployeemaster', models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
#     branchname = models.CharField(db_column='BranchName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ifsccode = models.CharField(db_column='IFSCCode', max_length=50)  # Field name made lowercase.
#     accountnumber = models.CharField(db_column='AccountNumber', max_length=50)  # Field name made lowercase.
#     gratuitycode = models.CharField(db_column='GratuityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     panno = models.CharField(db_column='PANNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aadharno = models.CharField(db_column='AadharNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pt = models.CharField(db_column='PT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ispf = models.BooleanField(db_column='IsPF')  # Field name made lowercase.
#     pfoldversion = models.CharField(db_column='PFOldVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fpf = models.CharField(db_column='FPF', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     vpf = models.CharField(db_column='VPF', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pfnewversion = models.CharField(db_column='PFNewVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pfjoindate = models.DateField(db_column='PFJoinDate', blank=True, null=True)  # Field name made lowercase.
#     pfremark = models.CharField(db_column='PFRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     isesic = models.BooleanField(db_column='IsESIC')  # Field name made lowercase.
#     esicoldversion = models.CharField(db_column='ESICOldVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esicnewversion = models.CharField(db_column='ESICNewVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esiccode = models.CharField(db_column='ESICCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esicname = models.CharField(db_column='ESICName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esicremark = models.CharField(db_column='ESICRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     cancelledchequepath = models.CharField(db_column='CancelledChequePath', max_length=500, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Bank'


# class EmpCategory(models.Model):
#     categoryid = models.AutoField(db_column='CategoryId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     categoryname = models.CharField(db_column='CategoryName', max_length=100)  # Field name made lowercase.
#     categorycode = models.CharField(db_column='CategoryCode', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Category'


# class EmpClearance(models.Model):
#     clearanceid = models.AutoField(db_column='ClearanceId', primary_key=True)  # Field name made lowercase.
#     clearancemasterid = models.IntegerField(db_column='ClearanceMasterId')  # Field name made lowercase.
#     clearancedetailsid = models.IntegerField(db_column='ClearanceDetailsId')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId')  # Field name made lowercase.
#     comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     approverid = models.IntegerField(db_column='ApproverId')  # Field name made lowercase.
#     approvelstatus = models.CharField(db_column='ApprovelStatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Clearance'


# class EmpClearancedetails(models.Model):
#     clearancedetailsid = models.AutoField(db_column='ClearanceDetailsId', primary_key=True)  # Field name made lowercase.
#     clearancemasterid = models.IntegerField(db_column='ClearanceMasterId')  # Field name made lowercase.
#     designationid = models.IntegerField(db_column='DesignationId')  # Field name made lowercase.
#     heads = models.CharField(db_column='Heads', max_length=500)  # Field name made lowercase.
#     approverid = models.IntegerField(db_column='ApproverId')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ClearanceDetails'


# class EmpClearancemaster(models.Model):
#     clearancemasterid = models.AutoField(db_column='ClearanceMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     departments = models.CharField(db_column='Departments', max_length=500)  # Field name made lowercase.
#     approverid = models.IntegerField(db_column='ApproverId')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ClearanceMaster'


# class EmpContact(models.Model):
#     contactid = models.AutoField(db_column='ContactId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey('EmpEmployeemaster', models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     residentialno = models.CharField(db_column='ResidentialNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     personalno = models.CharField(db_column='PersonalNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     officeno = models.CharField(db_column='OfficeNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     mobileno = models.CharField(db_column='MobileNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     alternatemobileno = models.CharField(db_column='AlternateMobileNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     alternateemail = models.CharField(db_column='AlternateEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     permanentaddress = models.CharField(db_column='PermanentAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     temporaryaddress = models.CharField(db_column='TemporaryAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     district = models.CharField(db_column='District', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     town = models.CharField(db_column='Town', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     pincode = models.IntegerField(db_column='PINCode', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Contact'


# class EmpDepartment(models.Model):
#     departmentid = models.AutoField(db_column='DepartmentId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     departmentname = models.CharField(db_column='DepartmentName', max_length=50)  # Field name made lowercase.
#     departmentcode = models.CharField(db_column='DepartmentCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Department'


# class EmpDesignation(models.Model):
#     designationid = models.AutoField(db_column='DesignationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     designationname = models.CharField(db_column='DesignationName', max_length=50)  # Field name made lowercase.
#     designationcode = models.CharField(db_column='DesignationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Designation'


# class EmpDivision(models.Model):
#     divisionid = models.AutoField(db_column='DivisionId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     divisionname = models.CharField(db_column='DivisionName', max_length=50)  # Field name made lowercase.
#     divisioncode = models.CharField(db_column='DivisionCode', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Division'


# class EmpDocument(models.Model):
#     documentid = models.AutoField(db_column='DocumentId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey('EmpEmployeemaster', models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     documentname = models.CharField(db_column='DocumentName', max_length=100, db_comment='Included in Add form')  # Field name made lowercase.
#     documenttype = models.CharField(db_column='DocumentType', max_length=50, db_comment='Included in Add form')  # Field name made lowercase.
#     path = models.CharField(db_column='Path', max_length=256)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True, db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Document'


# class EmpEmployeemaster(models.Model):
#     employeeid = models.AutoField(db_column='EmployeeId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     employeecode = models.CharField(db_column='EmployeeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     indexno = models.IntegerField(db_column='IndexNo', unique=True)  # Field name made lowercase.
#     title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
#     fname = models.CharField(db_column='FName', max_length=300)  # Field name made lowercase.
#     mname = models.CharField(db_column='MName', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     lname = models.CharField(db_column='LName', max_length=300)  # Field name made lowercase.
#     branchid = models.IntegerField(db_column='BranchId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     departmentid = models.IntegerField(db_column='DepartmentId', db_comment='Foreign Key')  # Field name made lowercase.
#     alt_departmentid = models.IntegerField(db_column='Alt_DepartmentId', blank=True, null=True, db_comment='Stores DepartmentId if Employe')  # Field name made lowercase.
#     designationid = models.ForeignKey(EmpDesignation, models.DO_NOTHING, db_column='DesignationId', db_comment='Foreign Key')  # Field name made lowercase.
#     alt_designationid = models.IntegerField(db_column='Alt_DesignationId', blank=True, null=True, db_comment='Stores DesignatioId if Employe')  # Field name made lowercase.
#     employeetypeid = models.ForeignKey('EmpEmployeetype', models.DO_NOTHING, db_column='EmployeeTypeId', db_comment='Foreign Key')  # Field name made lowercase.
#     categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True, db_comment='Used in EmployeeMaster for ide')  # Field name made lowercase.
#     divisionid = models.IntegerField(db_column='DivisionId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     unitid = models.IntegerField(db_column='UnitId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=20)  # Field name made lowercase.
#     dateofjoining = models.DateField(db_column='DateOfJoining')  # Field name made lowercase.
#     dateofresignation_offered = models.DateField(db_column='DateOfResignation_Offered', blank=True, null=True)  # Field name made lowercase.
#     dateofresignation_confirm = models.DateField(db_column='DateOfResignation_Confirm', blank=True, null=True)  # Field name made lowercase.
#     lastworkingdate = models.DateField(db_column='LastWorkingDate', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     freeze = models.BooleanField(db_column='Freeze', blank=True, null=True)  # Field name made lowercase.
#     freezedate = models.DateField(db_column='FreezeDate', blank=True, null=True)  # Field name made lowercase.
#     freezereason = models.CharField(db_column='FreezeReason', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     imagepath = models.CharField(db_column='ImagePath', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Storing PreJoinEmployeeId')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     seniorid = models.IntegerField(db_column='SeniorId', blank=True, null=True)  # Field name made lowercase.
#     prejoiningemployeeid = models.IntegerField(db_column='PreJoiningEmployeeId', blank=True, null=True)  # Field name made lowercase.
#     probationperiod = models.IntegerField(db_column='ProbationPeriod', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_EmployeeMaster'


# class EmpEmployeemastertemp(models.Model):
#     employeeid = models.AutoField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     employeecode = models.CharField(db_column='EmployeeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     indexno = models.IntegerField(db_column='IndexNo', blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fname = models.CharField(db_column='FName', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     mname = models.CharField(db_column='MName', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     lname = models.CharField(db_column='LName', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
#     gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
#     departmentid = models.IntegerField(db_column='DepartmentId', blank=True, null=True)  # Field name made lowercase.
#     alt_departmentid = models.IntegerField(db_column='Alt_DepartmentId', blank=True, null=True)  # Field name made lowercase.
#     designationid = models.IntegerField(db_column='DesignationId', blank=True, null=True)  # Field name made lowercase.
#     alt_designationid = models.IntegerField(db_column='Alt_DesignationId', blank=True, null=True)  # Field name made lowercase.
#     employeetypeid = models.IntegerField(db_column='EmployeeTypeId', blank=True, null=True)  # Field name made lowercase.
#     categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
#     divisionid = models.IntegerField(db_column='DivisionId', blank=True, null=True)  # Field name made lowercase.
#     unitid = models.IntegerField(db_column='UnitId', blank=True, null=True)  # Field name made lowercase.
#     dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ishandicapped = models.BooleanField(db_column='IsHandicapped', blank=True, null=True)  # Field name made lowercase.
#     dateofjoining = models.DateField(db_column='DateOfJoining', blank=True, null=True)  # Field name made lowercase.
#     dateofresignation_offered = models.DateField(db_column='DateOfResignation_Offered', blank=True, null=True)  # Field name made lowercase.
#     dateofresignation_confirm = models.DateField(db_column='DateOfResignation_Confirm', blank=True, null=True)  # Field name made lowercase.
#     lastworkingdate = models.DateField(db_column='LastWorkingDate', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     freeze = models.BooleanField(db_column='Freeze', blank=True, null=True)  # Field name made lowercase.
#     freezedate = models.DateField(db_column='FreezeDate', blank=True, null=True)  # Field name made lowercase.
#     freezereason = models.CharField(db_column='FreezeReason', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     imagepath = models.CharField(db_column='ImagePath', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     prejoiningemployeeid = models.IntegerField(db_column='PreJoiningEmployeeId', blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     seniorid = models.IntegerField(db_column='SeniorId', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_EmployeeMasterTemp'


# class EmpEmployeetransport(models.Model):
#     transportemployeeid = models.AutoField(db_column='TransportEmployeeId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     smartcard = models.DateField(db_column='SmartCard', blank=True, null=True)  # Field name made lowercase.
#     icard = models.DateField(db_column='ICard', blank=True, null=True)  # Field name made lowercase.
#     busno = models.CharField(db_column='BusNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     act = models.CharField(db_column='Act', max_length=50, blank=True, null=True, db_comment='MotorVehical, Scocks, Factory')  # Field name made lowercase.
#     dispensary = models.CharField(db_column='Dispensary', max_length=50, blank=True, null=True, db_comment='Medical Dispensories')  # Field name made lowercase.
#     drivinglicence = models.CharField(db_column='DrivingLicence', max_length=50)  # Field name made lowercase.
#     dlissuedate = models.DateField(db_column='DLIssueDate', blank=True, null=True, db_comment='Driving Licance Issue')  # Field name made lowercase.
#     dlrenewaldate = models.DateField(db_column='DLRenewalDate', blank=True, null=True, db_comment='Driving Licance')  # Field name made lowercase.
#     dlrenewalstatus = models.CharField(db_column='DLRenewalStatus', max_length=50, blank=True, null=True, db_comment='Renew in process etc..')  # Field name made lowercase.
#     batchno = models.CharField(db_column='BatchNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     batchrenewaldate = models.DateField(db_column='BatchRenewalDate', blank=True, null=True, db_comment='Batch Renewal Date')  # Field name made lowercase.
#     isresigned = models.BooleanField(db_column='IsResigned', db_comment='Not Resigned')  # Field name made lowercase.
#     resigndate = models.DateField(db_column='ResignDate', blank=True, null=True, db_comment='Resign Date')  # Field name made lowercase.
#     resignedreason = models.CharField(db_column='ResignedReason', max_length=500, blank=True, null=True, db_comment='Reason for Resignation')  # Field name made lowercase.
#     resignedlsdate = models.DateField(db_column='ResignedLSDate', blank=True, null=True, db_comment='Date of Resigning Letter Submi')  # Field name made lowercase.
#     relievingdate = models.DateField(db_column='RelievingDate', blank=True, null=True, db_comment='Date Of Relieving')  # Field name made lowercase.
#     transferdate = models.DateField(db_column='TransferDate', blank=True, null=True)  # Field name made lowercase.
#     transferreason = models.CharField(db_column='TransferReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     documentpath = models.CharField(db_column='DocumentPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True, db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_EmployeeTransport'


# class EmpEmployeetype(models.Model):
#     employeetypeid = models.AutoField(db_column='EmployeeTypeId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companylid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanylId', db_comment='Foreign Key')  # Field name made lowercase.
#     employeetypes = models.CharField(db_column='EmployeeTypes', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_EmployeeType'


# class EmpExitinterview(models.Model):
#     exitinterviewid = models.AutoField(db_column='ExitInterviewId', primary_key=True)  # Field name made lowercase.
#     resignationid = models.IntegerField(db_column='ResignationId')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ExitInterview'


# class EmpExitinterviewquestion(models.Model):
#     exitinterviewquestionid = models.AutoField(db_column='ExitInterviewQuestionId', primary_key=True)  # Field name made lowercase.
#     exitinterviewid = models.IntegerField(db_column='ExitInterviewId')  # Field name made lowercase.
#     questionid = models.IntegerField(db_column='QuestionId', blank=True, null=True)  # Field name made lowercase.
#     answerid = models.IntegerField(db_column='AnswerId', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ExitInterviewQuestion'


# class EmpExitinterviewratings(models.Model):
#     exitinterviewratingsid = models.AutoField(db_column='ExitInterviewRatingsId', primary_key=True)  # Field name made lowercase.
#     exitinterviewid = models.IntegerField(db_column='ExitInterviewId')  # Field name made lowercase.
#     areasid = models.IntegerField(db_column='AreasId', blank=True, null=True)  # Field name made lowercase.
#     rating = models.CharField(db_column='Rating', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ratingexplanation = models.CharField(db_column='RatingExplanation', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ExitInterviewRatings'


# class EmpExitquestiondetails(models.Model):
#     exitquestiondetailsid = models.AutoField(db_column='ExitQuestionDetailsId', primary_key=True)  # Field name made lowercase.
#     exitquestionmasterid = models.IntegerField(db_column='ExitQuestionMasterId')  # Field name made lowercase.
#     options = models.CharField(db_column='Options', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ExitQuestionDetails'


# class EmpExitquestionmaster(models.Model):
#     exitquestionmasterid = models.AutoField(db_column='ExitQuestionMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     designationid = models.IntegerField(db_column='DesignationId', blank=True, null=True)  # Field name made lowercase.
#     questions = models.CharField(db_column='Questions', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ExitQuestionMaster'


# class EmpExitratingmaster(models.Model):
#     exitratingmasterid = models.AutoField(db_column='ExitRatingMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     designationid = models.IntegerField(db_column='DesignationId', blank=True, null=True)  # Field name made lowercase.
#     areas = models.CharField(db_column='Areas', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_ExitRatingMaster'


# class EmpExperience(models.Model):
#     experienceid = models.AutoField(db_column='ExperienceId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     fromdate = models.DateField(db_column='FromDate')  # Field name made lowercase.
#     todate = models.DateField(db_column='ToDate')  # Field name made lowercase.
#     industrytype = models.CharField(db_column='IndustryType', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     organization = models.CharField(db_column='Organization', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     designation = models.CharField(db_column='Designation', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Experience'


# class EmpFamilyrelation(models.Model):
#     familyrelationid = models.AutoField(db_column='FamilyRelationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     relationship = models.CharField(db_column='Relationship', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     rname = models.CharField(db_column='RName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     contactno = models.CharField(db_column='ContactNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
#     isemergency = models.BooleanField(db_column='IsEmergency', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_FamilyRelation'


# class EmpGrade(models.Model):
#     gradeid = models.AutoField(db_column='GradeId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Grade'


# class EmpHolidaymaster(models.Model):
#     holidaymasterid = models.AutoField(db_column='HolidayMasterId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     holidayname = models.CharField(db_column='HolidayName', max_length=100)  # Field name made lowercase.
#     date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_HolidayMaster'


# class EmpLanguage(models.Model):
#     languageid = models.AutoField(db_column='LanguageId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     languagemasterid = models.ForeignKey('EmpLanguagemaster', models.DO_NOTHING, db_column='LanguageMasterId', db_comment='Foreign Key')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     isread = models.BooleanField(db_column='IsRead')  # Field name made lowercase.
#     readproficiency = models.CharField(db_column='ReadProficiency', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     iswrite = models.BooleanField(db_column='IsWrite')  # Field name made lowercase.
#     writeproficiency = models.CharField(db_column='WriteProficiency', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isspeaking = models.BooleanField(db_column='IsSpeaking')  # Field name made lowercase.
#     speakingproficiency = models.CharField(db_column='SpeakingProficiency', max_length=50, blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Language'


# class EmpLanguagemaster(models.Model):
#     languagemasterid = models.AutoField(db_column='LanguageMasterId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_LanguageMaster'


# class EmpMedicalhistory(models.Model):
#     medicalhistoryid = models.AutoField(db_column='MedicalHistoryId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     hospital = models.CharField(db_column='Hospital', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     doctor = models.CharField(db_column='Doctor', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     registrationno = models.CharField(db_column='RegistrationNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dateofcertificate = models.DateField(db_column='DateOfCertificate', blank=True, null=True)  # Field name made lowercase.
#     documenturl = models.CharField(db_column='DocumentUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_MedicalHistory'


# class EmpNominee(models.Model):
#     employeenomineeid = models.AutoField(db_column='EmployeeNomineeId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     nomineename = models.CharField(db_column='NomineeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     nomineetype = models.CharField(db_column='NomineeType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nomineerelation = models.CharField(db_column='NomineeRelation', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nomineedate = models.DateField(db_column='NomineeDate', blank=True, null=True)  # Field name made lowercase.
#     isnomineeminor = models.BooleanField(db_column='IsNomineeMinor', blank=True, null=True)  # Field name made lowercase.
#     nomineebirthdate = models.DateField(db_column='NomineeBirthDate', blank=True, null=True)  # Field name made lowercase.
#     pfpercentage = models.FloatField(db_column='PFPercentage', blank=True, null=True)  # Field name made lowercase.
#     nomineeaadharno = models.CharField(db_column='NomineeAadharNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     nomineestayingwith = models.CharField(db_column='NomineeStayingWith', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     guardianname = models.CharField(db_column='GuardianName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     guardianaddress = models.CharField(db_column='GuardianAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     nomineedescription = models.CharField(db_column='NomineeDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     nomineeof = models.CharField(db_column='NomineeOf', max_length=100, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
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
#         db_table = 'EMP_Nominee'


# class EmpOfferletter(models.Model):
#     offerletterid = models.AutoField(db_column='OfferLetterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     offerletterdate = models.DateTimeField(db_column='OfferLetterDate')  # Field name made lowercase.
#     prejoiningemployeeid = models.ForeignKey('EmpPrejoiningemployee', models.DO_NOTHING, db_column='PreJoiningEmployeeId')  # Field name made lowercase.
#     departmentid = models.ForeignKey(EmpDepartment, models.DO_NOTHING, db_column='DepartmentId')  # Field name made lowercase.
#     designationid = models.ForeignKey(EmpDesignation, models.DO_NOTHING, db_column='DesignationId')  # Field name made lowercase.
#     doj = models.DateTimeField(db_column='DOJ')  # Field name made lowercase.
#     jobdescription = models.CharField(db_column='JobDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     probationperiod = models.CharField(db_column='ProbationPeriod', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     emphandbookpath = models.CharField(db_column='EmpHandbookPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     basic = models.FloatField(db_column='Basic')  # Field name made lowercase.
#     hra = models.FloatField(db_column='HRA')  # Field name made lowercase.
#     travalallowance = models.FloatField(db_column='TravalAllowance')  # Field name made lowercase.
#     specialallowance = models.FloatField(db_column='SpecialAllowance')  # Field name made lowercase.
#     leavetravalallowance = models.FloatField(db_column='LeaveTravalAllowance')  # Field name made lowercase.
#     fixedcomponent = models.FloatField(db_column='FixedComponent')  # Field name made lowercase.
#     variablecomponent = models.FloatField(db_column='VariableComponent')  # Field name made lowercase.
#     ctc = models.FloatField(db_column='CTC')  # Field name made lowercase.
#     employeecc = models.CharField(db_column='EmployeeCC', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     validuptodate = models.DateTimeField(db_column='ValidUptoDate', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     requesteddoj = models.DateField(db_column='RequestedDOJ', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_OfferLetter'


# class EmpPersonalinformation(models.Model):
#     personalinformationid = models.AutoField(db_column='PersonalInformationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     altarnatename = models.CharField(db_column='AltarnateName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     nationality = models.CharField(db_column='Nationality', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     placeofbirth = models.CharField(db_column='PlaceOfBirth', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     passportno = models.CharField(db_column='PassportNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     religion = models.CharField(db_column='Religion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     maritalstatus = models.CharField(db_column='MaritalStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     numberofchildren = models.IntegerField(db_column='NumberOfChildren', blank=True, null=True)  # Field name made lowercase.
#     caste = models.CharField(db_column='Caste', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
#     weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
#     bloodgroup = models.CharField(db_column='BloodGroup', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     identificationmark = models.CharField(db_column='IdentificationMark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     isspeciallyable = models.BooleanField(db_column='IsSpeciallyAble', blank=True, null=True)  # Field name made lowercase.
#     specialitydescription = models.CharField(db_column='SpecialityDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     natureofspeciality = models.CharField(db_column='NatureOfSpeciality', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     residentialno = models.CharField(db_column='ResidentialNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     personalno = models.CharField(db_column='PersonalNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     officeno = models.CharField(db_column='OfficeNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     mobileno = models.CharField(db_column='MobileNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     alternatemobileno = models.CharField(db_column='AlternateMobileNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     alternateemail = models.CharField(db_column='AlternateEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     permanentaddress = models.CharField(db_column='PermanentAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     temporaryaddress = models.CharField(db_column='TemporaryAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     district = models.CharField(db_column='District', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     town = models.CharField(db_column='Town', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     pincode = models.IntegerField(db_column='PINCode', blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_PersonalInformation'


# class EmpPrejoinbank(models.Model):
#     prejoinbankid = models.AutoField(db_column='PreJoinBankId', primary_key=True)  # Field name made lowercase.
#     prejoiningemployeeid = models.IntegerField(db_column='PreJoiningEmployeeId')  # Field name made lowercase.
#     bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
#     branchname = models.CharField(db_column='BranchName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
#     ifsccode = models.CharField(db_column='IFSCCode', max_length=50)  # Field name made lowercase.
#     accountnumber = models.CharField(db_column='AccountNumber', max_length=50)  # Field name made lowercase.
#     panno = models.CharField(db_column='PANNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aadharno = models.CharField(db_column='AadharNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pt = models.CharField(db_column='PT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ispf = models.BooleanField(db_column='IsPF')  # Field name made lowercase.
#     pfoldversion = models.CharField(db_column='PFOldVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fpf = models.CharField(db_column='FPF', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     vpf = models.CharField(db_column='VPF', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pfnewversion = models.CharField(db_column='PFNewVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pfjoindate = models.DateField(db_column='PFJoinDate', blank=True, null=True)  # Field name made lowercase.
#     pfremark = models.CharField(db_column='PFRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     isesic = models.BooleanField(db_column='IsESIC')  # Field name made lowercase.
#     esicoldversion = models.CharField(db_column='ESICOldVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esicnewversion = models.CharField(db_column='ESICNewVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esiccode = models.CharField(db_column='ESICCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esicname = models.CharField(db_column='ESICName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     esicremark = models.CharField(db_column='ESICRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_PreJoinBank'


# class EmpPrejoindocument(models.Model):
#     prejoindocumentid = models.AutoField(db_column='PreJoinDocumentId', primary_key=True)  # Field name made lowercase.
#     prejoiningemployeeid = models.IntegerField(db_column='PreJoiningEmployeeId')  # Field name made lowercase.
#     documentname = models.CharField(db_column='DocumentName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     requireddocumentid = models.ForeignKey('EmpRequireddocument', models.DO_NOTHING, db_column='RequiredDocumentId')  # Field name made lowercase.
#     documenttype = models.CharField(db_column='DocumentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     path = models.CharField(db_column='Path', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_PreJoinDocument'


# class EmpPrejoinqualification(models.Model):
#     prejoinqualificationid = models.AutoField(db_column='PreJoinQualificationId', primary_key=True)  # Field name made lowercase.
#     prejoiningemployeeid = models.IntegerField(db_column='PreJoiningEmployeeId')  # Field name made lowercase.
#     degree = models.CharField(db_column='Degree', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     course = models.CharField(db_column='Course', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     institute = models.CharField(db_column='Institute', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     university = models.CharField(db_column='University', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     specification = models.CharField(db_column='Specification', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     duration = models.FloatField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
#     passingyear = models.DateField(db_column='PassingYear', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_PreJoinQualification'


# class EmpPrejoiningemployee(models.Model):
#     prejoiningemployeeid = models.AutoField(db_column='PreJoiningEmployeeId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
#     fname = models.CharField(db_column='FName', max_length=300)  # Field name made lowercase.
#     mname = models.CharField(db_column='MName', max_length=300)  # Field name made lowercase.
#     lname = models.CharField(db_column='LName', max_length=300)  # Field name made lowercase.
#     preemployeecode = models.CharField(db_column='PreEmployeeCode', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     designationid = models.IntegerField(db_column='DesignationId')  # Field name made lowercase.
#     departmentid = models.IntegerField(db_column='DepartmentId', blank=True, null=True)  # Field name made lowercase.
#     dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=20)  # Field name made lowercase.
#     mailid = models.CharField(db_column='MailId', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     mobileno = models.CharField(db_column='MobileNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ishandicapped = models.BooleanField(db_column='IsHandicapped', blank=True, null=True)  # Field name made lowercase.
#     nationality = models.CharField(db_column='Nationality', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     drivinglicence = models.CharField(db_column='DrivingLicence', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     placeofbirth = models.CharField(db_column='PlaceOfBirth', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     maritalstatus = models.CharField(db_column='MaritalStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     imagepath = models.CharField(db_column='ImagePath', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
#     employeestatus = models.CharField(db_column='EmployeeStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     stage = models.CharField(db_column='Stage', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     statusremark = models.CharField(db_column='StatusRemark', max_length=4000, blank=True, null=True)  # Field name made lowercase.
#     empentrymacid = models.CharField(db_column='EmpEntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tempemployeeid = models.IntegerField(db_column='TempEmployeeId', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_PreJoiningEmployee'


# class EmpPresentation(models.Model):
#     presentationid = models.AutoField(db_column='PresentationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     presentationdate = models.DateField(db_column='PresentationDate')  # Field name made lowercase.
#     presentationlevel = models.CharField(db_column='PresentationLevel', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     presentationtype = models.CharField(db_column='PresentationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     presentationtopic = models.CharField(db_column='PresentationTopic', max_length=100, db_comment='Included in Add form')  # Field name made lowercase.
#     presentationinstitute = models.CharField(db_column='PresentationInstitute', max_length=50)  # Field name made lowercase.
#     presentationcity = models.CharField(db_column='PresentationCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     presentationdescription = models.CharField(db_column='PresentationDescription', max_length=500, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True, db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Presentation'


# class EmpProject(models.Model):
#     projectid = models.AutoField(db_column='ProjectId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     projectmasterid = models.ForeignKey('EmpProjectmaster', models.DO_NOTHING, db_column='ProjectMasterId', db_comment='Foreign Key')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId')  # Field name made lowercase.
#     guidedby = models.CharField(db_column='GuidedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     assigndate = models.DateField(db_column='AssignDate', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     documentname = models.CharField(db_column='DocumentName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     documentpath = models.CharField(db_column='DocumentPath', max_length=100, blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Project'


# class EmpProjectmaster(models.Model):
#     projectmasterid = models.AutoField(db_column='ProjectMasterId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     subject = models.CharField(db_column='Subject', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     organisation = models.CharField(db_column='Organisation', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
#     enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_ProjectMaster'


# class EmpQualification(models.Model):
#     qualificationid = models.AutoField(db_column='QualificationId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     degree = models.CharField(db_column='Degree', max_length=100)  # Field name made lowercase.
#     course = models.CharField(db_column='Course', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     institute = models.CharField(db_column='Institute', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     university = models.CharField(db_column='University', max_length=100)  # Field name made lowercase.
#     specification = models.CharField(db_column='Specification', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     duration = models.FloatField(db_column='Duration')  # Field name made lowercase.
#     passingyear = models.DateField(db_column='PassingYear')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Qualification'


# class EmpRequireddocument(models.Model):
#     requireddocumentid = models.AutoField(db_column='RequiredDocumentId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     designationid = models.ForeignKey(EmpDesignation, models.DO_NOTHING, db_column='DesignationId')  # Field name made lowercase.
#     documentname = models.CharField(db_column='DocumentName', max_length=100)  # Field name made lowercase.
#     ismandatory = models.BooleanField(db_column='IsMandatory', blank=True, null=True)  # Field name made lowercase.
#     uploadinstruction = models.CharField(db_column='UploadInstruction', max_length=500, blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_RequiredDocument'


# class EmpResignation(models.Model):
#     resignationid = models.AutoField(db_column='ResignationId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId')  # Field name made lowercase.
#     departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
#     designationid = models.IntegerField(db_column='DesignationId', blank=True, null=True)  # Field name made lowercase.
#     seniorid = models.IntegerField(db_column='SeniorId')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
#     resignationdate = models.DateField(db_column='ResignationDate')  # Field name made lowercase.
#     relivingdate = models.DateField(db_column='RelivingDate', blank=True, null=True)  # Field name made lowercase.
#     lastworkingdate = models.CharField(db_column='LastWorkingDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     resignationdescription = models.CharField(db_column='ResignationDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Resignation'


# class EmpSkillmaster(models.Model):
#     skillmasterid = models.AutoField(db_column='SkillMasterId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True, db_comment='Extra Fields')  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_SkillMaster'


# class EmpSkills(models.Model):
#     skillsid = models.AutoField(db_column='SkillsId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     skillmasterid = models.ForeignKey(EmpSkillmaster, models.DO_NOTHING, db_column='SkillMasterId', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Skills'


# class EmpSuspend(models.Model):
#     suspendid = models.AutoField(db_column='SuspendId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
#     enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
#     suspendremark = models.CharField(db_column='SuspendRemark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     rejoinremark = models.CharField(db_column='RejoinRemark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'EMP_Suspend'


# class EmpUnit(models.Model):
#     unitid = models.AutoField(db_column='UnitId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     unitname = models.CharField(db_column='UnitName', max_length=100)  # Field name made lowercase.
#     unitcode = models.CharField(db_column='UnitCode', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Unit'


# class EmpWorkshop(models.Model):
#     workshopid = models.AutoField(db_column='WorkshopId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     employeeid = models.IntegerField(db_column='EmployeeId', db_comment='Foreign Key')  # Field name made lowercase.
#     organizername = models.CharField(db_column='OrganizerName', max_length=100)  # Field name made lowercase.
#     organizordepartment = models.CharField(db_column='OrganizorDepartment', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=50)  # Field name made lowercase.
#     venue = models.CharField(db_column='Venue', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     date = models.DateField(db_column='Date')  # Field name made lowercase.
#     subject = models.CharField(db_column='Subject', max_length=50)  # Field name made lowercase.
#     specilization = models.CharField(db_column='Specilization', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     fundedby = models.CharField(db_column='FundedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'EMP_Workshop'


# class Errorlogforkmssummery(models.Model):
#     errorlogid = models.IntegerField(db_column='ErrorLogId', primary_key=True)  # Field name made lowercase.
#     schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId', blank=True, null=True)  # Field name made lowercase.
#     errormessage = models.CharField(db_column='ErrorMessage', max_length=4000, blank=True, null=True)  # Field name made lowercase.
#     errorseverity = models.IntegerField(db_column='ErrorSeverity', blank=True, null=True)  # Field name made lowercase.
#     errorstate = models.IntegerField(db_column='ErrorState', blank=True, null=True)  # Field name made lowercase.
#     errordatetime = models.DateTimeField(db_column='ErrorDateTime', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ErrorLogForKMSSummery'


# class Errorlogfortrigger(models.Model):
#     errorlogid = models.AutoField(db_column='ErrorLogId', primary_key=True)  # Field name made lowercase.
#     schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId', blank=True, null=True)  # Field name made lowercase.
#     errormessage = models.CharField(db_column='ErrorMessage', max_length=4000, blank=True, null=True)  # Field name made lowercase.
#     errorseverity = models.IntegerField(db_column='ErrorSeverity', blank=True, null=True)  # Field name made lowercase.
#     errorstate = models.IntegerField(db_column='ErrorState', blank=True, null=True)  # Field name made lowercase.
#     errordatetime = models.DateTimeField(db_column='ErrorDateTime', blank=True, null=True)  # Field name made lowercase.
#     operationtype = models.CharField(db_column='OperationType', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ErrorLogForTrigger'


# class InvApprovaldetails(models.Model):
#     approvaldetailsid = models.AutoField(db_column='ApprovalDetailsId', primary_key=True)  # Field name made lowercase.
#     approvalid = models.ForeignKey('InvApprovalmaster', models.DO_NOTHING, db_column='ApprovalId')  # Field name made lowercase.
#     itemid = models.ForeignKey('InvItem', models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
#     approvalquantity = models.FloatField(db_column='ApprovalQuantity', blank=True, null=True)  # Field name made lowercase.
#     approvalrate = models.FloatField(db_column='ApprovalRate', blank=True, null=True)  # Field name made lowercase.
#     make = models.CharField(db_column='Make', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     unitid = models.ForeignKey('InvUnit', models.DO_NOTHING, db_column='UnitId', blank=True, null=True)  # Field name made lowercase.
#     istender = models.BooleanField(db_column='IsTender')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_ApprovalDetails'


# class InvApprovalmaster(models.Model):
#     approvalid = models.AutoField(db_column='ApprovalId', primary_key=True)  # Field name made lowercase.
#     indentid = models.ForeignKey('InvIndentmaster', models.DO_NOTHING, db_column='IndentId')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     approvalnumber = models.CharField(db_column='ApprovalNumber', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approvaldate = models.DateField(db_column='ApprovalDate', blank=True, null=True)  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', blank=True, null=True)  # Field name made lowercase.
#     approvalstatus = models.CharField(db_column='ApprovalStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lastdate = models.DateField(db_column='LastDate', blank=True, null=True)  # Field name made lowercase.
#     tendornumber = models.CharField(db_column='TendorNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tendordate = models.DateField(db_column='TendorDate', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_ApprovalMaster'


# class InvCngapinvoice(models.Model):
#     cngapinvoiceid = models.AutoField(db_column='CNGAPInvoiceId', primary_key=True)  # Field name made lowercase.
#     supplierid = models.ForeignKey('InvFuelsuppliermaster', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
#     cnglfillingdetailsid = models.ForeignKey('InvCngfillingdetails', models.DO_NOTHING, db_column='CNGlFillingDetailsId')  # Field name made lowercase.
#     billnumber = models.CharField(db_column='BillNumber', max_length=50)  # Field name made lowercase.
#     billdate = models.DateField(db_column='BillDate')  # Field name made lowercase.
#     invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isapproved = models.BooleanField(db_column='IsApproved', blank=True, null=True)  # Field name made lowercase.
#     approvedperson = models.IntegerField(db_column='ApprovedPerson', blank=True, null=True)  # Field name made lowercase.
#     approvedmacid = models.CharField(db_column='ApprovedMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     cancellationremark = models.CharField(db_column='CancellationRemark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_CNGAPInvoice'


# class InvCngfillingdetails(models.Model):
#     cnglfillingdetailsid = models.AutoField(db_column='CNGlFillingDetailsId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
#     supplierid = models.ForeignKey('InvFuelsuppliermaster', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
#     dmnumber = models.IntegerField(db_column='DMNumber')  # Field name made lowercase.
#     businformationid = models.ForeignKey('MtnBusinformation', models.DO_NOTHING, db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     busnumber = models.CharField(db_column='BusNumber', max_length=50)  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
#     sheetno = models.IntegerField(db_column='SheetNo', blank=True, null=True)  # Field name made lowercase.
#     fillingdatetime = models.DateTimeField(db_column='FillingDateTime')  # Field name made lowercase.
#     cngpressureinatpump = models.CharField(db_column='CNGPressureInAtPump', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     kmreading = models.FloatField(db_column='KMReading', blank=True, null=True)  # Field name made lowercase.
#     cngpressureoutatpump = models.CharField(db_column='CNGPressureOutAtPump', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cngpumpstartmeterreading = models.CharField(db_column='CNGPumpStartMeterReading', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cngpumpclosingmeterreading = models.CharField(db_column='CNGPumpClosingMeterReading', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cngfilledinkg = models.FloatField(db_column='CNGFilledInKg', blank=True, null=True)  # Field name made lowercase.
#     deadkm = models.FloatField(db_column='DeadKM', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_CNGFillingDetails'


# class InvCategory(models.Model):
#     categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     groupid = models.ForeignKey('InvGroup', models.DO_NOTHING, db_column='GroupId')  # Field name made lowercase.
#     categoryname = models.CharField(db_column='CategoryName', max_length=50)  # Field name made lowercase.
#     categorycode = models.CharField(db_column='CategoryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     startno = models.IntegerField(db_column='StartNo', blank=True, null=True)  # Field name made lowercase.
#     endno = models.IntegerField(db_column='EndNo', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_Category'


# class InvDieselapinvoice(models.Model):
#     dieselapinvoiceid = models.AutoField(db_column='DieselAPInvoiceId', primary_key=True)  # Field name made lowercase.
#     supplierid = models.ForeignKey('InvFuelsuppliermaster', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
#     dieselfillingdetailsid = models.ForeignKey('InvDieselfillingdetails', models.DO_NOTHING, db_column='DieselFillingDetailsId')  # Field name made lowercase.
#     billnumber = models.CharField(db_column='BillNumber', max_length=50)  # Field name made lowercase.
#     billdate = models.DateField(db_column='BillDate')  # Field name made lowercase.
#     invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isapproved = models.BooleanField(db_column='IsApproved', blank=True, null=True)  # Field name made lowercase.
#     approvedperson = models.IntegerField(db_column='ApprovedPerson', blank=True, null=True)  # Field name made lowercase.
#     approvedmacid = models.CharField(db_column='ApprovedMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     cancellationremark = models.CharField(db_column='CancellationRemark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_DieselAPInvoice'
#         unique_together = (('dieselfillingdetailsid', 'isactive'),)


# class InvDieselfillingdetails(models.Model):
#     dieselfillingdetailsid = models.AutoField(db_column='DieselFillingDetailsId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
#     supplierid = models.ForeignKey('InvFuelsuppliermaster', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
#     dmnumber = models.IntegerField(db_column='DMNumber')  # Field name made lowercase.
#     businformationid = models.ForeignKey('MtnBusinformation', models.DO_NOTHING, db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     busnumber = models.CharField(db_column='BusNumber', max_length=50)  # Field name made lowercase.
#     reading = models.CharField(db_column='Reading', max_length=50)  # Field name made lowercase.
#     quantity = models.DecimalField(db_column='Quantity', max_digits=18, decimal_places=2)  # Field name made lowercase.
#     rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=2)  # Field name made lowercase.
#     sheetno = models.IntegerField(db_column='SheetNo', blank=True, null=True)  # Field name made lowercase.
#     fillingdatetime = models.DateTimeField(db_column='FillingDateTime')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_DieselFillingDetails'
#         unique_together = (('supplierid', 'busnumber', 'quantity', 'fillingdatetime'),)


# class InvFuelratemaster(models.Model):
#     fuelrateid = models.AutoField(db_column='FuelRateId', primary_key=True)  # Field name made lowercase.
#     supplierid = models.ForeignKey('InvFuelsuppliermaster', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
#     petrolrate = models.FloatField(db_column='PetrolRate')  # Field name made lowercase.
#     dieselrate = models.FloatField(db_column='DieselRate', blank=True, null=True)  # Field name made lowercase.
#     cngrate = models.FloatField(db_column='CNGRate', blank=True, null=True)  # Field name made lowercase.
#     applicabledate = models.DateField(db_column='ApplicableDate')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_FuelRateMaster'


# class InvFuelsuppliermaster(models.Model):
#     supplierid = models.AutoField(db_column='SupplierId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pincode = models.CharField(db_column='PinCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     phone1 = models.CharField(db_column='Phone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     phone2 = models.CharField(db_column='Phone2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     panno = models.CharField(db_column='PANNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_FuelSupplierMaster'


# class InvGrnbilldetails(models.Model):
#     grnbilldetailsid = models.AutoField(db_column='GRNBillDetailsId', primary_key=True)  # Field name made lowercase.
#     grnbillid = models.ForeignKey('InvGrnbillmaster', models.DO_NOTHING, db_column='GRNBillId')  # Field name made lowercase.
#     itemid = models.ForeignKey('InvItem', models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
#     wtavgrate = models.FloatField(db_column='WtAvgRate', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status')  # Field name made lowercase.
#     discountpercentage = models.FloatField(db_column='DiscountPercentage')  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount')  # Field name made lowercase.
#     gstpercentage = models.FloatField(db_column='GSTPercentage')  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount')  # Field name made lowercase.
#     tdsamount = models.FloatField(db_column='TDSAmount', blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_GRNBillDetails'


# class InvGrnbillmaster(models.Model):
#     grnbillid = models.AutoField(db_column='GRNBillId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     purchaseorderid = models.ForeignKey('InvPurchaseorder', models.DO_NOTHING, db_column='PurchaseOrderId')  # Field name made lowercase.
#     billnumber = models.CharField(db_column='BillNumber', max_length=50)  # Field name made lowercase.
#     billdate = models.DateField(db_column='BillDate')  # Field name made lowercase.
#     billinvoiceno = models.CharField(db_column='BillInvoiceNo', unique=True, max_length=50)  # Field name made lowercase.
#     voucherno = models.CharField(db_column='VoucherNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     voucherdate = models.DateField(db_column='VoucherDate', blank=True, null=True)  # Field name made lowercase.
#     billamount = models.FloatField(db_column='BillAmount')  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount')  # Field name made lowercase.
#     othertax = models.FloatField(db_column='OtherTax')  # Field name made lowercase.
#     othercharges = models.FloatField(db_column='OtherCharges')  # Field name made lowercase.
#     tdsamount = models.FloatField(db_column='TDSAmount', blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_GRNBillMaster'


# class InvGrnbillpaid(models.Model):
#     grnbillpaidid = models.AutoField(db_column='GRNBillPaidId', primary_key=True)  # Field name made lowercase.
#     grnbillid = models.ForeignKey(InvGrnbillmaster, models.DO_NOTHING, db_column='GRNBillId')  # Field name made lowercase.
#     paidamount = models.FloatField(db_column='PaidAmount', blank=True, null=True)  # Field name made lowercase.
#     paiddate = models.DateField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
#     iscash = models.BooleanField(db_column='IsCash', blank=True, null=True)  # Field name made lowercase.
#     chequenumber = models.CharField(db_column='ChequeNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ddnumber = models.CharField(db_column='DDNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     chequedate = models.DateField(db_column='ChequeDate', blank=True, null=True)  # Field name made lowercase.
#     bankid = models.IntegerField(db_column='BankId', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_GRNBillPaid'


# class InvGrndetails(models.Model):
#     grndetailsid = models.AutoField(db_column='GRNDetailsId', primary_key=True)  # Field name made lowercase.
#     grnid = models.ForeignKey('InvGrnmaster', models.DO_NOTHING, db_column='GRNId')  # Field name made lowercase.
#     itemid = models.ForeignKey('InvItem', models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
#     wtavgrate = models.FloatField(db_column='WtAvgRate', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status')  # Field name made lowercase.
#     itemnumber = models.CharField(db_column='ItemNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     warrantystartdate = models.DateTimeField(db_column='WarrantyStartDate', blank=True, null=True)  # Field name made lowercase.
#     warrantyenddate = models.DateTimeField(db_column='WarrantyEndDate', blank=True, null=True)  # Field name made lowercase.
#     guarantystartdate = models.DateTimeField(db_column='GuarantyStartDate', blank=True, null=True)  # Field name made lowercase.
#     guarantyenddate = models.DateTimeField(db_column='GuarantyEndDate', blank=True, null=True)  # Field name made lowercase.
#     isused = models.BooleanField(db_column='Isused', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.
#     entryperson = models.CharField(db_column='EntryPerson', max_length=50)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.CharField(db_column='EditPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_GRNDetails'


# class InvGrnmaster(models.Model):
#     grnid = models.AutoField(db_column='GRNId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     grnnumber = models.CharField(db_column='GRNNumber', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
#     grndate = models.DateField(db_column='GRNDate', blank=True, null=True)  # Field name made lowercase.
#     purchaseorderid = models.IntegerField(db_column='PurchaseOrderId', blank=True, null=True)  # Field name made lowercase.
#     dmnumber = models.CharField(db_column='DMNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     vehicalnumber = models.CharField(db_column='VehicalNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
#     cancellationremark = models.CharField(db_column='CancellationRemark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_GRNMaster'


# class InvGroup(models.Model):
#     groupid = models.AutoField(db_column='GroupId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     groupname = models.CharField(db_column='GroupName', max_length=50)  # Field name made lowercase.
#     groupcode = models.CharField(db_column='GroupCode', unique=True, max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_Group'


# class InvIndentdetails(models.Model):
#     indentdetailsid = models.AutoField(db_column='IndentDetailsId', primary_key=True)  # Field name made lowercase.
#     indentid = models.ForeignKey('InvIndentmaster', models.DO_NOTHING, db_column='IndentId')  # Field name made lowercase.
#     itemid = models.ForeignKey('InvItem', models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
#     userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
#     unitid = models.ForeignKey('InvUnit', models.DO_NOTHING, db_column='UnitId', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_IndentDetails'


# class InvIndentmaster(models.Model):
#     indentid = models.AutoField(db_column='IndentId', primary_key=True)  # Field name made lowercase.
#     financialyearid = models.ForeignKey(CoreFinancialyear, models.DO_NOTHING, db_column='FinancialYearId', blank=True, null=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     vendorid = models.ForeignKey('InvVendormaster', models.DO_NOTHING, db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
#     indentnumber = models.CharField(db_column='IndentNumber', unique=True, max_length=50)  # Field name made lowercase.
#     indentdate = models.DateField(db_column='IndentDate')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isworkorder = models.BooleanField(db_column='IsWorkOrder', blank=True, null=True, db_comment='1:Work Order && 0:Indent')  # Field name made lowercase.
#     usermembershipid = models.IntegerField(db_column='UserMemberShipId', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=4000, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_IndentMaster'


# class InvItem(models.Model):
#     itemid = models.AutoField(db_column='ItemId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
#     unitid = models.ForeignKey('InvUnit', models.DO_NOTHING, db_column='UnitId', blank=True, null=True)  # Field name made lowercase.
#     itemname = models.CharField(db_column='ItemName', max_length=250)  # Field name made lowercase.
#     itemcode = models.CharField(db_column='ItemCode', unique=True, max_length=50)  # Field name made lowercase.
#     olditemcode = models.CharField(db_column='OldItemCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     vehicaltype = models.CharField(db_column='VehicalType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     specification = models.CharField(db_column='Specification', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     maker = models.CharField(db_column='Maker', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     newrate = models.FloatField(db_column='NewRate', blank=True, null=True)  # Field name made lowercase.
#     lastrate = models.FloatField(db_column='LastRate', blank=True, null=True)  # Field name made lowercase.
#     avgrate = models.FloatField(db_column='AvgRate', blank=True, null=True)  # Field name made lowercase.
#     openingstock = models.FloatField(db_column='OpeningStock', blank=True, null=True)  # Field name made lowercase.
#     balancestock = models.FloatField(db_column='BalanceStock', blank=True, null=True)  # Field name made lowercase.
#     isassetmanagement = models.BooleanField(db_column='IsAssetManagement', blank=True, null=True)  # Field name made lowercase.
#     iswarranty = models.BooleanField(db_column='IsWarranty', blank=True, null=True)  # Field name made lowercase.
#     warrantyindays = models.IntegerField(db_column='WarrantyInDays', blank=True, null=True)  # Field name made lowercase.
#     isguaranty = models.BooleanField(db_column='IsGuaranty', blank=True, null=True)  # Field name made lowercase.
#     guarantyindays = models.IntegerField(db_column='GuarantyInDays', blank=True, null=True)  # Field name made lowercase.
#     isonebyone = models.BooleanField(db_column='IsOneByOne', blank=True, null=True)  # Field name made lowercase.
#     reorderitems = models.IntegerField(db_column='ReorderItems', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_Item'


# class InvPetrolapinvoice(models.Model):
#     petrolapinvoiceid = models.AutoField(db_column='PetrolAPInvoiceId', primary_key=True)  # Field name made lowercase.
#     supplierid = models.ForeignKey(InvFuelsuppliermaster, models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
#     petrollfillingdetailsid = models.ForeignKey('InvPetrolfillingdetails', models.DO_NOTHING, db_column='PetrollFillingDetailsId')  # Field name made lowercase.
#     billnumber = models.CharField(db_column='BillNumber', max_length=50)  # Field name made lowercase.
#     billdate = models.DateField(db_column='BillDate')  # Field name made lowercase.
#     invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isapproved = models.BooleanField(db_column='IsApproved', blank=True, null=True)  # Field name made lowercase.
#     approvedperson = models.IntegerField(db_column='ApprovedPerson', blank=True, null=True)  # Field name made lowercase.
#     approvedmacid = models.CharField(db_column='ApprovedMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     cancellationremark = models.CharField(db_column='CancellationRemark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PetrolAPInvoice'


# class InvPetrolfillingdetails(models.Model):
#     petrolfillingdetailsid = models.AutoField(db_column='PetrolFillingDetailsId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
#     supplierid = models.ForeignKey(InvFuelsuppliermaster, models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
#     dmnumber = models.IntegerField(db_column='DMNumber')  # Field name made lowercase.
#     businformationid = models.ForeignKey('MtnBusinformation', models.DO_NOTHING, db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     busnumber = models.CharField(db_column='BusNumber', max_length=50)  # Field name made lowercase.
#     reading = models.CharField(db_column='Reading', max_length=50)  # Field name made lowercase.
#     quantity = models.DecimalField(db_column='Quantity', max_digits=18, decimal_places=2)  # Field name made lowercase.
#     rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=2)  # Field name made lowercase.
#     fillingdatetime = models.DateTimeField(db_column='FillingDateTime')  # Field name made lowercase.
#     sheetno = models.IntegerField(db_column='SheetNo', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PetrolFillingDetails'
#         unique_together = (('supplierid', 'busnumber', 'quantity', 'fillingdatetime'),)


# class InvPreindent(models.Model):
#     preindentid = models.AutoField(db_column='PreIndentId', primary_key=True)  # Field name made lowercase.
#     itemid = models.ForeignKey(InvItem, models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
#     itemno = models.CharField(db_column='ItemNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     qty = models.FloatField(db_column='Qty')  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     qtyinstore = models.FloatField(db_column='QtyInStore', blank=True, null=True)  # Field name made lowercase.
#     replacedate = models.DateTimeField(db_column='ReplaceDate', blank=True, null=True)  # Field name made lowercase.
#     isscrap = models.BooleanField(db_column='IsScrap', blank=True, null=True)  # Field name made lowercase.
#     scrapremark = models.CharField(db_column='ScrapRemark', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     scrapreturndate = models.DateTimeField(db_column='ScrapReturnDate', blank=True, null=True)  # Field name made lowercase.
#     scrapreturnremark = models.CharField(db_column='ScrapReturnRemark', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     isscrapsale = models.BooleanField(db_column='IsScrapSale', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PreIndent'


# class InvPurchaseorder(models.Model):
#     purchaseorderid = models.AutoField(db_column='PurchaseOrderId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     financialyearid = models.ForeignKey(CoreFinancialyear, models.DO_NOTHING, db_column='FinancialYearId', blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.CharField(db_column='PONumber', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
#     podate = models.DateField(db_column='PODate')  # Field name made lowercase.
#     poexpdate = models.DateField(db_column='POEXPDate', blank=True, null=True)  # Field name made lowercase.
#     vendorid = models.ForeignKey('InvVendormaster', models.DO_NOTHING, db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
#     quatationsubmissionid = models.ForeignKey('InvQuotationsubmission', models.DO_NOTHING, db_column='QuatationSubmissionId', blank=True, null=True)  # Field name made lowercase.
#     netamount = models.FloatField(db_column='NetAmount', blank=True, null=True)  # Field name made lowercase.
#     gst = models.FloatField(db_column='GST', blank=True, null=True)  # Field name made lowercase.
#     othertax = models.FloatField(db_column='OtherTAX', blank=True, null=True)  # Field name made lowercase.
#     taxtotal = models.FloatField(db_column='TaxTotal', blank=True, null=True)  # Field name made lowercase.
#     othercharges = models.FloatField(db_column='OtherCharges', blank=True, null=True)  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase.
#     educationcess = models.FloatField(db_column='EducationCess', blank=True, null=True)  # Field name made lowercase.
#     highereducationcess = models.FloatField(db_column='HigherEducationCess', blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     cancellationremark = models.CharField(db_column='CancellationRemark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PurchaseOrder'


# class InvPurchaseorderdetails(models.Model):
#     purchaseorderdetailsid = models.AutoField(db_column='PurchaseOrderDetailsId', primary_key=True)  # Field name made lowercase.
#     purchaseorderid = models.IntegerField(db_column='PurchaseOrderId')  # Field name made lowercase.
#     itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
#     vendorid = models.IntegerField(db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
#     gstper = models.FloatField(db_column='GSTPer', blank=True, null=True)  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount', blank=True, null=True)  # Field name made lowercase.
#     discountper = models.FloatField(db_column='DiscountPer', blank=True, null=True)  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PurchaseOrderDetails'


# class InvPurchaseorderexpenses(models.Model):
#     purchaseorderexpensesid = models.AutoField(db_column='PurchaseOrderExpensesId', primary_key=True)  # Field name made lowercase.
#     purchaseorderid = models.IntegerField(db_column='PurchaseOrderId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     basicamount = models.DecimalField(db_column='BasicAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     ispercent = models.BooleanField(db_column='IsPercent', db_comment='0: Percent, 1:Fix Amount')  # Field name made lowercase.
#     percentcalc = models.FloatField(db_column='PercentCalc')  # Field name made lowercase.
#     calcamount = models.DecimalField(db_column='CalcAmount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PurchaseOrderExpenses'


# class InvPurchaseordertc(models.Model):
#     purchaseordertcid = models.AutoField(db_column='PurchaseOrderTCId', primary_key=True)  # Field name made lowercase.
#     purchaseorderid = models.ForeignKey(InvPurchaseorder, models.DO_NOTHING, db_column='PurchaseOrderId')  # Field name made lowercase.
#     tcheader = models.CharField(db_column='TCHeader', max_length=250)  # Field name made lowercase.
#     tcdescription = models.TextField(db_column='TCDescription')  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PurchaseOrderTC'


# class InvPurchaseordertaxes(models.Model):
#     purchaseordertaxesid = models.AutoField(db_column='PurchaseOrderTaxesId', primary_key=True)  # Field name made lowercase.
#     purchaseorderid = models.ForeignKey(InvPurchaseorder, models.DO_NOTHING, db_column='PurchaseOrderId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     basicamount = models.DecimalField(db_column='BasicAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     ispercent = models.BooleanField(db_column='IsPercent', db_comment='0: Percent, 1:Fix Amount')  # Field name made lowercase.
#     percentcalc = models.FloatField(db_column='PercentCalc')  # Field name made lowercase.
#     calcamount = models.DecimalField(db_column='CalcAmount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_PurchaseOrderTaxes'


# class InvQuatationsubmissioncharges(models.Model):
#     quatationsubmissionchargesid = models.AutoField(db_column='QuatationSubmissionChargesId', primary_key=True)  # Field name made lowercase.
#     quotationsubmissionid = models.ForeignKey('InvQuotationsubmission', models.DO_NOTHING, db_column='QuotationSubmissionId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     basicamount = models.DecimalField(db_column='BasicAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     ispercent = models.BooleanField(db_column='IsPercent')  # Field name made lowercase.
#     percentage = models.FloatField(db_column='Percentage')  # Field name made lowercase.
#     percentageamt = models.DecimalField(db_column='PercentageAmt', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_QuatationSubmissionCharges'


# class InvQuatationsubmissiontaxes(models.Model):
#     quatationsubmissiontaxesid = models.AutoField(db_column='QuatationSubmissionTaxesId', primary_key=True)  # Field name made lowercase.
#     quatationsubmissionid = models.ForeignKey('InvQuotationsubmission', models.DO_NOTHING, db_column='QuatationSubmissionId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     basicamount = models.DecimalField(db_column='BasicAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     ispercent = models.BooleanField(db_column='IsPercent')  # Field name made lowercase.
#     percentcalc = models.FloatField(db_column='PercentCalc')  # Field name made lowercase.
#     calcamount = models.DecimalField(db_column='CalcAmount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_QuatationSubmissionTaxes'


# class InvQuotationsubmission(models.Model):
#     quotationsubmissionid = models.AutoField(db_column='QuotationSubmissionId', primary_key=True)  # Field name made lowercase.
#     tenderid = models.IntegerField(db_column='TenderId')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     vendorid = models.ForeignKey('InvVendormaster', models.DO_NOTHING, db_column='VendorId')  # Field name made lowercase.
#     refferencenumber = models.CharField(db_column='RefferenceNumber', max_length=50)  # Field name made lowercase.
#     submissionquantity = models.FloatField(db_column='SubmissionQuantity')  # Field name made lowercase.
#     itemid = models.ForeignKey(InvItem, models.DO_NOTHING, db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
#     submissionrate = models.FloatField(db_column='SubmissionRate')  # Field name made lowercase.
#     submissiondate = models.DateField(db_column='SubmissionDate')  # Field name made lowercase.
#     submissiondescription = models.CharField(db_column='SubmissionDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     submissionspecification = models.CharField(db_column='SubmissionSpecification', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     discountpercentage = models.FloatField(db_column='DiscountPercentage', blank=True, null=True)  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase.
#     gstpercentage = models.FloatField(db_column='GSTPercentage', blank=True, null=True)  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount', blank=True, null=True)  # Field name made lowercase.
#     othertax = models.FloatField(db_column='OtherTax')  # Field name made lowercase.
#     othercharges = models.FloatField(db_column='OtherCharges')  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='1=deleted, 0= not deleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_QuotationSubmission'


# class InvTenderdetails(models.Model):
#     tenderdetailsid = models.AutoField(db_column='TenderDetailsId', primary_key=True)  # Field name made lowercase.
#     tenderid = models.ForeignKey('InvTendermaster', models.DO_NOTHING, db_column='TenderId')  # Field name made lowercase.
#     approvaldetailsid = models.ForeignKey(InvApprovaldetails, models.DO_NOTHING, db_column='ApprovalDetailsId')  # Field name made lowercase.
#     itemid = models.ForeignKey(InvItem, models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
#     approvalquantity = models.FloatField(db_column='ApprovalQuantity')  # Field name made lowercase.
#     unitid = models.ForeignKey('InvUnit', models.DO_NOTHING, db_column='UnitId', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.CharField(db_column='EntryPerson', max_length=50)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.CharField(db_column='EditPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_TenderDetails'


# class InvTendermaster(models.Model):
#     tenderid = models.AutoField(db_column='TenderId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     tendernumber = models.CharField(db_column='TenderNumber', unique=True, max_length=100)  # Field name made lowercase.
#     tenderdate = models.DateField(db_column='TenderDate')  # Field name made lowercase.
#     financialyearid = models.ForeignKey(CoreFinancialyear, models.DO_NOTHING, db_column='FinancialYearId')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.CharField(db_column='EntryPerson', max_length=50)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.CharField(db_column='EditPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_TenderMaster'


# class InvTermandcondition(models.Model):
#     termsandconditionid = models.AutoField(db_column='TermsAndConditionId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     tearmsandconditionheader = models.CharField(db_column='TearmsAndConditionHeader', max_length=50)  # Field name made lowercase.
#     tearmsandconditiondescription = models.TextField(db_column='TearmsAndConditionDescription')  # Field name made lowercase.
#     priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     iswo = models.BooleanField(db_column='IsWO', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_TermAndCondition'


# class InvUnit(models.Model):
#     unitid = models.AutoField(db_column='UnitId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     unittypeid = models.ForeignKey('InvUnittype', models.DO_NOTHING, db_column='UnitTypeId')  # Field name made lowercase.
#     parentunitid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentUnitId', blank=True, null=True)  # Field name made lowercase.
#     unitname = models.CharField(db_column='UnitName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     unitcode = models.CharField(db_column='UnitCode', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
#     unitfactor = models.CharField(db_column='UnitFactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.CharField(db_column='EntryPerson', max_length=50)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.CharField(db_column='EditPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_Unit'


# class InvUnittype(models.Model):
#     unittypeid = models.AutoField(db_column='UnitTypeId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     unittypename = models.CharField(db_column='UnitTypeName', max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_UnitType'


# class InvVendorbankdetails(models.Model):
#     vendorbankdetailsid = models.AutoField(db_column='VendorBankDetailsId', primary_key=True)  # Field name made lowercase.
#     vendorid = models.ForeignKey('InvVendormaster', models.DO_NOTHING, db_column='VendorId')  # Field name made lowercase.
#     bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     accountno = models.CharField(db_column='AccountNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ifscode = models.CharField(db_column='IFSCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     swiscode = models.CharField(db_column='SWISCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_VendorBankDetails'


# class InvVendorcontactdetails(models.Model):
#     vendorcontactid = models.AutoField(db_column='VendorContactId', primary_key=True)  # Field name made lowercase.
#     vendorid = models.ForeignKey('InvVendormaster', models.DO_NOTHING, db_column='VendorId')  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=50)  # Field name made lowercase.
#     cpdesignation = models.CharField(db_column='CPDesignation', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cpbranch = models.CharField(db_column='CPBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mobileno = models.CharField(db_column='MobileNo', max_length=50)  # Field name made lowercase.
#     landlineno1 = models.CharField(db_column='LandLineNo1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     landlineno2 = models.CharField(db_column='LandLineNo2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     emailid = models.CharField(db_column='EmailId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isnotificationemail = models.BooleanField(db_column='IsNotificationEmail')  # Field name made lowercase.
#     isnotificationsms = models.BooleanField(db_column='IsNotificationSMS')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_VendorContactDetails'


# class InvVendordocumentmaster(models.Model):
#     vendordocumentmasterid = models.AutoField(db_column='VendorDocumentMasterId', primary_key=True)  # Field name made lowercase.
#     vendorid = models.ForeignKey('InvVendormaster', models.DO_NOTHING, db_column='VendorId')  # Field name made lowercase.
#     documenttype = models.CharField(db_column='DocumentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     documentattachment = models.CharField(db_column='DocumentAttachment', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     documentnumber = models.CharField(db_column='DocumentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_VendorDocumentMaster'


# class InvVendormaster(models.Model):
#     vendorid = models.AutoField(db_column='VendorId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     vendorcode = models.CharField(db_column='VendorCode', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
#     vendorname = models.CharField(db_column='VendorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pincode = models.CharField(db_column='PinCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pannumber1 = models.CharField(db_column='PANNumber1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pannumber2 = models.CharField(db_column='PANNumber2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tinnumber = models.CharField(db_column='TINNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isigst = models.BooleanField(db_column='IsIGST')  # Field name made lowercase.
#     gstin = models.CharField(db_column='GSTIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     creditlimit = models.FloatField(db_column='CreditLimit', blank=True, null=True)  # Field name made lowercase.
#     paymentgraceperiod = models.IntegerField(db_column='PaymentGracePeriod', blank=True, null=True)  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_VendorMaster'


# class InvVendorratecontract(models.Model):
#     vendorratecontractid = models.AutoField(db_column='VendorRateContractId', primary_key=True)  # Field name made lowercase.
#     vendorid = models.ForeignKey(InvVendormaster, models.DO_NOTHING, db_column='VendorId')  # Field name made lowercase.
#     startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
#     enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
#     agreementdate = models.DateField(db_column='AgreementDate', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     agreementurl = models.CharField(db_column='AgreementUrl', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_VendorRateContract'


# class InvVendorratecontractdetails(models.Model):
#     vendorratecontractdetailsid = models.AutoField(db_column='VendorRateContractDetailsId', primary_key=True)  # Field name made lowercase.
#     vendorratecontractid = models.ForeignKey(InvVendorratecontract, models.DO_NOTHING, db_column='VendorRateContractId')  # Field name made lowercase.
#     itemid = models.ForeignKey(InvItem, models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
#     gstpercent = models.FloatField(db_column='GSTPercent', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_VendorRateContractDetails'


# class InvWocategory(models.Model):
#     wocategoryid = models.AutoField(db_column='WOCategoryId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     wogroupid = models.IntegerField(db_column='WOGroupId')  # Field name made lowercase.
#     categoryname = models.CharField(db_column='CategoryName', max_length=50)  # Field name made lowercase.
#     categorycode = models.CharField(db_column='CategoryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     startno = models.IntegerField(db_column='StartNo', blank=True, null=True)  # Field name made lowercase.
#     endno = models.IntegerField(db_column='EndNo', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOCategory'


# class InvWogrnbilldetails(models.Model):
#     wogrnbilldetailsid = models.AutoField(db_column='WOGRNBillDetailsId', primary_key=True)  # Field name made lowercase.
#     wobillmasterid = models.IntegerField(db_column='WOBillMasterId')  # Field name made lowercase.
#     woitemid = models.IntegerField(db_column='WOItemId')  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
#     wtavgrate = models.FloatField(db_column='WtAvgRate', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status')  # Field name made lowercase.
#     discountper = models.FloatField(db_column='DiscountPer')  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount')  # Field name made lowercase.
#     gstper = models.FloatField(db_column='GSTPer')  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount')  # Field name made lowercase.
#     vatper = models.FloatField(db_column='VATPer')  # Field name made lowercase.
#     vatamount = models.FloatField(db_column='VATAmount')  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount')  # Field name made lowercase.
#     description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOGRNBillDetails'


# class InvWogrnbillmaster(models.Model):
#     wogrnbillmasterid = models.AutoField(db_column='WOGRNBillMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     wopurchaseorderid = models.IntegerField(db_column='WOPurchaseOrderId')  # Field name made lowercase.
#     billnumber = models.CharField(db_column='BillNumber', max_length=50)  # Field name made lowercase.
#     billdate = models.DateField(db_column='BillDate')  # Field name made lowercase.
#     billinvoiceno = models.CharField(db_column='BillInvoiceNo', max_length=50)  # Field name made lowercase.
#     billamount = models.FloatField(db_column='BillAmount')  # Field name made lowercase.
#     gst = models.FloatField(db_column='GST')  # Field name made lowercase.
#     educationcess = models.FloatField(db_column='EducationCess')  # Field name made lowercase.
#     highereducationcess = models.FloatField(db_column='HigherEducationCess')  # Field name made lowercase.
#     othertax = models.FloatField(db_column='OtherTax')  # Field name made lowercase.
#     othercharges = models.FloatField(db_column='OtherCharges')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOGRNBillMaster'


# class InvWogrndetails(models.Model):
#     wogrndetailsid = models.AutoField(db_column='WOGRNDetailsId', primary_key=True)  # Field name made lowercase.
#     wogrnmasterid = models.IntegerField(db_column='WOGRNMasterId')  # Field name made lowercase.
#     woitemid = models.IntegerField(db_column='WOItemId')  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
#     wtavgrate = models.FloatField(db_column='WtAvgRate', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status')  # Field name made lowercase.
#     itemnumber = models.CharField(db_column='ItemNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     warrantystartdate = models.DateTimeField(db_column='WarrantyStartDate', blank=True, null=True)  # Field name made lowercase.
#     warrantyenddate = models.DateTimeField(db_column='WarrantyEndDate', blank=True, null=True)  # Field name made lowercase.
#     guarantystartdate = models.DateTimeField(db_column='GuarantyStartDate', blank=True, null=True)  # Field name made lowercase.
#     guarantyenddate = models.DateTimeField(db_column='GuarantyEndDate', blank=True, null=True)  # Field name made lowercase.
#     isused = models.BooleanField(db_column='Isused', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     repairdescription = models.TextField(db_column='RepairDescription', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.CharField(db_column='EntryPerson', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.CharField(db_column='EditPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOGRNDetails'


# class InvWogrnmaster(models.Model):
#     wogrnmasterid = models.AutoField(db_column='WOGRNMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     grnnumber = models.CharField(db_column='GRNNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     grndate = models.DateField(db_column='GRNDate', blank=True, null=True)  # Field name made lowercase.
#     wopurchaseorderid = models.IntegerField(db_column='WOPurchaseOrderId', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     vehicalnumber = models.CharField(db_column='VehicalNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dmnumber = models.CharField(db_column='DMNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     cancellationremark = models.CharField(db_column='CancellationRemark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOGRNMaster'


# class InvWogroup(models.Model):
#     wogroupid = models.AutoField(db_column='WOGroupId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     groupname = models.CharField(db_column='GroupName', max_length=50)  # Field name made lowercase.
#     groupcode = models.CharField(db_column='GroupCode', unique=True, max_length=50)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOGroup'


# class InvWoindentdetails(models.Model):
#     woindentdetailsid = models.AutoField(db_column='WOIndentDetailsId', primary_key=True)  # Field name made lowercase.
#     woindentid = models.IntegerField(db_column='WOIndentId')  # Field name made lowercase.
#     woitemid = models.IntegerField(db_column='WOItemId')  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
#     unitid = models.IntegerField(db_column='UnitId', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     repairdescription = models.TextField(db_column='RepairDescription', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOIndentDetails'


# class InvWoindentmaster(models.Model):
#     woindentid = models.AutoField(db_column='WOIndentId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     woindentnumber = models.CharField(db_column='WOIndentNumber', unique=True, max_length=50)  # Field name made lowercase.
#     indentdate = models.DateField(db_column='IndentDate')  # Field name made lowercase.
#     vendorid = models.IntegerField(db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     usermembershipid = models.IntegerField(db_column='UserMemberShipId', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     financialyearid = models.IntegerField(db_column='FinancialYearId', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOIndentMaster'


# class InvWoitem(models.Model):
#     woitemid = models.AutoField(db_column='WOItemId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     wocategoryid = models.IntegerField(db_column='WOCategoryId')  # Field name made lowercase.
#     wounitid = models.IntegerField(db_column='WOUnitId')  # Field name made lowercase.
#     itemname = models.CharField(db_column='ItemName', max_length=250)  # Field name made lowercase.
#     itemcode = models.CharField(db_column='ItemCode', max_length=50)  # Field name made lowercase.
#     vehicaltype = models.CharField(db_column='VehicalType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     specification = models.CharField(db_column='Specification', max_length=250)  # Field name made lowercase.
#     maker = models.CharField(db_column='Maker', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     avgrate = models.FloatField(db_column='AvgRate', blank=True, null=True)  # Field name made lowercase.
#     lastrate = models.FloatField(db_column='LastRate', blank=True, null=True)  # Field name made lowercase.
#     decription = models.CharField(db_column='Decription', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     poitemid = models.IntegerField(db_column='POItemId', blank=True, null=True)  # Field name made lowercase.
#     openingstock = models.FloatField(db_column='OpeningStock', blank=True, null=True)  # Field name made lowercase.
#     balancestock = models.FloatField(db_column='BalanceStock', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOItem'


# class InvWopurchaseorder(models.Model):
#     wopurchaseorderid = models.AutoField(db_column='WOPurchaseOrderId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     woponumber = models.CharField(db_column='WOPONumber', unique=True, max_length=50)  # Field name made lowercase.
#     wopodate = models.DateField(db_column='WOPODate')  # Field name made lowercase.
#     poexpdate = models.DateField(db_column='POEXPDate', blank=True, null=True)  # Field name made lowercase.
#     academicyearid = models.IntegerField(db_column='AcademicYearID', blank=True, null=True)  # Field name made lowercase.
#     financialyearid = models.IntegerField(db_column='FinancialYearID', blank=True, null=True)  # Field name made lowercase.
#     quatationsubmissionid = models.IntegerField(db_column='QuatationSubmissionId', blank=True, null=True)  # Field name made lowercase.
#     othercharges = models.FloatField(db_column='OtherCharges')  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount', blank=True, null=True)  # Field name made lowercase.
#     servicetax = models.FloatField(db_column='ServiceTax')  # Field name made lowercase.
#     othertax = models.FloatField(db_column='OtherTax', blank=True, null=True)  # Field name made lowercase.
#     othertaxtotal = models.FloatField(db_column='OtherTaxTotal')  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase.
#     tdsper = models.FloatField(db_column='TDSPer', blank=True, null=True)  # Field name made lowercase.
#     tdsamount = models.FloatField(db_column='TDSAmount', blank=True, null=True)  # Field name made lowercase.
#     tdiscountper = models.FloatField(db_column='TDiscountPer', blank=True, null=True)  # Field name made lowercase.
#     tdiscountamount = models.FloatField(db_column='TDiscountAmount', blank=True, null=True)  # Field name made lowercase.
#     educationcess = models.FloatField(db_column='EducationCess')  # Field name made lowercase.
#     highereducationcess = models.FloatField(db_column='HigherEducationCess')  # Field name made lowercase.
#     netamount = models.FloatField(db_column='NetAmount', blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     vendorid = models.IntegerField(db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
#     cancellationremark = models.CharField(db_column='CancellationRemark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOPurchaseOrder'


# class InvWopurchaseorderdetails(models.Model):
#     wopurchaseorderdetailsid = models.AutoField(db_column='WOPurchaseOrderDetailsId', primary_key=True)  # Field name made lowercase.
#     wopurchaseorderid = models.IntegerField(db_column='WOPurchaseOrderId')  # Field name made lowercase.
#     itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
#     vendorid = models.IntegerField(db_column='VendorId', blank=True, null=True)  # Field name made lowercase.
#     rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
#     quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
#     gstrate = models.FloatField(db_column='GSTRate', blank=True, null=True)  # Field name made lowercase.
#     discountper = models.FloatField(db_column='DiscountPer', blank=True, null=True)  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase.
#     gstper = models.FloatField(db_column='GSTPer', blank=True, null=True)  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount', blank=True, null=True)  # Field name made lowercase.
#     vatper = models.FloatField(db_column='VATPer', blank=True, null=True)  # Field name made lowercase.
#     vatamount = models.FloatField(db_column='VATAmount', blank=True, null=True)  # Field name made lowercase.
#     lbtper = models.FloatField(db_column='LBTPer', blank=True, null=True)  # Field name made lowercase.
#     lbtamount = models.FloatField(db_column='LBTAmount', blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     itemnumber = models.CharField(db_column='ItemNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     repairdescription = models.TextField(db_column='RepairDescription', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOPurchaseOrderDetails'


# class InvWopurchaseordertc(models.Model):
#     wopurchaseordertcid = models.AutoField(db_column='WOPurchaseOrderTCId', primary_key=True)  # Field name made lowercase.
#     wopurchaseorderid = models.IntegerField(db_column='WOPurchaseOrderId')  # Field name made lowercase.
#     tcheader = models.CharField(db_column='TCHeader', max_length=250)  # Field name made lowercase.
#     tcdescription = models.TextField(db_column='TCDescription')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOPurchaseOrderTC'


# class InvWoquatationsubmissioncharges(models.Model):
#     woquatationsubmissionchargesid = models.AutoField(db_column='WOQuatationSubmissionChargesId', primary_key=True)  # Field name made lowercase.
#     woquotationsubmissionid = models.ForeignKey('InvWoquotationsubmission', models.DO_NOTHING, db_column='WOQuotationSubmissionId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     basicamount = models.DecimalField(db_column='BasicAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     ispercent = models.BooleanField(db_column='IsPercent')  # Field name made lowercase.
#     percentage = models.FloatField(db_column='Percentage')  # Field name made lowercase.
#     percentageamt = models.DecimalField(db_column='PercentageAmt', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOQuatationSubmissionCharges'


# class InvWoquatationsubmissiontaxes(models.Model):
#     woquatationsubmissiontaxesid = models.AutoField(db_column='WOQuatationSubmissionTaxesId', primary_key=True)  # Field name made lowercase.
#     woquatationsubmissionid = models.ForeignKey('InvWoquotationsubmission', models.DO_NOTHING, db_column='WOQuatationSubmissionId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     basicamount = models.DecimalField(db_column='BasicAmount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     ispercent = models.BooleanField(db_column='IsPercent')  # Field name made lowercase.
#     percentcalc = models.FloatField(db_column='PercentCalc')  # Field name made lowercase.
#     calcamount = models.DecimalField(db_column='CalcAmount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOQuatationSubmissionTaxes'


# class InvWoquotationsubmission(models.Model):
#     woquotationsubmissionid = models.AutoField(db_column='WOQuotationSubmissionId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     wotenderid = models.IntegerField(db_column='WOTenderId')  # Field name made lowercase.
#     submissionquantity = models.FloatField(db_column='SubmissionQuantity')  # Field name made lowercase.
#     vendorid = models.IntegerField(db_column='VendorId')  # Field name made lowercase.
#     refferencenumber = models.CharField(db_column='RefferenceNumber', max_length=50)  # Field name made lowercase.
#     submissiondate = models.DateField(db_column='SubmissionDate')  # Field name made lowercase.
#     submissionrate = models.FloatField(db_column='SubmissionRate')  # Field name made lowercase.
#     submissiondescription = models.CharField(db_column='SubmissionDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     submissionspecification = models.CharField(db_column='SubmissionSpecification', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     woitemid = models.IntegerField(db_column='WOItemId', blank=True, null=True)  # Field name made lowercase.
#     discountper = models.FloatField(db_column='DiscountPer', blank=True, null=True)  # Field name made lowercase.
#     discountamount = models.FloatField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase.
#     gstper = models.FloatField(db_column='GSTPer', blank=True, null=True)  # Field name made lowercase.
#     gstamount = models.FloatField(db_column='GSTAmount', blank=True, null=True)  # Field name made lowercase.
#     vatper = models.FloatField(db_column='VATPer', blank=True, null=True)  # Field name made lowercase.
#     vatamount = models.FloatField(db_column='VATAmount', blank=True, null=True)  # Field name made lowercase.
#     lbtper = models.FloatField(db_column='LBTPer', blank=True, null=True)  # Field name made lowercase.
#     lbtamount = models.FloatField(db_column='LBTAmount', blank=True, null=True)  # Field name made lowercase.
#     totalamount = models.FloatField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
#     servicetax = models.FloatField(db_column='ServiceTax')  # Field name made lowercase.
#     educationcess = models.FloatField(db_column='EducationCess')  # Field name made lowercase.
#     highereducationcess = models.FloatField(db_column='HigherEducationCess')  # Field name made lowercase.
#     othertax = models.FloatField(db_column='OtherTax')  # Field name made lowercase.
#     othercharges = models.FloatField(db_column='OtherCharges')  # Field name made lowercase.
#     itemnumber = models.CharField(db_column='ItemNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     repairdescription = models.TextField(db_column='RepairDescription', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', blank=True, null=True)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOQuotationSubmission'


# class InvWotenderdetails(models.Model):
#     wotenderdetailsid = models.AutoField(db_column='WOTenderDetailsId', primary_key=True)  # Field name made lowercase.
#     wotenderid = models.IntegerField(db_column='WOTenderId')  # Field name made lowercase.
#     woitemid = models.IntegerField(db_column='WOItemId')  # Field name made lowercase.
#     approvalquantity = models.FloatField(db_column='ApprovalQuantity')  # Field name made lowercase.
#     wounitid = models.IntegerField(db_column='WOUnitId', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     repairdescription = models.TextField(db_column='RepairDescription', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.CharField(db_column='EntryPerson', max_length=50)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.CharField(db_column='EditPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOTenderDetails'


# class InvWotendermaster(models.Model):
#     wotendermasterid = models.AutoField(db_column='WOTenderMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     tendernumber = models.CharField(db_column='TenderNumber', max_length=100)  # Field name made lowercase.
#     tenderdate = models.DateField(db_column='TenderDate')  # Field name made lowercase.
#     financialyearid = models.IntegerField(db_column='FinancialYearId')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.CharField(db_column='EntryPerson', max_length=50)  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.CharField(db_column='EditPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'INV_WOTenderMaster'


# class LevLeaveadjestment(models.Model):
#     leaveadjustmentid = models.AutoField(db_column='LeaveAdjustmentId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Include In Form as name')  # Field name made lowercase.
#     month = models.DateField(db_column='Month', blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     leavetypeid = models.IntegerField(db_column='LeaveTypeId', blank=True, null=True)  # Field name made lowercase.
#     totalleaves = models.IntegerField(db_column='TotalLeaves', blank=True, null=True)  # Field name made lowercase.
#     adjustmentdays = models.IntegerField(db_column='AdjustmentDays', blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=500, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     isappliedbyemp = models.BooleanField(db_column='IsAppliedByEmp')  # Field name made lowercase.
#     isappliedbymanager = models.BooleanField(db_column='IsAppliedByManager')  # Field name made lowercase.
#     isappliedbyhr = models.BooleanField(db_column='IsAppliedByHR')  # Field name made lowercase.
#     ismanagerapproved = models.BooleanField(db_column='IsManagerApproved', blank=True, null=True)  # Field name made lowercase.
#     ishrapproved = models.BooleanField(db_column='IsHRApproved', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_LeaveAdjestment'


# class LevLeaveapplication(models.Model):
#     leaveapplicationid = models.AutoField(db_column='LeaveApplicationId', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
#     financialyearid = models.ForeignKey(CoreFinancialyear, models.DO_NOTHING, db_column='FinancialYearId', db_comment='Include In form(Req)')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Include In Form as name')  # Field name made lowercase.
#     leavetypeid = models.IntegerField(db_column='LeaveTypeId', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     applicationtype = models.CharField(db_column='ApplicationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     applieddate = models.DateField(db_column='AppliedDate', db_comment='Include In form(Req)')  # Field name made lowercase.
#     startdate = models.DateField(db_column='StartDate', db_comment='Include In form(Req)')  # Field name made lowercase.
#     enddate = models.DateField(db_column='EndDate', db_comment='Include In form(Req)')  # Field name made lowercase.
#     totaldays = models.FloatField(db_column='TotalDays')  # Field name made lowercase.
#     leavedescription = models.CharField(db_column='LeaveDescription', max_length=500, blank=True, null=True, db_comment='Include In form')  # Field name made lowercase.
#     documentpath = models.CharField(db_column='DocumentPath', max_length=500, blank=True, null=True, db_comment='Include In form')  # Field name made lowercase.
#     isappliedbyemp = models.BooleanField(db_column='IsAppliedByEmp')  # Field name made lowercase.
#     isappliedbymanager = models.BooleanField(db_column='IsAppliedByManager')  # Field name made lowercase.
#     approvalstatus = models.CharField(db_column='ApprovalStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
#     issubstituteapproved = models.BooleanField(db_column='IsSubstituteApproved', blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     substituteresponse = models.CharField(db_column='SubstituteResponse', max_length=500, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     subapproveddate = models.DateField(db_column='SubApprovedDate', blank=True, null=True)  # Field name made lowercase.
#     cancelreason = models.CharField(db_column='CancelReason', max_length=500, blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     canceldate = models.DateField(db_column='CancelDate', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True, db_comment='Included in Add form')  # Field name made lowercase.
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_LeaveApplication'


# class LevLeaveapplicationdetails(models.Model):
#     leaveapplicationdetailsid = models.AutoField(db_column='LeaveApplicationDetailsId', primary_key=True)  # Field name made lowercase.
#     leaveapplicationid = models.ForeignKey(LevLeaveapplication, models.DO_NOTHING, db_column='LeaveApplicationId')  # Field name made lowercase.
#     financialyearid = models.ForeignKey(CoreFinancialyear, models.DO_NOTHING, db_column='FinancialYearId')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
#     leavetype = models.CharField(db_column='LeaveType', max_length=50)  # Field name made lowercase.
#     leavedate = models.DateField(db_column='LeaveDate')  # Field name made lowercase.
#     daystatus = models.CharField(db_column='DayStatus', max_length=50)  # Field name made lowercase.
#     approvalstatus = models.CharField(db_column='ApprovalStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
#     cancelreason = models.CharField(db_column='CancelReason', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     canceldate = models.DateField(db_column='CancelDate', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_LeaveApplicationDetails'


# class LevLeavemaster(models.Model):
#     leavemasterid = models.AutoField(db_column='LeaveMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', db_comment='Include In form(Req)')  # Field name made lowercase.
#     financialyearid = models.IntegerField(db_column='FinancialYearId', db_comment='Include In form(Req)')  # Field name made lowercase.
#     leavetypeid = models.IntegerField(db_column='LeaveTypeId', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     leaveavailable = models.FloatField(db_column='LeaveAvailable', blank=True, null=True)  # Field name made lowercase.
#     balanceleave = models.FloatField(db_column='BalanceLeave', blank=True, null=True, db_comment='Total Leave = LeaveCount + Car')  # Field name made lowercase.
#     carryleave = models.FloatField(db_column='CarryLeave', blank=True, null=True, db_comment='Back Year Leave')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_LeaveMaster'


# class LevLeaveregister(models.Model):
#     leaveregisterid = models.AutoField(db_column='LeaveRegisterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
#     financialyearid = models.IntegerField(db_column='FinancialYearId')  # Field name made lowercase.
#     pl = models.FloatField(db_column='PL', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     sl = models.FloatField(db_column='SL', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     cl = models.FloatField(db_column='CL', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     co = models.FloatField(db_column='CO', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     lwp = models.FloatField(db_column='LWP', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l1 = models.FloatField(db_column='L1', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l2 = models.FloatField(db_column='L2', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l3 = models.FloatField(db_column='L3', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l4 = models.FloatField(db_column='L4', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l5 = models.FloatField(db_column='L5', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l6 = models.FloatField(db_column='L6', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l7 = models.FloatField(db_column='L7', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l8 = models.FloatField(db_column='L8', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l10 = models.FloatField(db_column='L10', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l11 = models.FloatField(db_column='L11', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l12 = models.FloatField(db_column='L12', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l13 = models.FloatField(db_column='L13', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l14 = models.FloatField(db_column='L14', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     l15 = models.FloatField(db_column='L15', db_comment='Casual Leave (CL), SL, EL')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_LeaveRegister'


# class LevLeavetype(models.Model):
#     leavetypeid = models.AutoField(db_column='LeaveTypeId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     leavename = models.CharField(db_column='LeaveName', max_length=50)  # Field name made lowercase.
#     minimumdays = models.IntegerField(db_column='MinimumDays', db_comment='Include In form(Req)')  # Field name made lowercase.
#     maximumdays = models.IntegerField(db_column='MaximumDays')  # Field name made lowercase.
#     condition1 = models.BooleanField(db_column='Condition1', blank=True, null=True)  # Field name made lowercase.
#     condition2 = models.BooleanField(db_column='Condition2', blank=True, null=True)  # Field name made lowercase.
#     condition3 = models.BooleanField(db_column='Condition3', blank=True, null=True)  # Field name made lowercase.
#     condition4 = models.BooleanField(db_column='Condition4', blank=True, null=True)  # Field name made lowercase.
#     condition5 = models.BooleanField(db_column='Condition5', blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_LeaveType'


# class LevTeammaster(models.Model):
#     teammasterid = models.AutoField(db_column='TeamMasterId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     teamname = models.CharField(db_column='TeamName', max_length=100)  # Field name made lowercase.
#     teamdescription = models.TextField(db_column='TeamDescription', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     totalmember = models.IntegerField(db_column='TotalMember', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     minimummember = models.IntegerField(db_column='MinimumMember', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     nomemberforleave = models.IntegerField(db_column='NoMemberForLeave', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_TeamMaster'


# class LevTeammember(models.Model):
#     teammemberid = models.AutoField(db_column='TeamMemberId', primary_key=True)  # Field name made lowercase.
#     teammasterid = models.ForeignKey(LevTeammaster, models.DO_NOTHING, db_column='TeamMasterId')  # Field name made lowercase.
#     teamdescription = models.CharField(db_column='TeamDescription', max_length=500, db_comment='Include In form(Req)')  # Field name made lowercase.
#     employeeid = models.ForeignKey(EmpEmployeemaster, models.DO_NOTHING, db_column='EmployeeId', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     ispublic = models.BooleanField(db_column='IsPublic', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     issupervisor = models.BooleanField(db_column='IsSupervisor', blank=True, null=True, db_comment='Include In form(Req)')  # Field name made lowercase.
#     isremoved = models.BooleanField(db_column='IsRemoved', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'LEV_TeamMember'


# class MobInspectioncheck(models.Model):
#     inspectionid = models.AutoField(primary_key=True)
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     vehicleid = models.IntegerField(db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
#     entry_date = models.DateField(blank=True, null=True)
#     scheduleid = models.IntegerField(db_column='ScheduleId', blank=True, null=True)  # Field name made lowercase.
#     schedulecode = models.CharField(db_column='ScheduleCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     buscode = models.CharField(db_column='BusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
#     drivername = models.CharField(db_column='DriverName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     inspectedby = models.CharField(max_length=50, blank=True, null=True)
#     vehicle_body_damage = models.CharField(max_length=50, blank=True, null=True)
#     question_1 = models.BooleanField(blank=True, null=True, db_comment='Windscreen for crack / clean')
#     question_1_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_1_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_2 = models.CharField(max_length=50, blank=True, null=True, db_comment='Front Body clean / no damage')
#     question_2_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_2_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_3 = models.CharField(max_length=50, blank=True, null=True, db_comment='Head Light / Indicator Light\r\n')
#     question_3_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_3_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_4 = models.CharField(max_length=50, blank=True, null=True, db_comment='Wiper working and blade ok\r\n')
#     question_4_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_4_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_5 = models.CharField(max_length=50, blank=True, null=True, db_comment='Front Des na on Board wokring\r')
#     question_5_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_5_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_6 = models.BooleanField(blank=True, null=True, db_comment='Left side body clean/no Damage')
#     question_6_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_6_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_7 = models.BooleanField(blank=True, null=True, db_comment='Side lamps working\r\n')
#     question_7_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_7_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_8 = models.CharField(max_length=50, blank=True, null=True, db_comment='Window glass clean and tidy\r\n')
#     question_8_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_8_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_9 = models.CharField(max_length=50, blank=True, null=True, db_comment='Rear view Mirrior clean / Fix\r')
#     question_9_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_9_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_10 = models.CharField(max_length=50, blank=True, null=True, db_comment='Rear body clean / No damage\r\n')
#     question_10_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_10_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_11 = models.CharField(max_length=50, blank=True, null=True, db_comment='Rear Window Glass clean\r\n')
#     question_11_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_11_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_12 = models.CharField(max_length=50, blank=True, null=True, db_comment='Rear Des na on na on Board Wor')
#     question_12_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_12_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_13 = models.CharField(max_length=50, blank=True, null=True, db_comment='Rear All Tail Lamps working\r\n')
#     question_13_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_13_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_14 = models.BooleanField(blank=True, null=True, db_comment='Engine compartment door lock\r\n')
#     question_14_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_14_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_15 = models.CharField(max_length=50, blank=True, null=True, db_comment='Right side body clean/no Damag')
#     question_15_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_15_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_16 = models.BooleanField(blank=True, null=True, db_comment='Door glass clean and tidy\r\n')
#     question_16_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_16_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_17 = models.CharField(max_length=50, blank=True, null=True, db_comment='Destination Board working\r\n')
#     question_17_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_17_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_18 = models.CharField(max_length=50, blank=True, null=True, db_comment='Rear View Mirror clean and fit')
#     question_18_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_18_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_19 = models.CharField(max_length=50, blank=True, null=True, db_comment='All Types free of damage & Air')
#     question_19_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_19_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_20 = models.CharField(max_length=50, blank=True, null=True, db_comment='Passenger saloon area, sear cl')
#     question_20_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_20_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_21 = models.BooleanField(blank=True, null=True, db_comment='Passenger hand rails and holdi')
#     question_21_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_21_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_22 = models.BooleanField(blank=True, null=True, db_comment='Fire extinguisher 3nos. Ok\r\n')
#     question_22_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_22_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_23 = models.CharField(max_length=50, blank=True, null=True, db_comment='Dashboard clean and tidy\r\n')
#     question_23_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_23_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_24 = models.CharField(max_length=50, blank=True, null=True, db_comment='All gauges and switches workin')
#     question_24_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_24_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_25 = models.CharField(max_length=50, blank=True, null=True, db_comment='Both Doors open and close\r\n')
#     question_25_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_25_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_26 = models.CharField(max_length=50, blank=True, null=True, db_comment='SOC panel working\r\n')
#     question_26_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_26_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_27 = models.CharField(max_length=50, blank=True, null=True, db_comment='All CCTV camera working\r\n')
#     question_27_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_27_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_28 = models.CharField(max_length=50, blank=True, null=True, db_comment='Seat Belt working / no damage\r')
#     question_28_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_28_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_29 = models.BooleanField(blank=True, null=True, db_comment='Inside all lights working\r\n')
#     question_29_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_29_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_30 = models.CharField(max_length=50, blank=True, null=True, db_comment='Sun wiser working / no damage\r')
#     question_30_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_30_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_31 = models.CharField(max_length=50, blank=True, null=True, db_comment='Driver Door condition on\r\n')
#     question_31_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_31_remarks = models.CharField(max_length=500, blank=True, null=True)
#     commentedby = models.CharField(max_length=50)
#     comment = models.CharField(max_length=50)
#     isstatus = models.CharField(db_column='IsStatus', max_length=50)  # Field name made lowercase.
#     approvedby = models.CharField(max_length=50)
#     approveddatetime = models.DateTimeField()
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MOB_InspectionCheck'


# class MobSafetymonitoring(models.Model):
#     safetyid = models.AutoField(primary_key=True)
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     vehicleid = models.IntegerField(db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
#     entry_date = models.DateField(blank=True, null=True)
#     scheduleid = models.IntegerField(db_column='ScheduleId', blank=True, null=True)  # Field name made lowercase.
#     schedulecode = models.CharField(db_column='ScheduleCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     buscode = models.CharField(db_column='BusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
#     drivername = models.CharField(db_column='DriverName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     conductedby = models.CharField(max_length=50, blank=True, null=True)
#     operationtype = models.CharField(max_length=50, blank=True, null=True)
#     question_1 = models.BooleanField(blank=True, null=True, db_comment='Seat Belt Violation')
#     question_1_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_1_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_2 = models.CharField(max_length=50, blank=True, null=True, db_comment='Vehicle Speed Violation')
#     question_2_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_3 = models.CharField(max_length=50, blank=True, null=True, db_comment='Usage of Indicators')
#     question_3_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_4 = models.CharField(max_length=50, blank=True, null=True, db_comment='Destination Sign Board')
#     question_4_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_4_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_5 = models.CharField(max_length=50, blank=True, null=True, db_comment='Trip / Schedule time Followed')
#     question_5_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_6 = models.BooleanField(blank=True, null=True, db_comment='Talking to Customers')
#     question_6_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_7 = models.BooleanField(blank=True, null=True, db_comment='Using hand held devices')
#     question_7_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_7_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_8 = models.CharField(max_length=50, blank=True, null=True, db_comment='Pre & Post Inspection Check Li')
#     question_8_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_8_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_9a = models.CharField(db_column='question_9A', max_length=50, blank=True, null=True, db_comment='Pilot Behavior Stopping Distan')  # Field name made lowercase.
#     question_9b = models.CharField(db_column='question_9B', max_length=50, blank=True, null=True, db_comment='Pilot Behavior Following Dista')  # Field name made lowercase.
#     question_9c = models.CharField(db_column='question_9C', max_length=50, blank=True, null=True, db_comment='Pilot Behavior Lane Discipline')  # Field name made lowercase.
#     question_9d = models.CharField(db_column='question_9D', max_length=50, blank=True, null=True, db_comment='Pilot Behaviour Overall Pilot ')  # Field name made lowercase.
#     question_9d_remarks = models.CharField(db_column='question_9D_remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     question_10 = models.CharField(max_length=50, blank=True, null=True, db_comment='Harsh Breking')
#     question_10_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_11 = models.CharField(max_length=50, blank=True, null=True, db_comment='Feedback from Conductor about ')
#     question_11_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_12 = models.CharField(max_length=50, blank=True, null=True, db_comment='Vehicle Internal Condition of ')
#     question_12_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_13 = models.CharField(max_length=50, blank=True, null=True, db_comment='BAC test')
#     question_13_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_14 = models.BooleanField(blank=True, null=True, db_comment='Feedback to Pilot')
#     question_14_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_15 = models.CharField(max_length=50, blank=True, null=True, db_comment='Any Encroached / Obstructed Bu')
#     question_15_photo = models.CharField(max_length=500, blank=True, null=True)
#     question_15_remarks = models.CharField(max_length=500, blank=True, null=True)
#     question_16a = models.BooleanField(db_column='question_16A', blank=True, null=True, db_comment='Infringement Level Severe')  # Field name made lowercase.
#     question_16b = models.BooleanField(db_column='question_16B', blank=True, null=True, db_comment='Infringement Level Moderate')  # Field name made lowercase.
#     question_16c = models.BooleanField(db_column='question_16C', blank=True, null=True, db_comment='Infringement Level Near-Miss o')  # Field name made lowercase.
#     question_17a = models.BooleanField(db_column='question_17A', blank=True, null=True, db_comment='Action on Infringement Level S')  # Field name made lowercase.
#     question_17b = models.BooleanField(db_column='question_17B', blank=True, null=True, db_comment='Action on Infringement Level V')  # Field name made lowercase.
#     question_17c = models.BooleanField(db_column='question_17C', blank=True, null=True, db_comment='Action on Infringement Level W')  # Field name made lowercase.
#     question_17d = models.BooleanField(db_column='question_17D', blank=True, null=True, db_comment='Action on Infringement Level R')  # Field name made lowercase.
#     question_17e = models.BooleanField(db_column='question_17E', blank=True, null=True, db_comment='Action on Infringement Level S')  # Field name made lowercase.
#     question_17f = models.BooleanField(db_column='question_17F', blank=True, null=True, db_comment='Action on Infringement Level T')  # Field name made lowercase.
#     isstatus = models.CharField(db_column='IsStatus', max_length=50)  # Field name made lowercase.
#     approvedby = models.CharField(max_length=50)
#     approveddatetime = models.DateTimeField(blank=True, null=True)
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MOB_SafetyMonitoring'


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


# class MtnBuscharginghistory(models.Model):
#     buscharginghistoryid = models.AutoField(db_column='BusChargingHistoryId', primary_key=True)  # Field name made lowercase.
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
#     f1 = models.CharField(db_column='F1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f2 = models.CharField(db_column='F2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lastodo = models.FloatField(db_column='LastODO', blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MTN_BusChargingHistory'




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


# class MtnBusinformationdetails(models.Model):
#     businformationdetailsid = models.AutoField(db_column='BusInformationDetailsId', primary_key=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId')  # Field name made lowercase.
#     detailstype = models.CharField(db_column='DetailsType', max_length=50)  # Field name made lowercase.
#     insurancecompanyname = models.CharField(db_column='InsuranceCompanyName', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     policynumber = models.CharField(db_column='PolicyNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     policystartdate = models.DateField(db_column='PolicyStartDate', blank=True, null=True)  # Field name made lowercase.
#     policyexpirydate = models.DateField(db_column='PolicyExpiryDate', blank=True, null=True)  # Field name made lowercase.
#     bslcertificateno = models.CharField(db_column='BSLCertificateNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     bslstartdate = models.DateField(db_column='BSLStartDate', blank=True, null=True)  # Field name made lowercase.
#     bslexpirydate = models.DateField(db_column='BSLExpiryDate', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MTN_BusInformationDetails'



  

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









# class OprInvoice(models.Model):
#     oprinvoiceid = models.AutoField(db_column='OPRInvoiceId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     schedulingdate = models.DateField(db_column='SchedulingDate', blank=True, null=True)  # Field name made lowercase.
#     totalfleet = models.IntegerField(db_column='TotalFleet', blank=True, null=True)  # Field name made lowercase.
#     deployedfleet = models.IntegerField(db_column='DeployedFleet', blank=True, null=True)  # Field name made lowercase.
#     defectedfleet = models.IntegerField(db_column='DefectedFleet', blank=True, null=True)  # Field name made lowercase.
#     scheduledfleet = models.IntegerField(db_column='ScheduledFleet', blank=True, null=True)  # Field name made lowercase.
#     assuredkm = models.FloatField(db_column='AssuredKM', blank=True, null=True)  # Field name made lowercase.
#     totalassuredkm = models.FloatField(db_column='TotalAssuredKM', blank=True, null=True)  # Field name made lowercase.
#     scheduledkm = models.FloatField(db_column='ScheduledKM', blank=True, null=True)  # Field name made lowercase.
#     runkm = models.FloatField(db_column='RunKM', blank=True, null=True)  # Field name made lowercase.
#     totallosskm = models.FloatField(db_column='TotalLossKM', blank=True, null=True)  # Field name made lowercase.
#     nonavablitylosskm = models.FloatField(db_column='NonAvablityLossKM', blank=True, null=True)  # Field name made lowercase.
#     lossatripskm = models.FloatField(db_column='LossATripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossbtripskm = models.FloatField(db_column='LossBTripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossctripskm = models.FloatField(db_column='LossCTripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossdtripskm = models.FloatField(db_column='LossDTripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossetripskm = models.FloatField(db_column='LossETripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossftripskm = models.FloatField(db_column='LossFTripsKM', blank=True, null=True)  # Field name made lowercase.
#     totalactualkm = models.FloatField(db_column='TotalActualKM', blank=True, null=True)  # Field name made lowercase.
#     totalexcesskm = models.FloatField(db_column='TotalExcessKM', blank=True, null=True)  # Field name made lowercase.
#     unscheduledkm = models.FloatField(db_column='UnscheduledKM', blank=True, null=True)  # Field name made lowercase.
#     rateactualkm = models.FloatField(db_column='RateActualKM', blank=True, null=True)  # Field name made lowercase.
#     rateexcesskm = models.FloatField(db_column='RateExcessKM', blank=True, null=True)  # Field name made lowercase.
#     rateunscheduledkm = models.FloatField(db_column='RateUnscheduledKM', blank=True, null=True)  # Field name made lowercase.
#     billingamount = models.FloatField(db_column='BillingAmount', blank=True, null=True)  # Field name made lowercase.
#     recoveryoem = models.FloatField(db_column='RecoveryOEM', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'OPR_Invoice'


# class OprKms(models.Model):
#     kmsid = models.AutoField(db_column='KMSId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     zoneid = models.IntegerField(db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
#     zonename = models.CharField(db_column='ZoneName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     schedulingdate = models.DateField(db_column='SchedulingDate')  # Field name made lowercase.
#     onroadbuses = models.IntegerField(db_column='OnRoadBuses', blank=True, null=True)  # Field name made lowercase.
#     oprbuses = models.IntegerField(db_column='OPRBuses', blank=True, null=True)  # Field name made lowercase.
#     plannedtrips = models.IntegerField(db_column='PlannedTrips', blank=True, null=True)  # Field name made lowercase.
#     plannedkm = models.FloatField(db_column='PlannedKM', blank=True, null=True)  # Field name made lowercase.
#     scheduletrips = models.IntegerField(db_column='ScheduleTrips', blank=True, null=True)  # Field name made lowercase.
#     schedulekm = models.FloatField(db_column='ScheduleKM', blank=True, null=True)  # Field name made lowercase.
#     losttrips = models.IntegerField(db_column='LostTrips', blank=True, null=True)  # Field name made lowercase.
#     lostkm = models.FloatField(db_column='LostKM', blank=True, null=True)  # Field name made lowercase.
#     unitperkm = models.FloatField(db_column='UnitPerKM', blank=True, null=True)  # Field name made lowercase.
#     tripefficiency = models.FloatField(db_column='TripEfficiency', blank=True, null=True)  # Field name made lowercase.
#     unitconsumptionsoc = models.FloatField(db_column='UnitConsumptionSOC', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'OPR_KMS'


# class OprKmssummary(models.Model):
#     kmssummaryid = models.AutoField(db_column='KMSSummaryId', primary_key=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
#     schedulingid = models.IntegerField(db_column='SchedulingId', blank=True, null=True)  # Field name made lowercase.
#     schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId', blank=True, null=True)  # Field name made lowercase.
#     schedulingdate = models.DateField(db_column='SchedulingDate', blank=True, null=True)  # Field name made lowercase.
#     shift = models.CharField(db_column='Shift', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     routeid = models.IntegerField(db_column='RouteId', blank=True, null=True)  # Field name made lowercase.
#     routename = models.CharField(db_column='RouteName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     routecode = models.CharField(db_column='RouteCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     scheduleid = models.IntegerField(db_column='ScheduleId', blank=True, null=True)  # Field name made lowercase.
#     schedulecode = models.CharField(db_column='ScheduleCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     buscode = models.CharField(db_column='BusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     vehicalno = models.CharField(db_column='VehicalNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
#     drivercode = models.CharField(db_column='DriverCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     drivername = models.CharField(db_column='DriverName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     plannedtrips = models.IntegerField(db_column='PlannedTrips', blank=True, null=True)  # Field name made lowercase.
#     plannedkm = models.FloatField(db_column='PlannedKM', blank=True, null=True)  # Field name made lowercase.
#     startodo = models.FloatField(db_column='StartODO', blank=True, null=True)  # Field name made lowercase.
#     endodo = models.FloatField(db_column='EndODO', blank=True, null=True)  # Field name made lowercase.
#     startsoc = models.FloatField(db_column='StartSOC', blank=True, null=True)  # Field name made lowercase.
#     endsoc = models.FloatField(db_column='EndSOC', blank=True, null=True)  # Field name made lowercase.
#     cbusinformationid = models.IntegerField(db_column='CBusInformationId', blank=True, null=True)  # Field name made lowercase.
#     cvehicalno = models.CharField(db_column='CVehicalNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cstartodo = models.FloatField(db_column='CStartODO', blank=True, null=True)  # Field name made lowercase.
#     cendodo = models.FloatField(db_column='CEndODO', blank=True, null=True)  # Field name made lowercase.
#     cstartsoc = models.FloatField(db_column='CStartSOC', blank=True, null=True)  # Field name made lowercase.
#     cendsoc = models.FloatField(db_column='CEndSOC', blank=True, null=True)  # Field name made lowercase.
#     c2businformationid = models.IntegerField(db_column='C2BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     c2vehicalno = models.CharField(db_column='C2VehicalNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     c2startodo = models.FloatField(db_column='C2StartODO', blank=True, null=True)  # Field name made lowercase.
#     c2endodo = models.FloatField(db_column='C2EndODO', blank=True, null=True)  # Field name made lowercase.
#     c2startsoc = models.FloatField(db_column='C2StartSOC', blank=True, null=True)  # Field name made lowercase.
#     c2endsoc = models.FloatField(db_column='C2EndSOC', blank=True, null=True)  # Field name made lowercase.
#     c3businformationid = models.IntegerField(db_column='C3BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     c3vehicalno = models.CharField(db_column='C3VehicalNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     c3startodo = models.FloatField(db_column='C3StartODO', blank=True, null=True)  # Field name made lowercase.
#     c3endodo = models.FloatField(db_column='C3EndODO', blank=True, null=True)  # Field name made lowercase.
#     c3startsoc = models.FloatField(db_column='C3StartSOC', blank=True, null=True)  # Field name made lowercase.
#     c3endsoc = models.FloatField(db_column='C3EndSOC', blank=True, null=True)  # Field name made lowercase.
#     totalodo = models.FloatField(db_column='TotalODO', blank=True, null=True)  # Field name made lowercase.
#     totalsoc = models.FloatField(db_column='TotalSOC', blank=True, null=True)  # Field name made lowercase.
#     socperkm = models.FloatField(db_column='SOCPerKM', blank=True, null=True)  # Field name made lowercase.
#     depottostart = models.FloatField(db_column='DepotToStart', blank=True, null=True)  # Field name made lowercase.
#     depottoclose = models.FloatField(db_column='DepotToClose', blank=True, null=True)  # Field name made lowercase.
#     atob = models.FloatField(db_column='AtoB', blank=True, null=True)  # Field name made lowercase.
#     btoa = models.FloatField(db_column='BtoA', blank=True, null=True)  # Field name made lowercase.
#     dt1 = models.IntegerField(db_column='DT1', blank=True, null=True)  # Field name made lowercase.
#     dt2 = models.IntegerField(db_column='DT2', blank=True, null=True)  # Field name made lowercase.
#     completedtrips = models.IntegerField(db_column='CompletedTrips', blank=True, null=True)  # Field name made lowercase.
#     completedkm = models.FloatField(db_column='CompletedKM', blank=True, null=True)  # Field name made lowercase.
#     losttrips = models.IntegerField(db_column='LostTrips', blank=True, null=True)  # Field name made lowercase.
#     lostkm = models.FloatField(db_column='LostKM', blank=True, null=True)  # Field name made lowercase.
#     shorttrips = models.IntegerField(db_column='ShortTrips', blank=True, null=True)  # Field name made lowercase.
#     shortkm = models.FloatField(db_column='ShortKM', blank=True, null=True)  # Field name made lowercase.
#     excesstrips = models.IntegerField(db_column='ExcessTrips', blank=True, null=True)  # Field name made lowercase.
#     excesskm = models.FloatField(db_column='ExcessKM', blank=True, null=True)  # Field name made lowercase.
#     deadtrips = models.IntegerField(db_column='DeadTrips', blank=True, null=True)  # Field name made lowercase.
#     deadkm = models.FloatField(db_column='DeadKM', blank=True, null=True)  # Field name made lowercase.
#     adeadkm = models.FloatField(db_column='ADeadKM', blank=True, null=True)  # Field name made lowercase.
#     lossatrips = models.FloatField(db_column='LossATrips', blank=True, null=True)  # Field name made lowercase.
#     lossbtrips = models.FloatField(db_column='LossBTrips', blank=True, null=True)  # Field name made lowercase.
#     lossctrips = models.FloatField(db_column='LossCTrips', blank=True, null=True)  # Field name made lowercase.
#     lossdtrips = models.FloatField(db_column='LossDTrips', blank=True, null=True)  # Field name made lowercase.
#     lossetrips = models.FloatField(db_column='LossETrips', blank=True, null=True)  # Field name made lowercase.
#     lossftrips = models.FloatField(db_column='LossFTrips', blank=True, null=True)  # Field name made lowercase.
#     lossatripskm = models.FloatField(db_column='LossATripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossbtripskm = models.FloatField(db_column='LossBTripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossctripskm = models.FloatField(db_column='LossCTripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossdtripskm = models.FloatField(db_column='LossDTripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossetripskm = models.FloatField(db_column='LossETripsKM', blank=True, null=True)  # Field name made lowercase.
#     lossftripskm = models.FloatField(db_column='LossFTripsKM', blank=True, null=True)  # Field name made lowercase.
#     isdiversion = models.BooleanField(db_column='IsDiversion', blank=True, null=True)  # Field name made lowercase.
#     diversionkm = models.FloatField(db_column='DiversionKM', blank=True, null=True)  # Field name made lowercase.
#     diversionreason = models.CharField(db_column='DiversionReason', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     buskm = models.FloatField(db_column='BusKM', blank=True, null=True)  # Field name made lowercase.
#     billingkm = models.FloatField(db_column='BillingKM', blank=True, null=True)  # Field name made lowercase.
#     status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
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
#         db_table = 'OPR_KMSSummary'


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


# class OprSchedulingdetailshistory(models.Model):
#     schedulingdetailshistoryid = models.AutoField(db_column='SchedulingDetailsHistoryId', primary_key=True)  # Field name made lowercase.
#     schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId', blank=True, null=True)  # Field name made lowercase.
#     schedulingid = models.IntegerField(db_column='SchedulingId', blank=True, null=True)  # Field name made lowercase.
#     scheduleid = models.IntegerField(db_column='ScheduleId', blank=True, null=True)  # Field name made lowercase.
#     starttime = models.CharField(db_column='StartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     endtime = models.CharField(db_column='EndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nooftrips = models.IntegerField(db_column='NoOfTrips', blank=True, null=True)  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     buscode = models.CharField(db_column='BusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     conductorid = models.IntegerField(db_column='ConductorId', blank=True, null=True)  # Field name made lowercase.
#     conductorname = models.CharField(db_column='ConductorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
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
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     islostremark = models.IntegerField(db_column='IsLostRemark', blank=True, null=True)  # Field name made lowercase.
#     islost = models.BooleanField(db_column='IsLost')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.
#     isclose = models.BooleanField(db_column='IsClose', blank=True, null=True)  # Field name made lowercase.
#     closeremark = models.CharField(db_column='CloseRemark', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     closedate = models.DateTimeField(db_column='CloseDate', blank=True, null=True)  # Field name made lowercase.
#     istransfer = models.BooleanField(db_column='IsTransfer', blank=True, null=True)  # Field name made lowercase.
#     cstartsoc = models.FloatField(db_column='CStartSOC', blank=True, null=True)  # Field name made lowercase.
#     cendsoc = models.FloatField(db_column='CEndSOC', blank=True, null=True)  # Field name made lowercase.
#     cstartodo = models.FloatField(db_column='CStartODO', blank=True, null=True)  # Field name made lowercase.
#     cendodo = models.FloatField(db_column='CEndODO', blank=True, null=True)  # Field name made lowercase.
#     clastodo = models.FloatField(db_column='CLastODO', blank=True, null=True)  # Field name made lowercase.
#     deletedperson = models.IntegerField(db_column='DeletedPerson', blank=True, null=True)  # Field name made lowercase.
#     deletedmacid = models.CharField(db_column='DeletedMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_SchedulingDetailsHistory'


# class OprSchedulingdetailstrip(models.Model):
#     schedulingdetailstripid = models.AutoField(db_column='SchedulingDetailsTripId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     scheduleid = models.IntegerField(db_column='ScheduleId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     scheduletripid = models.IntegerField(db_column='ScheduleTripId', blank=True, null=True, db_comment='Foreign Key')  # Field name made lowercase.
#     schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId', db_comment='Foreign Key')  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     starttime = models.CharField(db_column='StartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     astarttime = models.CharField(db_column='AStartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     endtime = models.CharField(db_column='EndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aendtime = models.CharField(db_column='AEndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fromstage = models.CharField(db_column='FromStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     tostage = models.CharField(db_column='ToStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     distanceinkm = models.FloatField(db_column='DistanceInKM', blank=True, null=True)  # Field name made lowercase.
#     adistanceinkm = models.FloatField(db_column='ADistanceInKM', blank=True, null=True)  # Field name made lowercase.
#     isdead = models.BooleanField(db_column='IsDead', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     islost = models.BooleanField(db_column='IsLost')  # Field name made lowercase.
#     isbuschange = models.BooleanField(db_column='IsBusChange', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.
#     isshort = models.BooleanField(db_column='isShort', blank=True, null=True)  # Field name made lowercase.
#     shortkm = models.FloatField(db_column='ShortKM', blank=True, null=True)  # Field name made lowercase.
#     isdiversion = models.BooleanField(db_column='IsDiversion', blank=True, null=True)  # Field name made lowercase.
#     diversionkm = models.FloatField(db_column='DiversionKM', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_SchedulingDetailsTrip'


# class OprSchedulingdetailstriphistory(models.Model):
#     schedulingdetailstriphistoryid = models.AutoField(db_column='SchedulingDetailsTripHistoryId', primary_key=True)  # Field name made lowercase.
#     schedulingdetailstripid = models.IntegerField(db_column='SchedulingDetailsTripId', blank=True, null=True)  # Field name made lowercase.
#     scheduleid = models.IntegerField(db_column='ScheduleId', blank=True, null=True)  # Field name made lowercase.
#     scheduletripid = models.IntegerField(db_column='ScheduleTripId', blank=True, null=True)  # Field name made lowercase.
#     schedulingdetailsid = models.IntegerField(db_column='SchedulingDetailsId')  # Field name made lowercase.
#     businformationid = models.IntegerField(db_column='BusInformationId', blank=True, null=True)  # Field name made lowercase.
#     starttime = models.CharField(db_column='StartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     astarttime = models.CharField(db_column='AStartTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     endtime = models.CharField(db_column='EndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aendtime = models.CharField(db_column='AEndTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fromstage = models.CharField(db_column='FromStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     tostage = models.CharField(db_column='ToStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     distanceinkm = models.FloatField(db_column='DistanceInKM', blank=True, null=True)  # Field name made lowercase.
#     adistanceinkm = models.FloatField(db_column='ADistanceInKM', blank=True, null=True)  # Field name made lowercase.
#     isdead = models.BooleanField(db_column='IsDead', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50)  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True)  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     islost = models.BooleanField(db_column='IsLost')  # Field name made lowercase.
#     isbuschange = models.BooleanField(db_column='IsBusChange', blank=True, null=True)  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.
#     isshort = models.BooleanField(db_column='isShort', blank=True, null=True)  # Field name made lowercase.
#     shortkm = models.FloatField(db_column='ShortKM', blank=True, null=True)  # Field name made lowercase.
#     isdiversion = models.BooleanField(db_column='IsDiversion', blank=True, null=True)  # Field name made lowercase.
#     diversionkm = models.FloatField(db_column='DiversionKM', blank=True, null=True)  # Field name made lowercase.
#     deletedperson = models.IntegerField(db_column='DeletedPerson', blank=True, null=True)  # Field name made lowercase.
#     deletedmacid = models.CharField(db_column='DeletedMacId', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_SchedulingDetailsTripHistory'


# class OprSchedulingmaster(models.Model):
#     schedulingmasterid = models.AutoField(db_column='SchedulingMasterId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     applicabledate = models.DateField(db_column='ApplicableDate')  # Field name made lowercase.
#     remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     entryperson = models.IntegerField(db_column='EntryPerson', db_comment='Login UaserId')  # Field name made lowercase.
#     entrymacid = models.CharField(db_column='EntryMacId', max_length=50, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     entrydate = models.DateTimeField(db_column='EntryDate', db_comment='Insertion Date')  # Field name made lowercase.
#     editperson = models.IntegerField(db_column='EditPerson', blank=True, null=True, db_comment='Login UserId')  # Field name made lowercase.
#     editmacid = models.CharField(db_column='EditMacId', max_length=50, blank=True, null=True, db_comment='IP Or Mac Address of Browser')  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True, db_comment='Updation Date')  # Field name made lowercase.
#     isdelete = models.BooleanField(db_column='IsDelete', db_comment='For Deletion operation 1=delet')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OPR_SchedulingMaster'




# class OprZone(models.Model):
#     zoneid = models.AutoField(db_column='ZoneId', primary_key=True, db_comment='Primery Key')  # Field name made lowercase.
#     companyid = models.ForeignKey(ConfigCompanymaster, models.DO_NOTHING, db_column='CompanyId', db_comment='Foreign Key')  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
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
#         db_table = 'OPR_Zone'














