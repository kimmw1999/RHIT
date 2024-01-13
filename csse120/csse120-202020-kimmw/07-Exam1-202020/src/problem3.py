"""
Exam 1, problem 3.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math
import math

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  problem3  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # ONE test on ONE window.
    title = "Test 1 of Problem 3:"
    title += " circle, red vertical line 10 thick, big X."
    window = rg.RoseWindow(400, 250, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 150), 50)
    circle.outline_thickness = 10
    problem3(circle, 200, "red", window)
    window.close_on_mouse_click()

    # TWO MORE tests on ANOTHER window
    title = "Tests 2 & 3:"
    title += " grey circle, blue vertical line 20 thick,"
    title += " X 100 long;  green circle, thin black line, small X."
    window = rg.RoseWindow(700, 350, title)

    # Test 2:
    circle = rg.Circle(rg.Point(175, 50), 25)
    circle.fill_color = 'light gray'
    circle.outline_thickness = 20
    problem3(circle, 100, "blue", window)
    window.continue_on_mouse_click()

    # Test 3:
    circle = rg.Circle(rg.Point(400, 250), 100)
    circle.fill_color = "green"
    problem3(circle, 50, "black", window)
    window.close_on_mouse_click()

    # TWO MORE tests on ANOTHER window
    title = "Tests 4 & 5:"
    title += " black circle, 20 thick magenta line, teeny X;"
    title += "  circle, 5 thick light blue line, huge X."
    window = rg.RoseWindow(650, 200, title)

    # Test 4:
    circle = rg.Circle(rg.Point(200, 75), 50)
    circle.outline_thickness = 20
    circle.fill_color = "black"
    problem3(circle, 10, "magenta", window)
    window.continue_on_mouse_click()

    # Test 5:
    circle = rg.Circle(rg.Point(350, 100), 20)
    circle.outline_thickness = 5
    problem3(circle, 250, "light blue", window)
    window.close_on_mouse_click()


def problem3(circle, length, line_color, window):
    """
    See   problem3_pictures.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Circle
      -- A positive integer
      -- A string that represents a color in RoseGraphics
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given rg.RoseWindow:
      a. The given rg.Circle,
           but with 5 as its outline thickness.
         [ATTACH this rg.Circle BEFORE attaching the following rg.Line
          objects, so that the lines are "on top" of the rg.Circle.]
      b. An rg.Line object that (see the pictures!):
           -- is vertical,
           -- has endpoints that are the topmost and bottommost points
                of the given rg.Circle,
           -- has as its color the given color, and
           -- has as its thickness the outline thickness
                of the given rg.Circle BEFORE it was changed to 5.
      c. Two more rg.Line objects that form an X such that (see the pictures!):
           -- The X is centered on the given rg.Circle, rotated 45 degrees
                from the horizontal/vertical axes,
           -- Each line has the given length.
      Must render but   ** NOT close **   the window.

    ** Ask for help if, AFTER you have looked at the file in this project:
    **     problem3_pictures.pdf
    ** you do not understand what this problem asks you to do.

    Type hints:
      :type circle:      rg.Circle
      :type length:      int
      :type line_color:  str
      :type window:      rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    #   ___
    #   HINT: Recall the Pythagorean theorem, namely:
    #         For a right triangle, the sum of the squares of the lengths
    #         of the sides equals the square of the length of the hypotenuse.
    # -------------------------------------------------------------------------
    circle.attach_to(window)

    orig_thick=circle.outline_thickness
    circle.outline_thickness=5
    cent_x = circle.get_bounding_box().get_center().x
    cent_y = circle.get_bounding_box().get_center().y
    top_p = rg.Point(cent_x, cent_y - circle.radius)
    bot_p = rg.Point(cent_x, cent_y + circle.radius)
    line = rg.Line(top_p, bot_p)
    line.thickness=orig_thick
    line.color=line_color
    line.attach_to(window)

    x_diff=(length//2)//(math.sqrt(2))
    y_diff=x_diff
    line1_p1=rg.Point(cent_x-x_diff,cent_y-y_diff)
    line1_p2=rg.Point(cent_x+x_diff,cent_y+y_diff)
    line2_p1=rg.Point(cent_x+x_diff,cent_y-y_diff)
    line2_p2=rg.Point(cent_x-x_diff,cent_y+y_diff)
    line1=rg.Line(line1_p1, line1_p2)
    line2=rg.Line(line2_p1, line2_p2)
    line1.attach_to(window)
    line2.attach_to(window)


    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
