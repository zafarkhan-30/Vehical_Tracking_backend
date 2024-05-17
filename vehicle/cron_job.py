import requests

def run_device_details_view():
    url = "http://timscan.transvolt.in/vehical/post-Device-Details/"  
    headers = {"Content-Type": "application/json"} 
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Device details successfully updated.")
    else:
        print(f"Failed to update device details. Status code: {response.status_code}")


