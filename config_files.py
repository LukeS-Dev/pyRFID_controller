import json 

#Don't use try except here, you want to create the config on a per element basis. 
#The structure of this configuration handler will cause issues in the future.
#For example. If ONE config element is missing, it will OVERWRITE the FULL configuration file
#With this implementation.

#I'll work on an alterantive implementation in the future, but this is an example of how I would implement

"""
with open("RFID_config.json) as json_data_file:
    data = json.load(json_data_file)

#This will create a dictionary of keys
config_keys = data.keys()

if "API Key" in config_keys: 
    api_key = config_keys
    

"""

try:
    with open("RFID_config.json") as json_data_file:
        data = json.load(json_data_file)

    config = data.get("config")
    api_key = config.get("API Key")
    api_base_url = config.get("RFID URL")
except:
    config_file = { "config":{ 
                "API Key":"XXXXXXXX", 
                "RFID URL":"http://XXXX.XXXX.XXXX.XXXX"
                } 
             }

    with open("config_temp.json", 'w') as json_data_file:
        json.dump(config_file, json_data_file)

    with open("config_temp.json") as json_data_file:   
        data = json.load(json_data_file)
    
    config = data.get("config")
    api_key = config.get("API Key")
    api_base_url = config.get("RFID URL")
    

# print(data.get("config").get("API Key"))
# print(api_base_url)
