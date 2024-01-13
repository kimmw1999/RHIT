"""
This project is the test of the final project

Author: Marco Saucedo
"""
import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

def main():
    gui_constructor()


def gui_constructor():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_mqtt_to_talk_to_robot()

    root = tkinter.Tk()
    root.title("Marco's Project")
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    # bull_checkbutton = ttk.Checkbutton(main_frame, text="Check me out!")
    # bull_checkbutton.grid(row=0, column=0, padx=20)
    # bull_checkbutton_observer = tkinter.StringVar()
    # bull_checkbutton['variable'] = bull_checkbutton_observer
    # bull_checkbutton['command'] = lambda: checkbutton_changed(bull_checkbutton_observer)
    #
    # dog_checkbutton = ttk.Checkbutton(main_frame, text="Check me out!")
    # dog_checkbutton.grid(row=0, column=1, padx=20)
    # dog_checkbutton_observer = tkinter.StringVar()
    # dog_checkbutton['variable'] = dog_checkbutton_observer
    # dog_checkbutton['command'] = lambda: checkbutton_changed(dog_checkbutton_observer)
    # Label
    label = ttk.Label(main_frame, text="Welcome! \n"
                                       "You have the option of picking a bull or a dog for today \n"
                                       "Bull: The bull will follow a red object \n"
                                       "Dog: The Dog will fetch a colored object \n"
                                       "Make a choice and PRESS START \n"
                                       "To Quit PRESS QUIT", relief='sunken')

    # Buttons
    start_button = ttk.Button(main_frame, text='Start!')
    quit_button = ttk.Button(main_frame, text='Stop!')

    # Radiobuttons
    radio_frame = ttk.Frame(main_frame, borderwidth=10, relief='groove')
    bull_radiobutton = ttk.Radiobutton(radio_frame, text='Bull Mode', value='bull')
    dog_radiobutton = ttk.Radiobutton(radio_frame, text='Dog Mode', value='dog')

    radio_observer = tkinter.StringVar()
    for radio in [bull_radiobutton, dog_radiobutton]:
        radio['variable'] = radio_observer

    for radio in [bull_radiobutton, dog_radiobutton]:
        radio['command'] = lambda: radiobutton_changed(mqtt_client, radio_observer)
        # radio['command'] = lambda: start_button_pressed(mqtt_client, radio_observer)

    start_button['command'] = lambda: start_button_pressed(mqtt_client, radio_observer)
    root.bind('<space>', lambda event: start_button_pressed(mqtt_client, radio_observer))
    quit_button['command'] = lambda: quit_button_pressed(mqtt_client, True)

    # Adding Widgets to grid
    label.grid(row=0, column=0, padx=20)
    radio_frame.grid(row=1, column=0, padx=20)
    start_button.grid(row=2, column=0, padx=30)
    quit_button.grid(row=3, column=0, padx=20)

    bull_radiobutton.grid(sticky='w')
    dog_radiobutton.grid(sticky='w')

    root.mainloop()

def radiobutton_changed(mqtt_client, radiobutton_observer):
    print('The radiobutton changed to', radiobutton_observer.get())
    print("robot is stopping")


def start_button_pressed(mqtt_client, radiobutton_observer):
    pet_type = radiobutton_observer.get()
    if pet_type == 'bull':
        print()
        print("you have chosen bull")
        print("Starting program!")
        mqtt_client.send_message("camera_tracker", "spin_to_track_color", [100, 20])
        mqtt_client.send_message("drive_system", "stop")
    if pet_type == 'dog':
        print()
        print("you have chosen dog")
        print("Starting program!")
        mqtt_client.send_message("camera_tracker", "fetch", [50])


def quit_button_pressed(mqtt_client, should_shutdown_robot):
    print("Quitting program!")
    if should_shutdown_robot:
        print("robot", "shutdown")
        mqtt_client.send_message("robot", "shutdown")
    exit()

main()