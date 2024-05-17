import requests

def run_device_details_view():
    url = "http://127.0.0.1:8000/vehical/DeviceDetailsView/"  
    headers = {"Content-Type": "application/json"} 
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Device details successfully updated.")
    else:
        print(f"Failed to update device details. Status code: {response.status_code}")


