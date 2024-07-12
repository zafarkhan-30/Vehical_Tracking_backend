from django.apps import AppConfig
from .db_connection import  DatabaseConnection

class SchedulingmgmtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedulingMgmt'


