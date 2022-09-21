from doctest import FAIL_FAST
from genericpath import exists
import json
import os.path, sys
from pickle import TRUE
from sre_constants import SUCCESS 

# Set up config file as class
class ConfigClass:
    # Creating flags to highlight success or fail during a function call
    SUCCESS = 0
    FAIL = -1

    def __init__(self):
        self.flag = 2
        self.__config_volatile = {}

    # Creating a default config file
    def default_config(self):
        default_config = {
            "API Config": {
                    "Key": "00000000", 
                    "URL": "http://0000.0000.0000.0000"
            },
            "Power Settings": {
                    "power" : 33,
                    "seq" : "default"
            },
            "Inventory Settings": {
                    "cycles" : 3,
                    "interval" : 5
            }
        }

        default_config = json.dumps(default_config)

        return default_config

    # Creating a checking function to see if config_temp.txt exists -> can insert additional checks here
    def check_config(self):
        try:
            check_file = open("config.json")
            self.flag =  ConfigClass.SUCCESS
            return self.flag
        except:
            self.flag = ConfigClass.FAIL
            return self.flag
    
    # Loading the config settings if file exists and if it doesn't,
    # it loads the default config file
    def load_config(self):
        file_check = self.check_config()

        if file_check == ConfigClass.SUCCESS:
            with open("config.json", "r") as json_data_file:
                self.__config_volatile = json.load(json_data_file)
                # print(data)
            return self.__config_volatile
        else:
            with open('config.json', "w+") as default_file:
                f = default_file.write(self.default_config())
                self.__config_volatile = json.loads(self.default_config())
                # print(f)
            return self.__config_volatile
    
    # Set config volatile value
    def set_config_volatile(self, config):
        self.__config_volatile = config
        return self.__config_volatile

    # When user requests config value, this function will fetch config volatile value
    def get_config_volatile(self):
        return self.__config_volatile

    def get_config_parsed_value(self, header, dict_key):
        value = 0
        if dict_key in self.__config_volatile[header]:
            value = self.__config_volatile[header][dict_key]
        return value

    def save_config(self):
        save_file = json.dumps(self.__config_volatile)
        with open('config.json', 'w') as save_settings:
            save_settings = save_settings.write(save_file)
        return save_settings

    # Creating an open file function to override new config settings
    def open_file(self, file_contents):
        with open('config.json', "w") as change_config:
            change_config = change_config.write(file_contents)
        return change_config
        
    # Creating a base function to change any classified key in the config file
    def change_config_value(self, header, dict_key, new_value):
        config_file = self.get_config_volatile()
        config_file[header][dict_key] = new_value
        altered_config_value = self.set_config_volatile(config_file)
        return altered_config_value




