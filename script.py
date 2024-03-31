"""
Script Challenge:
    Read data from xlsx file
    Send data to API
    Store data in database
"""
from datetime import datetime
from excel import read_xlsx
import gvars
import os
import shutil
import requests

def send_data_to_api(data, api_url):
    """Sends a dictionary containing data to the API.

    Args:
        data: A dictionary representing the data to send.
        api_url: The URL of the API endpoint.

    Returns:
        1: Success.
        -1: Invalid data format (data must be a dictionary).
        -2: Invalid API URL format (must start with "http").
        -3: Network error during request.
        -4: API error (non-200 status code).
    """
    print("data", data)
    if not isinstance(data, dict):
        print("Invalid data format. Data must be a dictionary.")
        return -1

    print("api_url", api_url)
    if not isinstance(api_url, str):
        print("Invalid API URL format.")
        return -2

    try:
        response = requests.post(api_url, json=data, timeout=60)
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return -3

    if response.status_code != 201:
        print("API error:", response.status_code, response.text)
        return -4

    print("Data sent successfully!")
    return 1


def main():
    """Main function to read Excel data and send it to the API."""
    api_url = gvars.API_URL
    file_path = gvars.EXCEL_FILEPATH
    if not os.path.exists(file_path):
        print(f"file_path '{file_path}' does not exist")
        return 0

    xlsx_data = read_xlsx(file_path)
    if not xlsx_data:
        print("No data found in the Excel file.")
        return 0

    for data in xlsx_data:
        data["pendente"] = True
        return_send_data_to_api = send_data_to_api(data, api_url)
        if return_send_data_to_api != 1:
            print("error sending data to api!")

    try:
        filename = os.path.basename(file_path)
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")

        output_folder = gvars.OUTPUT_DIR
        new_folder_path = os.path.join(output_folder, current_time)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        new_file_path = os.path.join(new_folder_path, filename)
        print("new_file_path", new_file_path)
        shutil.move(file_path, new_file_path)
    except Exception as error:
        print("Error moving file to output directory", error)

    return 1


if __name__ == "__main__":
    main()
