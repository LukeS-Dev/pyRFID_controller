# This code is a prototype script to establish basic communication with a SensThys RFID reader.
import re
import requests
import time
import logging
from config_files import*

# Logging function
logging.basicConfig(filename='Reader.log', level=logging.INFO,
                            format='%(levelname)s:%(asctime)s:%(message)s')

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

# Main function loop
if __name__ == '__main__':
    id_1 = '1'
    id_2 = '2'
    id_3 = '3'
    id_4 = '4'

    # Setting up reader object
    reader = readerSetup(api_base_url, api_key)


    attempt = reader.attempt_connection()
    r_power = reader.power()
    
    total_interval = 1
    
    #Reading in timed intervals 
    for i in range(total_interval):
        r_inv = reader.timed_inv('1500')
        time.sleep(3)

    inv_data = r_inv.text
    parse_inv_data = json.loads(inv_data)

    # Setting log file to read EPC values and the read count associated with each tag read (Count includes which antenna read it)
    counter = 1

    for items_read in parse_inv_data:
        epc_values = parse_inv_data[counter]["epc"]
        count = parse_inv_data[counter]["count"]

        # print(epc_values)
        # print(count)
        
        logging.info('EPC Read: {} \n Read Count: {} '.format(epc_values, count))

        if counter < len(parse_inv_data)-1:
            counter+=1


    print(r_power.text)
    print(r_inv.text)
