from ConfigClass import ConfigHandler
from tkinter import *
from tkinter import ttk

#This will open a GUI that lets us set our config file.

config = ConfigHandler()

root = Tk()
root.geometry("300x300")

ttk.Label(root,text="RFID Settings ",font=('Calibri',24),relief=RIDGE,borderwidth=12,width=18).pack(pady=15)
config_frame = ttk.Frame(root,relief=RIDGE,borderwidth=10)
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

ttk.Label(config_frame,text="Api Key").grid(row=0,column=0,sticky='w')
entry_key = ttk.Entry(config_frame,textvariable=api_key)
entry_key.grid(row=0,column=1,padx=2,pady=2)

ttk.Label(config_frame,text="Base URL").grid(row=1,column=0,sticky='w')
entry_url = ttk.Entry(config_frame,textvariable=api_url)
entry_url.grid(row=1,column=1,padx=2,pady=2)

ttk.Label(config_frame,text="Inv read interval").grid(row=2,column=0,sticky='w')
entry_url = ttk.Entry(config_frame,textvariable=inv_interval)
entry_url.grid(row=2,column=1,padx=2,pady=2)

ttk.Label(config_frame,text="Read cycles").grid(row=3,column=0,sticky='w')
entry_url = ttk.Entry(config_frame,textvariable=inv_cycles)
entry_url.grid(row=3,column=1,padx=2,pady=2)

ttk.Label(config_frame,text="Antenna Power").grid(row=4,column=0,sticky='w')
entry_url = ttk.Entry(config_frame,textvariable=ant_power)
entry_url.grid(row=4,column=1,padx=2,pady=2)

ttk.Label(config_frame,text="Antenna Sequence").grid(row=5,column=0,sticky='w')
entry_url = ttk.Entry(config_frame,textvariable=ant_seq)
entry_url.grid(row=5,column=1,padx=20,pady=2)

ttk.Button(config_frame,text="Save",command=save_config_gui).grid(row=6,column=0,columnspan=2,padx=2,pady=12)

root.mainloop()