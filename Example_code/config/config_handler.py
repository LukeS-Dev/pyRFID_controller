import os 
import json

class ConfigHandler: 
    #Macros
    SUCCESS = 0
    FAIL = -1

    #TODO 
    #-Defined Required Values
    #-Search function that iterates through all parameters to make sure they are of correct type.

    #Make a default configuration.
    default_config = {
        'api' : {
            'key': '00000000',
            'url': '192.168.0.1'
        },
        'inv' : {
            'read_interval' : 60,
            'cycles' : 1
        },
        'ant' : {
            'power' : 24,
            'seq' : 'default'
        }
    }

    def __init__(self,filename='config.json'):
        ### Private
        self.__config_volatile = {} 
        
        ### Public
        self.filename = filename
        #Volatile config will be the variable we use to store and manipulate the config file.
        #In our code. Once we save the config file with the save_config() method, it becomes.
        #persistent.
        self.set_config_volatile(self.load_config())
        print(self.get_config_volatile()) #Debug code - This prints the current config

    def check_for_existing_config(self):
        #Checks if file exists, if not we create a default configuration file.
        isFile = os.path.isfile(self.filename)
        if isFile == False: 
            with open(self.filename,'w+') as file: 
                default_config = json.dumps(ConfigHandler.default_config)
                file.write(default_config)

    def set_config_volatile(self,config):
        self.__config_volatile = config

    def get_config_volatile(self):
        return self.__config_volatile

    def load_config(self):
        #Check if config file exists, if not then we create and load defaults.
        self.check_for_existing_config()

        #Reads the configuration file and saves 
        with open(self.filename) as file:
            loaded_configuration = file.read()
        return json.loads(loaded_configuration)

    def save_config(self):
        try:
            with open(self.filename,'w') as file:
                save_data = json.dumps(self.get_config_volatile())
                file.write(save_data)
            return ConfigHandler.SUCCESS
        except: 
            return ConfigHandler.FAIL

    def set_config_value(self,classification,element,value):
        try: 
            current_config = self.get_config_volatile()
            current_config[classification][element] = value
            self.set_config_volatile(current_config)
            return ConfigHandler.SUCCESS
        except:
            return ConfigHandler.FAIL

    def get_config_value(self,classification,element):
        value = "Nan"
        current_config = self.get_config_volatile()
        if classification in current_config.keys(): 
            if element in current_config[classification].keys():
                value = current_config[classification][element]
        return value

if __name__ == '__main__':
    myConfig = ConfigHandler()

    #We can get and set configuration settings.
    print(myConfig.get_config_value("api","key"))
    myConfig.set_config_value("api","key","AAAAAAAAA")
    print(myConfig.get_config_value("api","key"))

    
    print_full_config = True

    #I am printing stuff here, but we can use this in other code to "Load" our settings.
    if print_full_config == True:
        print("Api Key          : ",myConfig.get_config_value("api","key"))
        print("base Url         : ",myConfig.get_config_value("api","url"))
        print("read Interval    : ",myConfig.get_config_value("inv","read_interval"))
        print("read cycles      : ",myConfig.get_config_value("inv","cycles"))
        print("antenna power    : ",myConfig.get_config_value("ant","power"))
        print("antenna sequenc  : ",myConfig.get_config_value("ant","seq"))

    #Save config writes config to file.
    myConfig.save_config()



    