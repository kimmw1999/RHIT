"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Derek Whitley, their colleagues, and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# DONE: 2
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#  _
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
###############################################################################

import rosegraphics as rg
import math

def main():
    """
    TESTS the functions that you will write below.
    You write the tests per the _TODO_s below.
    """
    hyp(3, 4)
    hyp(5, 12)
    window = rg.TurtleWindow()
    # Put your TESTS immediately below this line, as directed by _TODO_s below.
    turtle("red", 15)
    turtle("orange", 50)

    window.close_on_mouse_click()


###############################################################################
# DONE: 3a.  Define a function immediately below this _TODO_.
#   It takes two arguments that denote, for a right triangle,
#   the lengths of the two sides adjacent to its right angle,
#   and it returns the length of the hypotenuse of that triangle.
#     HINT: Apply the Pythagorean theorem.
#  _
#   You may name the function and its parameters whatever you wish,
#   but choose DESCRIPTIVE (self-documenting) names.
#
# DONE: 3b.  In main, CALL your function TWICE (with different values
#   for the arguments) and print the returned values,
#   to test whether you defined the function correctly.
###############################################################################
def hyp(a, b):
    c=math.sqrt(a**2+b**2)
    print(c)
    return c

###############################################################################
# DONE: 4a.  Define a function immediately below this _TODO_.
#   It takes two arguments:
#     -- a string that represents a color (e.g. "red")
#     -- a positive integer that represents the thickness of a Pen.
#  _
#   The function should do the following (in the order listed):
#     a. Constructs two SimpleTurtle objects, where:
#          - one has a Pen whose color is "green" and has the GIVEN thickness
#        - - the other has a Pen whose color is the GIVEN color
#              and whose thickness is 5
#  _
#        Note: the "GIVEN" color means the PARAMETER that represents a color.
#        Likewise, the "GIVEN" thickness means the PARAMETER for thickness.
#  _
#     b. Makes the first (green) SimpleTurtle move FORWARD 100 pixels.
#  _
#     c. Makes the other (thickness 5) SimpleTurtle move BACKWARD 100 pixels.
#  _
#   You may name the function and its parameters whatever you wish,
#   but choose DESCRIPTIVE (self-documenting) names.
#
# TODO: 4b.  In main, CALL your function at least TWICE (with different values
#   for the arguments) to test whether you defined the function correctly.
###############################################################################
def turtle( color, thick):
    turtle_1= rg.SimpleTurtle("turtle")
    turtle_1.pen=rg.Pen("green",thick)
    turtle_2= rg.SimpleTurtle("turtle")
    turtle_2.pen=rg.Pen(color, 5)
    turtle_1.forward(100)
    turtle_2.backward(100)
###############################################################################
# DONE: 5.
#   COMMIT-and-PUSH your work (after changing this _TODO_ to DONE).
#  _
#   As a reminder, here is how you should do so:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up,
#        press the   Commit and Push   button.
#           Note: If you see only a Commit button:
#              - HOVER over the  Commit  button
#                  (in the lower-right corner of the window)
#              - CLICK on  Commit and Push.
#  _
#   COMMIT adds the changed work to the version control on your computer.
#   PUSH adds the changed work into your Github repository in the "cloud".
#  _
#   COMMIT-and-PUSH your work as often as you want, but at the least, commit
#   and push after you have tested a module and believe that it is correct.
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
