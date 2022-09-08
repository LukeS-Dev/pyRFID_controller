from Reader_Class import*
import logging
import json
import time

# Logging function
logging.basicConfig(filename='Reader.log', level=logging.INFO,
                            format='%(levelname)s:%(asctime)s:%(message)s')

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
        
        logging.info('EPC Read: {} \n Read Count: {} '
                            .format(epc_values, count))

        if counter < len(parse_inv_data)-1:
            counter+=1
    

    print(r_power.text)
    print(r_inv.text)
