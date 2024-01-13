"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Derek Whitley, their colleagues, and Martino Kim.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   Define a complete program that:
#     a.  Imports  rosegraphics
#     b.  Defines a   main   function that:
#          - Constructs a TurtleWindow.
#          - Calls the function that YOU define (see next bullet, below) TWICE
#              (with different arguments each time) to TEST your function.
#          - Asks the TurtleWindow to wait for a mouse click, then close.
#     c.  Defines another function that takes three parameters:
#             a SimpleTurtle, a string that represents a color,
#             and an integer for the distance to move (in pixels),
#         and causes the SimpleTurtle to:
#           - Move backward the given distance.
#           - Change its Pen's color to the given color.
#           - Turn left 90 degrees.
#           - Move forward twice the given distance.
#     d.  Calls main.
###############################################################################
import rosegraphics as rg

def main():
    drawing_speed = 1  # Bigger numbers mean faster drawing
    window = rg.TurtleWindow()
    window.tracer(drawing_speed)
    my_function("red",100)
    my_function("green",300)
    window.update()
    window.close_on_mouse_click()

def my_function(color, distance):
    turtle=rg.SimpleTurtle()
    turtle.pen=rg.Pen(color,10)
    turtle.speed=1
    turtle.left(90)
    turtle.forward(2*distance)

main()