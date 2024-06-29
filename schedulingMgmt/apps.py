from django.apps import AppConfig
from .db_connection import  DatabaseConnection

class SchedulingmgmtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedulingMgmt'


    # def ready(self):
    #     # Initialize and connect to the database when the app is ready
    #     global db_connection
    #     server = '103.248.60.42'
    #     database = 'ITMS'
    #     username = 'sa'
    #     password = 'vtpl@123'
    #     driver = '{ODBC Driver 17 for SQL Server}' 

    #     if db_connection is None:
    #         db_connection = DatabaseConnection(server, database, username, password)
    #         db_connection.connect()

    #     # Ensure the connection is closed when the server stops
    #     import schedulingMgmt.signals  # This will trigger the import of signals.py where we handle the closing
