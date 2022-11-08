from typing import Container
# from ConfigClass import ConfigClass
import config_handler
from tkinter import *
from tkinter import ttk

# Accessing the config file
config = config_handler.config_opener

# Application Name
win = Tk() 

# Setting up window size
win.geometry("300x300")

# Application Name
win.title("Config Settings")

config_frame = ttk.Frame(win)
config_frame.pack()

# Initializing constants
api_key = StringVar()
api_url = StringVar()
inv_interval = StringVar()
inv_cycles = StringVar()
ant_power = StringVar()
ant_seq = StringVar()

# Get values from configuration file
api_key.set(config.get_config_parsed_value('API Config', 'Key'))
api_url.set(config.get_config_parsed_value('API Config', 'URL'))
inv_interval.set(config.get_config_parsed_value('Inventory Settings', 'interval'))
inv_cycles.set(config.get_config_parsed_value('Inventory Settings', 'cycles'))
ant_power.set(config.get_config_parsed_value('Power Settings', 'power'))
ant_seq.set(config.get_config_parsed_value('Power Settings', 'seq'))

# Create save function
def save_config_gui():
    config.change_config_value('API Config', 'Key', api_key.get())
    config.change_config_value('API Config', 'URL', api_url.get())
    config.change_config_value('Inventory Settings', 'interval', inv_interval.get())
    config.change_config_value('Inventory Settings', 'cycles', inv_cycles.get())
    config.change_config_value('Power Settings', 'power', ant_power.get())
    config.change_config_value('Power Settings', 'seq', ant_seq.get())

    print(config.get_config_volatile())
    # Save all changed settings
    config.save_config()

ttk.Label(config_frame,text="API Key").pack()
entry_key = ttk.Entry(config_frame,textvariable=api_key)
entry_key.pack()

ttk.Label(config_frame,text="Base URL").pack()
entry_url = ttk.Entry(config_frame,textvariable=api_url)
entry_url.pack()

ttk.Label(config_frame,text="Inventory read interval").pack()
entry_url = ttk.Entry(config_frame,textvariable=inv_interval)
entry_url.pack()

ttk.Label(config_frame,text="Read cycles").pack()
entry_url = ttk.Entry(config_frame,textvariable=inv_cycles)
entry_url.pack()

ttk.Label(config_frame,text="Antenna Power").pack()
entry_url = ttk.Entry(config_frame,textvariable=ant_power)
entry_url.pack()

ttk.Label(config_frame,text="Antenna Sequence").pack()
entry_url = ttk.Entry(config_frame,textvariable=ant_seq)
entry_url.pack()

ttk.Button(config_frame,text="Save",command=save_config_gui).pack()

win.mainloop()