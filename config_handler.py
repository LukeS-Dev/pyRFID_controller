from config_class import ConfigClass

config_opener = ConfigClass()
config_load = config_opener.load_config()
# config_change = config_opener.change_config_value('API Config', 'Key', 'abcdefgh')
config_opener.save_config()

# Saving variables for accesbility in Reader Class
content = config_opener.get_config_volatile()

api_key = content['API Config']['Key']
api_url = content['API Config']['URL']
# change_key = config_opener.change_API_key('xxxxxxxx')


# ---------------------------- Testing Statements ---------------------------- #
# print(config_load.load())
file = open("config.json")
file_contents = file.read()
print(api_key)
print(api_url)
print(file_contents)
