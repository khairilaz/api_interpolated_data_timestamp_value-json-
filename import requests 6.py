import requests
from requests.auth import HTTPBasicAuth
import json

# Updated URL for GetInterpolated data
url = "https://win-a6rtrd7niso/piwebapi/streams/F1AbEg6hcEhn5_kiAIbZ9w6Ub4ATniv6_aX7hGMgAgAJ_JtwgGSVtqkX1qUGD5sgAfpoWXAV0lOLUE2UlRSRDdOSVNPXEpYTlxKWE5cMS4xIENPTkRFTlNBVEUgRVNDQVBFfENPTkRZIFBSRVNTVVJF/interpolated"

# Authentication details
username = "administrator"
password = "P@ssw0rd"

# Define the start and end time for the data range
start_time = "2023-11-01T00:00:00Z"
end_time = "2023-11-02T00:00:00Z"

# Interval to get approximately 30 data points
interval = "1h"  # Adjust as needed

# Parameters for the interpolated request
params = {
    "startTime": start_time,
    "endTime": end_time,
    "interval": interval
}

# Send a GET request to the interpolated data API with SSL verification disabled
try:
    response = requests.get(url, auth=HTTPBasicAuth(username, password), params=params, verify=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data and extract only Timestamp and Value
        data = response.json().get("Items", [])
        filtered_data = [{"Timestamp": entry["Timestamp"], "Value": entry["Value"]} for entry in data]
        
        # Write filtered JSON data to a .txt file
        with open("api_interpolated_data_timestamp_value.txt", "w") as file:
            json.dump(filtered_data, file, indent=4)
        
        print("Filtered data (Timestamp and Value only) successfully saved to api_interpolated_data_timestamp_value.txt.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")


