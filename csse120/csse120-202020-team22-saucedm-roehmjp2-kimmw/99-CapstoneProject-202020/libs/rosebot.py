"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the RoseBot class (the top-level class for a robot).

Authors:  Your professors (for the framework)
    and Marco Saucedo, Joshua Roehm, Martino Kimm.
Winter term, 2019-2020.
"""
# Done: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_drive_system

import rosebot_touch_sensor
import rosebot_arm_and_claw

import rosebot_leds
import rosebot_brick_buttons
import rosebot_remote_control

import rosebot_sound
import rosebot_infrared_proximity_sensor
import rosebot_beacon_sensor
import rosebot_beacon_seeker

import rosebot_color_sensor
import rosebot_line_follower

import rosebot_camera_sensor
import rosebot_camera_tracker
###############################################################################
#    RoseBot class.
#
# NOTE TO STUDENTS:
#   You should construct a  RoseBot  object for the Snatch3r robot.
#   Do ** NOT ** construct any instances of any other classes in this module,
#   since a RoseBot constructs instances of all the sub-systems that provide
#   ALL of the functionality available to a Snatch3r robot.
#
#   Use those sub-systems (and their instance variables)
#   to make the RoseBot (and its associated Snatch3r robot) do things.
###############################################################################
class RoseBot(object):
    def __init__(self):
        # Lab 1
        self.drive_system = rosebot_drive_system.DriveSystem("B","D")

        # Lab 2
        self.touch_sensor = rosebot_touch_sensor.TouchSensor(None)
        self.arm_and_claw = rosebot_arm_and_claw.ArmAndClaw("A", self.touch_sensor)

        # Lab 3
        self.leds = rosebot_leds.Leds()
        self.brick_buttons = rosebot_brick_buttons.BrickButtons()
        self.remote_control = rosebot_remote_control.RemoteControl()

        #  Lab 4
        self.sound = rosebot_sound.Sound()
        self.infrared_proximity_sensor = rosebot_infrared_proximity_sensor.InfraredProximitySensor(4)
        self.beacon_sensor = rosebot_beacon_sensor.BeaconSensor(4, 1)
        self.beacon_seeker = rosebot_beacon_seeker.BeaconSeeker(self.beacon_sensor, self.drive_system)

        # Lab 5
        self.color_sensor = rosebot_color_sensor.ColorSensor(3)
        self.line_follower = rosebot_line_follower.LineFollower(self.color_sensor, self.drive_system, self.remote_control)

        # Lab 6
        self.camera_sensor = rosebot_camera_sensor.CameraSensor(2)
        self.camera_tracker = rosebot_camera_tracker.CameraTracker(self.camera_sensor, self.drive_system, self.infrared_proximity_sensor, self.arm_and_claw)

        # Lab 7
        self.should_shutdown = False

    def shutdown(self):
        self.should_shutdown = True