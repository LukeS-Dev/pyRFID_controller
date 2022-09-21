from Reader_Class import* 
import logging
import json
import time
import Config_Handler
import collections
from datetime import datetime
import time

# Logging file setup
file_name = 'Reader.log'
logging.basicConfig(filename=file_name, 
                        level=logging.INFO,
                        format='%(levelname)s:%(asctime)s:%(message)s')


# Main function loop
if __name__ == '__main__':
    # Initialise variables
    id_1 = '1'
    id_2 = '2'
    id_3 = '3'
    id_4 = '4'

    ant_order = [0,1,2,3]
    total_interval = 1

    r_inv = {}

    now = datetime.now()

    # Initialising reader class
    api_base_url = Config_Handler.api_url
    api_key = Config_Handler.api_key
    reader = ReaderClass(api_base_url, api_key)

    attempt = reader.attempt_connection()
    # r_set_power = reader.set_all_power(10)
    r_power = reader.power()
    


    #Reading in timed intervals 
    for i in range(total_interval):
        r_inv = reader.timed_inv('3000')
        time.sleep(3)

    inv_data = r_inv.text
    parsed_inv_data = json.loads(inv_data)

    # Setting log file to read EPC values and the read count associated with each tag read (Count includes which antenna read it)
    counter = 0
    epc_array = []
    count_array = []
    seen = set()
    uniq = []
    current_time = []
    # Create EPC read + Read count associated with each antenna for that tag + time elapsed + Number of Unique Tags Read
    for items_read in parsed_inv_data:
        epc_values = parsed_inv_data[counter]["epc"]
        count = parsed_inv_data[counter]["count"]
        
        epc_array.append(epc_values)
        count_array.append(count)
        current_time.append(now.strftime("%H:%M:%S"))
        logging.info('EPC Read: {} \n Read Count: {} '
                            .format(epc_values, count))

        now = datetime.now()
        if counter <= len(parsed_inv_data)-1:
            counter+=1

    for i in epc_array:
            if i not in seen:
                uniq.append(i)
                seen.add(i)
    
    total_unique_tags = len(uniq)
    # current_time = now.strftime("%H:%M:%S")
    # Setting up dictionary to store only EPC values and read counts 
    epc_count_dict = [{"Current Time": current_time[i], "EPC Value":epc_array[i], "Count":count_array[i]}
                                         for i in range(len(epc_array))]
    
    
    # print(epc_count_dict)

    # print(uniq)
    print(total_unique_tags)
    print(epc_count_dict)
    # print(len(seen))
    # print(seen)

    # Setting the power to all antennas simultaneously for both reading and writing power
    set_power = reader.set_all_power(33,33)    
    # print(set_power.text)

    # Setting up the ant sequence
    ant_sequence = reader.set_ant_seq(ant_order)
    # print(ant_sequence.text)

    # Setting up the dwell time in milliseconds -> ant dwell time is the time interval.
    # That the reader spends reading tags on a specific antenna before moving on to read.
    # on the next antenna sequence.
    dwell_interval = reader.dwell_time(500)
    # print(dwell_interval.text)

