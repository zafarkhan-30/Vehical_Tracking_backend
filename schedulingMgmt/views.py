
from .db_connection import  DatabaseConnection
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import json
from rest_framework.views import APIView
db_config = {
            'server': '103.248.60.42',
            'database': 'ITMS',
            'username': 'sa',
            'password': 'vtpl@123',
            'driver': '{ODBC Driver 17 for SQL Server}'
        }


db_connection  = DatabaseConnection(**db_config)

class GetRoutelistView(APIView):
    
    serializer_class = None
    def get(self ,request):
        connection = db_connection.get_connection()
        cursor = connection.cursor()
        
        # Example query
        cursor.execute("SELECT * FROM OPR_Schedule;")
        rows = cursor.fetchall()
        
        return None
    





