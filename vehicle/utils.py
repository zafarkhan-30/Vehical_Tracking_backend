import requests
import json

access_token = None

def get_access_token():
    global access_token
    if access_token is None:
        refresh_access_token()
    return access_token

def refresh_access_token():
    global access_token
    headers = {"User-Agent": "iamdarksied"}
    params = {
        "client_id": "33OkryzDZsJ1Co4repIdtvGPurCexnGKFFge-SHVez21HwxLTNk5wgGze1lPMxmms7WoblbuZwxIXVnM_g-uEA==",
        "client_secret": "lrFxI-iSEg-dBY_dL3gjNlHjAVUuqEObcMHEjHIa9jrfvgT_qwnPhH4DfJQIT5j-MX0rDQFVqLG9iF5KXblWPs0torF2Cn7s",
        "grant_type": "client_credentials"
    }
    url = "https://outpost.mappls.com/api/security/oauth/token"
    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        access_token = json.loads(response.content).get('access_token')
        return access_token
    else:
        raise Exception("Failed to fetch access token")


def get_device_Data(refresh_token):
    url = "https://intouch.mapmyindia.com/iot/api/device"
    headers = {"Authorization": f"Bearer {refresh_token}"}

    response = requests.get(url, headers=headers)
    return response



from django.core.mail import EmailMessage
from VehicalTracking.settings import EMAIL_HOST_USER


class util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body= data['body'],
            from_email = EMAIL_HOST_USER,
            to = [data['to_email']]
        )
        email.send()