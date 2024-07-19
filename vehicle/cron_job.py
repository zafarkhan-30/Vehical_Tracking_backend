import requests



def run_device_details_view():
    url = "https://timscan.transvolt.in/vehical/post-Master-Device-Data/"
    headers = {"Content-Type": "application/json"}
    log_file = "/tmp/cron_job_output.log"

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



