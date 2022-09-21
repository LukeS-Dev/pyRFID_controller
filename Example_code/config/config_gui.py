from ConfigClass import ConfigHandler
from tkinter import *
from tkinter import ttk

#This will open a GUI that lets us set our config file.

config = ConfigHandler()

root = Tk()
root.geometry("300x300")

config_frame = ttk.Frame(root)
config_frame.pack()

#Initialize constants.
api_key = StringVar()
api_url = StringVar()
inv_interval = StringVar()
inv_cycles = StringVar()
ant_power = StringVar()
ant_seq = StringVar()

#Get values from configuration file.
api_key.set(config.get_config_value("api","key"))
api_url.set(config.get_config_value("api","url"))
inv_interval.set(config.get_config_value("inv","read_interval"))
inv_cycles.set(config.get_config_value("inv","cycles"))
ant_power.set(config.get_config_value("ant","power"))
ant_seq.set(config.get_config_value("ant","seq"))

def save_config_gui():
    config.set_config_value("api","key",api_key.get())
    config.set_config_value("api","url",api_url.get())
    config.set_config_value("inv","read_interval",inv_interval.get())
    config.set_config_value("inv","cycles",inv_cycles.get())
    config.set_config_value("ant","power",ant_power.get())
    config.set_config_value("ant","seq",ant_seq.get())

    #Save config
    config.save_config()
    print(config.get_config_volatile())

ttk.Label(config_frame,text="Api Key").pack()
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

root.mainloop()