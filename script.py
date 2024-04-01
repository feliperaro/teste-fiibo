"""
Script Challenge:
    Read data from xlsx file
    Send data to API
    Store data in database
"""
from datetime import datetime
from excel import read_xlsx
import glob
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
        -1: Invalid data type (data must be a dictionary).
        -2: Invalid API URL type (api_url must a string").
        -3: Network error during request.
        -4: API error (non-200 status code).
    """
    print("data", data)
    if not isinstance(data, dict):
        print("Invalid data type. data must be a dictionary.")
        return -1

    print("api_url", api_url)
    if not isinstance(api_url, str):
        print("Invalid api_url type.")
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
    """
    Main function to read Excel data and send it to the API.
    TODO: Read CSV files from input folder
    TODO: Write RPA result to output file 
    TODO: Send errors to errors folder
    """
    api_url = gvars.API_URL

    input_folder = gvars.INPUT_DIR
    if not os.path.exists(input_folder):
        print(f"input_folder '{input_folder}' does not exist")
        return 0
    
    input_files = glob.glob(os.path.join(input_folder, '*.xlsx'))
    if not input_files or len(input_files) == 0:
        print(f"input_folder has no files")
        return 0
    
    for input_file in input_files:
        print(f"input_file '{input_file}'")

        xlsx_data = read_xlsx(input_file)
        if isinstance(xlsx_data, int) and xlsx_data < 0:
            print("error reading input_file", input_file)
            continue

        if not xlsx_data:
            print("No data found in the Excel file.")
            continue

        for data in xlsx_data:
            data["pendente"] = True
            return_send_data_to_api = send_data_to_api(data, api_url)
            if return_send_data_to_api == 1:
                data["rpa"] = "success"
                print("success sending data to api!")
            else:
                print("error sending data to api!")
                data["rpa"] = "error"
            
        try:
            filename = os.path.basename(input_file)
            current_time = datetime.now().strftime("%Y%m%d%H%M%S")

            output_folder = gvars.OUTPUT_DIR
            new_folder_path = os.path.join(output_folder, current_time)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            new_file_path = os.path.join(new_folder_path, filename)
            print("new_file_path", new_file_path)
            shutil.move(input_file, new_file_path)
        except Exception as error:
                print("Error moving file to output directory", error)

    return 1


if __name__ == "__main__":
    main()
