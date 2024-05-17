from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(devices)
admin.site.register(deviceLocation)

admin.site.register(canInfo)
admin.site.register(alerts)
admin.site.register(deviceStatus)