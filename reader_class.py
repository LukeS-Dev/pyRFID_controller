# This file contains a prototype version for the RFID class set up for a SensThys reader
from email import header
import re
import requests

# Creating Class set up
class ReaderClass:
    api_power = "/stapi/v0/ant/pwr"
    api_timed_inv = "/stapi/v0/inv/timed"
    api_start_inv = "/stapi/v0/inv/start"
    api_stop_inv = "/stapi/v0/inv/stop"
    api_reader_info = "/stapi/v0/reader"
    api_reboot = "/stapi/v0/reader/boot"
    api_ant_seq = "/stapi/v0/ant/seq"
    api_dwell = "/stapi/v0/ant/dwell"

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

    # Creating a post function template to alter settings at endpoint
    def change_settings(self, add_endpoint, payload):
        r = requests.post(self.build_endpoint(add_endpoint),
                        headers = self.headers, json = payload)
                                                # data = payload)
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
# ---------------------- Power Settings and Information ---------------------- #
    # Getting the power of all antennas and readers
    def power(self):
        return self.extract_info(ReaderClass.api_power)

    # Getting the power of a specific antenna
    def ant_power(self, id):
        return self.extract_info(ReaderClass.api_power 
                                            + '/{id}')

    #Set power levels simultaneously to all antennas/reader for both writing and reading power
    def set_all_power(self, all_read_power, all_write_power): 
        payload = [{
                        "antenna_id": 0, 
                        "read_power": all_read_power,
                        "write_power": all_write_power
                    }, {
                        "antenna_id": 1, 
                        "read_power": all_read_power,
                        "write_power": all_write_power
                    }, {
                        "antenna_id": 2, 
                        "read_power": all_read_power,
                        "write_power": all_write_power
                    }, {
                        "antenna_id": 3, 
                        "read_power": all_read_power,
                        "write_power": all_write_power
                    }
                    ]
        return self.change_settings(ReaderClass.api_power, payload)
    
    # Set individual power levels for each antenna
    def set_single_antenna_power(self, id, single_read_power, single_write_power):
        payload = [{
                        "antenna_id": id, 
                        "read_power": single_read_power,
                        "write_power": single_write_power
                     }]
        return self.change_settings(self.api_power, payload)

# ------------------- RFID Start, Stop, and Timed Inventory ------------------ #
    # Starting the reading process until the stop command is sent
    def start_inv(self):
        return self.extract_info(ReaderClass.api_start_inv)

    #Ending the reading process
    def stop_inv(self):
        return self.extract_info(ReaderClass.api_stop_inv) 

    # Running a timed inventory 
    def timed_inv(self, set_time):
        return self.extract_info(ReaderClass.api_timed_inv 
                         + '?timeframe=' + set_time)
# ---------------------- Antenna Sequence and Dwell Time --------------------- #
    # Getting the antenna sequence 
    def get_ant_seq(self):
        return self.extract_info(self.api_ant_seq)

    # Specifying the sequency order. Eg. A single antenna would be a single element.
    def set_ant_seq(self, ant_order):
        payload = ant_order
        return self.change_settings(self.api_ant_seq, payload)
    
    #Set antenna dwell time
    def dwell_time(self, dwell_period):
        payload = {
                     "dwell_time": dwell_period
                    }
        return self.change_settings(self.api_dwell, payload) 

# ------------------------------ Reboot Command ------------------------------ #
    # Reboot the reader
    def reboot(self):
        return self.extract_info(self.api_reboot)


 
