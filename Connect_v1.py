# This code is a prototype script to establish basic communication with a SensThys RFID reader.
import re
import requests
import time
from config_files import*



class readerSetup:
    api_power = "/stapi/v0/ant/pwr"
    api_inv = "/stapi/v0/inv/timed"

    def build_endpoint(self, add_endpoint):
        return self.base_Url + add_endpoint

    def __init__(self,api_base_url,
                 api_key,retries=3):
        self.api_key = api_key
        self.base_Url = api_base_url
        self.retries = retries
        self.headers = self.construct_Header()

    def construct_Header(self):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json;charset=utf-8'
        }
        return headers

    def extract_info(self, add_endpoint):
        r = requests.get(self.build_endpoint(add_endpoint), 
                                    headers = self.headers)
        return r

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

    def power(self):
        return self.extract_info(readerSetup.api_power)
    # Extracting the power of the reader


    # Running a timed inventory 
    def timed_inv(self, set_time):
        return self.extract_info(readerSetup.api_inv + '?timeframe=' + set_time)


if __name__ == '__main__':
    reader = readerSetup(api_base_url, api_key)
    attempt = reader.attempt_connection()
    r_power = reader.power()
    
    total_interval = 5
    for i in range(total_interval):
        r_inv = reader.timed_inv('1500')
        time.sleep(10)

    print(r_power.text)
    print(r_inv.text)
