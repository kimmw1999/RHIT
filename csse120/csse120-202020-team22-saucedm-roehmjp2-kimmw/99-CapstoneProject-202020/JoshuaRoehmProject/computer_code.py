

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com

def main():
    gui_constructor()


def gui_constructor():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_mqtt_to_talk_to_robot()

    root = tkinter.Tk()
    root.title("Josh's Project")
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()


    label = ttk.Label(main_frame,text="welcome to Josh's Project")

    #creating buttons
    start_button = ttk.Button(main_frame,text="Start!")
    stop_button = ttk.Button(main_frame,text="Stop!")

    #creating radio buttons
    radio_frame = ttk.Frame(main_frame,borderwidth = 15,relief="groove")
