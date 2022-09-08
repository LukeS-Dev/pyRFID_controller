# This code is a prototype script to establish basic communication with a SensThys RFID reader.
import re
import requests
from config_files import*



# Creating Class set up
class readerSetup:
    api_power = "/stapi/v0/ant/pwr"
    api_timed_inv = "/stapi/v0/inv/timed"
    api_start_inv = "/stapi/v0/inv/start"
    api_stop_inv = "/stapi/v0/inv/stop"
    api_reader_info = "/stapi/v0/reader"

    # Building the address for SensAPI
    def build_endpoint(self, add_endpoint):
        return self.base_Url + add_endpoint

    # Initialising the class characteristics
    def __init__(self,api_base_url,
                 api_key,retries=3):
        self.api_key = api_key
        self.base_Url = api_base_url
        self.retries = retries
        self.headers = self.construct_Header()

    # Token to access the readers
    def construct_Header(self):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json;charset=utf-8'
        }
        return headers
    
    # Creating an extraction function template to get info from endpoints
    def extract_info(self, add_endpoint):
        r = requests.get(self.build_endpoint(add_endpoint), 
                                    headers = self.headers)
        return r

    # Attempt connection with the reader
    def attempt_connection(self):
        self.retries = 3

        for i in range(self.retries):
            r = requests.get(self.base_Url)
            if r.status_code == 200:
                print("Connected")
                return r
            elif i == 2:
                print("Connection to \
                RFID reader failed")
            else:
                print(f"Connection could \
                not be established. \
                Attempt to reconnect try {i}")

    # Getting the power of all antennas and readers
    def power(self):
        return self.extract_info(readerSetup.api_power)

    # Getting the power of a specific antenna
    def ant_power(self, id):
        return self.extract_info(readerSetup.api_power + '/{id}')

    # Starting the reading process until the stop command is sent
    def start_inv(self):
        return self.extract_info(readerSetup.api_start_inv)

    #Ending the reading process
    def stop_inv(self):
        return self.extract_info(readerSetup.api_stop_inv) 

    # Running a timed inventory 
    def timed_inv(self, set_time):
        return self.extract_info(readerSetup.api_timed_inv 
                         + '?timeframe=' + set_time)

 