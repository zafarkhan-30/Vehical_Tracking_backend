import requests
import json



def format_error_message(errors):
    try:
        error_dict = errors[0]
        print(error_dict)
        key, value = list(error_dict.items())[0]
        if isinstance(value, list) and value:
            error_detail = value[0]
            
            if hasattr(error_detail, 'string'):
                error_message = f"{key}, {error_detail.string}"
            else:
                error_message = f"{key}, {str(error_detail)}"
        else:
            error_message = f"{key}, {str(value)}"
        
    except Exception as e:
        error_message = str(e)
    return error_message


def deep_flatten(lst):
    
    flat = []
    print(lst)
    
    while lst:
        val = lst.pop()
        if isinstance(val,list):
            lst.extend(val)
        else:
            flat.append(val)

    return flat


def error_simplifier(error_dict):
    error_key = error = ""
    value = []
    for key,val in error_dict.items():
        error_key = key
        error = val
        break

    if isinstance(error,str):
        if "field" in error:
            return error_key + ", " + error
        return error
    else:
        value = deep_flatten(error)
        if "field" in value:
            return error_key + ", " + value[0]
        return value[0]



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