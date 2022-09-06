import json 

with open("RFID_config.json") as json_data_file:
    data = json.load(json_data_file)

config = data.get("config")
api_key = config.get("API Key")
api_base_url = config.get("RFID URL")
# print(data.get("config").get("API Key"))
# print(api_base_url)
