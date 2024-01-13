


import rosebot
import mqtt_remote_method_calls as com
import time

def main():
    """ Test a robot's using MQTT. """
    print()
    print('--------------------------------------------------')
    print(' Listening for MQTT messages from the PC')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # DONE: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------
    robot= rosebot.RoseBot()
    # -------------------------------------------------------------------------
    # DONE: 3. Construct an MQTT client passing in the robot as the argument.
    # -------------------------------------------------------------------------
    mqtt_client= com.MqttClient(robot)
    # -------------------------------------------------------------------------
    # DONE: 4. Connect to talk to the laptop
    # -------------------------------------------------------------------------
    mqtt_client.connect_to_mqtt_to_talk_to_laptop()
    # -------------------------------------------------------------------------
    # TODO: 5. Create a loop which can be shutdown
    #          Add a field on the robot called should_shutdown
    #          That is set to False
    #          And add a method that can modify that field called shutdown
    # -------------------------------------------------------------------------
    while True:
        time.sleep(0.05)
        if robot.should_shutdown:
            break

main()
