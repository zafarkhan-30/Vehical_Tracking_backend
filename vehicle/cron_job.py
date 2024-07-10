import requests
import certifi
from django.core.management.base import BaseCommand
from django.test import RequestFactory
from .views import PostMasterDeviceData


def run_device_details_view():
    url = "https://timscan.transvolt.in/vehical/post-Master-Device-Data/"
    headers = {"Content-Type": "application/json"}
    log_file = "/tmp/cron_job_output.log"

    view = PostMasterDeviceData()
    get = view.get()
    


    try:
        response = requests.get(url, headers=headers , verify=False)
        with open(log_file, "a") as f:
            if response.status_code == 200:
                f.write("Device details successfully updated.\n")
            else:
                f.write(f"Failed to update device details. Status code: {response.status_code}\n")
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"An error occurred: {str(e)}\n")



# class Command(BaseCommand):
#     help = 'Updates device details by calling the PostMasterDeviceData get method'

#     def handle(self, *args, **kwargs):
#         factory = RequestFactory()
#         request = factory.get('/fake-url/')
#         view = PostMasterDeviceData.as_view()
#         response = view(request)
#         log_file = "/tmp/cron_job_output.log"
#         with open(log_file, "a") as f:
#             if response.status_code == 200:
#                 f.write("Device details successfully updated.\n")
#             else:
#                 f.write(f"Failed to update device details. Status code: {response.status_code}\n")


# a = Command
# print(a.handle())