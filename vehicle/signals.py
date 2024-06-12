from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from database.models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# @receiver(post_save , sender = test_models)
# def test_post_save(sender,instance,  created , **kwargs):
#     print(instance)
#     print(created)
#     if created:
#         print("Created successfully inside" )



# @receiver(post_save, sender=test_models)
# def send_location_update(sender, instance, created, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()
#         data = {
#             # 'latitude': instance.latitude,
#             # 'longitude': instance.longitude,
#             'test1': instance.test1,
#         }
#         print(data)
#         async_to_sync(channel_layer.group_send)(
#             'location_group',
#             {
#                 'type': 'send_location_data',
#                 'data': data
#             }
#         )