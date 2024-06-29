from django.core.signals import request_finished
from django.dispatch import receiver
from .apps import db_connection

@receiver(request_finished)
def close_db_connection(sender, **kwargs):
    if db_connection is not None:
        db_connection.close_connection()