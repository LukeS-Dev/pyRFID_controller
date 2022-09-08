import json 

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
