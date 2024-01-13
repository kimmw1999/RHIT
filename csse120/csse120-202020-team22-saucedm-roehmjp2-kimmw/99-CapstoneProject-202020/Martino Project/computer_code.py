import tkinter
from tkinter import ttk
import time
import mqtt_remote_method_calls as com

def main():
    # -------------------------------------------------------------------------
    # DONE: 2. Setup an mqtt_client.  Notice that since you don't need to receive any messages you do NOT need to have
    #  an argument  class.  Simply construct the MqttClient with no parameter in the constructor (easy).
    # -------------------------------------------------------------------------
    mqtt_client = com.MqttClient()


    # -------------------------------------------------------------------------
    # DONE: 3. Connect to talk to the robot
    # -------------------------------------------------------------------------
    mqtt_client.connect_to_mqtt_to_talk_to_robot()

    root = tkinter.Tk()
    root.title("Martino Kim Project")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    explain_label= ttk.Label(main_frame, text="Hello. Let's start a game.\n"
                                              "Try to avoid black roads. \n"
                                              "If your robot stamps on the black road, \n"
                                              "you lose!")
    explain_label.grid()
    calibrate_button= ttk.Button(main_frame, text= "calibrate")
    calibrate_button.grid(row=0, column=1)
    calibrate_button['command'] = lambda: calibrate_button_command(mqtt_client)
    start_button = ttk.Button(main_frame, text= "start!")
    start_button.grid(row=0, column=2)
    start_button['command']= lambda: start_button_command(mqtt_client)

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()
def quit_program(mqtt_client, should_shutdown_robot):
    if should_shutdown_robot:
        print("robot", "shutdown")
        mqtt_client.send_message("robot", "shutdown")
    exit()
def calibrate_button_command(mqtt_client):
    print("line_follower","search_black")
    mqtt_client.send_message("line_follower","search_black")
def start_button_command(mqtt_client):
    print("line_follower", "capture_black")
    mqtt_client.send_message("line_follower", "capture_black")
main()