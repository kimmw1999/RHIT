"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the LineFollower class.  The LineFollower uses the
reflected light intensity to drive the robot.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import time
import rosebot_ev3dev_api as rose_ev3
import rosebot_color_sensor
import rosebot_drive_system
import rosebot_remote_control

###############################################################################
#    LineFollower
###############################################################################
class LineFollower(object):
    """
    Methods using the reflected light intensity to drive the robot.
    """

    def __init__(self, color_sensor, drive_system, remote_control):
        """
        Constructs LineFollower to track black lines.
          :type color_sensor: rosebot_color_sensor.ColorSensor
          :type drive_system: rosebot_drive_system.DriveSystem
          :type remote_control: rosebot_remote_control.RemoteControl
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement (uncomment)  this method.
        # ---------------------------------------------------------------------
        self.color_sensor = color_sensor
        self.drive_system = drive_system
        self.white_reading = 95  # Approximation until a calibration is done.
        self.black_reading = 5  # Approximation until a calibration is done.
        self.left_turn= False
        self.right_turn= False
        self.stop=False
        self.remote= remote_control

    def calibrate(self):
        """
        Calibrates the white and black values for the given room conditions.
        Asks the user to place the robot on white first, then hit enter to
        take the reading.  Prints (and stores) the white_reading.  Then this
        method asks the user to place the robot on black, then hit enter to
        take the black reading.  Prints (and stores) the black_reading.
        """
        print("Place the robot on a white surface.")
        input("Press the ENTER key when you are ready to take the white_reading.")
        # ---------------------------------------------------------------------
        # TODO: Implement the rest of method.
        # ---------------------------------------------------------------------
        self.white_reading = self.color_sensor.get_reflected_light_intensity()
        print(self.white_reading)
        print("Place the robot on a black surface.")
        input("Press the ENTER key whey you are ready to take the black_reading.")
        self.black_reading = self.color_sensor.get_reflected_light_intensity()
        print(self.black_reading)

    def search_black(self):
        print("Place the robot on an object.")
        input("Press the ENTER key whey you are ready to take the object.")
        self.black_reading = self.color_sensor.get_reflected_light_intensity()
        print(self.black_reading)
        time.sleep(1)
        print("Place the robot on a floor.")
        input("Press the ENTER key whey you are ready to take the floor.")
        self.white_reading = self.color_sensor.get_reflected_light_intensity()
        print(self.white_reading)

    def capture_black(self):
        print("game start")
        while True:
            if self.white_reading < self.black_reading:
                if self.color_sensor.get_reflected_light_intensity() > self.black_reading-3:
                    self.drive_system.twist_around_3sec(100)
                    self.drive_system.stop()
                    print("object captured. you lose!")
                    break
                elif self.remote.is_pressed(1, "blue_down")==True:
                    self.drive_system.stop()
                    break
                else:
                    if self.remote.is_pressed(1, "red_up")== True:
                        self.drive_system.go(25, 100)
                    elif self.remote.is_pressed(1, "red_down")== True:
                        self.drive_system.go(100, 25)
                    else:
                        self.drive_system.go(100, 100)
            else:
                if self.color_sensor.get_reflected_light_intensity() <= self.black_reading+3:
                    self.drive_system.twist_around_3sec(50)
                    self.drive_system.stop()
                    print("object captured. you lose!")
                    break
                elif self.remote.is_pressed(1, "blue_down") == True:
                    self.drive_system.stop()
                    break
                else:
                    if self.remote.is_pressed(1, "red_up") == True:
                        self.drive_system.go(25, 100)
                    elif self.remote.is_pressed(1, "red_down") == True:
                        self.drive_system.go(100, 25)
                    else:
                        self.drive_system.go(100, 100)

    def follow_line_inside_ccw(self, max_speed, duration_s):
        """
        Makes the robot follow a line around in a circle.  In this version of
        line following the robot goes straight on white and does an arc left
        turn when on black.
         - White is might be 90+ values of the reflected light intensity
         - Black is might be as low as 5 on the reflected light intensity
        but here white is anything above light_threshold, otherwise black.
        This method should make the robot follow the inside of a line in a
        counter-clockwise direction at the given speed.
        After duration_s seconds have passed this method will stop both motors.
        :param max_speed: 1 to 100 value for the max wheel motor speed
        :type max_speed: int
        :param duration_s: How long to continue this action (in seconds)
        :type duration_s: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        light_threshold = (self.white_reading + self.black_reading)/2
        time_init= time.time()
        while True:
            if self.color_sensor.get_reflected_light_intensity()> light_threshold:
                self.drive_system.go(max_speed, max_speed)
            else:
                self.drive_system.go(max_speed/5, max_speed)
            if time.time()>time_init+ duration_s:
                break


    def stay_on_line(self, max_speed, duration_s):
        """
        Makes the robot follow a arbitrary line that turns left and right.
        When the robot is on black it continues straight, but when the robot
        is on white it stops and looks (arcs left for a while, arcs right for
        while) to try to find the line.  Once the line is found again it
        continues moving forward.
        After duration_s seconds have passed this method will stop both motors.
        :param max_speed: 1 to 100 value for the max wheel motor speed
        :type max_speed: int
        :param duration_s: How long to continue this action (in seconds)
        :type duration_s: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # Hint towards implementing the duration_s requirement...
        # start_time_s = time.time()
        # while True:
        #     time.sleep(0.05)
        #     if time.time() > start_time_s + duration_s:
        #         break
        # ---------------------------------------------------------------------
