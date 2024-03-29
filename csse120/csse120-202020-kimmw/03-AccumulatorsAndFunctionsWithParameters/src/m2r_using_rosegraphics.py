"""
This module uses ROSEGRAPHICS to demonstrate:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Derek Whitley, their colleagues, and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# DONE: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#  _
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
###############################################################################

###############################################################################
# DONE: 3.
#   RUN this program.  Then answer the following, FOLLOWING YOUR INSTRUCTOR
#     and GETTING HELP AS NEED! (Ask questions!!!)
#  _
#     a. For the RoseGraphics coordinate system:
#  _
#        -- Where is the (0, 0) point on the screen?
#              top left
#  _
#        -- In what direction on the screen does the positive X-axis point?
#              right
#  _
#        -- In what direction on the screen does the positive Y-axis point?
#              down
#  _
#     b. Write a line of code that constructs a RoseWindow object:
#            window=rg.RoseWindow()
#  +
#     c. What is the default height of a RoseWindow?
#        (Select RoseWindow in the code below, then  View ~ Quick Documentation
#         to determine the answer to this question.)
#            300
#  +
#     d. Write a line of code that construct a RoseWindow object
#        whose height is 100:
#        (Use the   View ~ Quick Documentation   trick to figure it out)
#            window=rg.RoseWindow(400,100)
#  +
#     e. Use the DOT trick to answer the following:
#  +
#          -- Write the names of two types of graphics objects that
#             you can construct OTHER than Circle and Point:
#                rg.Square(), rg.Rectangle()
#  +
#          -- Write the names of three METHODs that Circle objects have:
#                circle.move_by()
#                circle.clone()
#                circle.attach_to()
#  +
#          -- Write the names of three INSTANCE VARIABLEs that Circle
#             objects have:
#                Center, radius, fill_color
#  _
#     f. What does a RoseWindow RENDER method do?
#            draw all the objects attached to the window
#  _
#     g. When is a RoseWindow close_on_mouse_click method call
#        necessary?  Why?
#            At the end of the function. Needs a way to exit the code.
#  _
#   ASK QUESTIONS ** NOW ** if you do not understand how the
#     RoseGraphics graphics system works.
#  _
#   When you are confident that you have written correct answers
#   to the above questions (ASK QUESTIONS AS NEEDED!),
#   change the above _TODO_ to DONE.
###############################################################################

import rosegraphics as rg


def main():
    """
    Uses ROSEGRAPHICS to demonstrate:
      -- CONSTRUCTING objects,
      -- applying METHODS to them, and
      -- accessing their DATA via INSTANCE VARIABLES
    """
    example1()
    example2()
    example3()


def example1():
    """ Displays an empty window. """
    window = rg.RoseWindow(500, 300, "Example 1: An empty window")
    window.close_on_mouse_click()


def example2():
    """ Displays two Point objects. """
    # -------------------------------------------------------------------------
    # Construct the window in which objects will be drawn.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    # -------------------------------------------------------------------------
    # Construct some rg.Point objects.
    # Note: the y-axis goes DOWN from the TOP.
    # -------------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    # -------------------------------------------------------------------------
    # A RoseGraphics object is not associated with a window,
    # and hence are not drawn, until you ATTACH it to a window.
    # -------------------------------------------------------------------------
    point1.attach_to(window)
    point2.attach_to(window)

    # -------------------------------------------------------------------------
    # And they still are not DRAWN until you RENDER the window.
    # That will draw ALL the objects on the window.
    # This two-step approach is important for animation.
    # -------------------------------------------------------------------------
    window.render()

    window.close_on_mouse_click()


def example3():
    """ Displays a Circle and a Rectangle. """
    # -------------------------------------------------------------------------
    # RoseWindow: optionally takes its width and height.
    # -------------------------------------------------------------------------
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)

    # -------------------------------------------------------------------------
    # Circle: needs its center and radius.
    # Has  fill_color  instance variable.
    # -------------------------------------------------------------------------
    center_point = rg.Point(300, 100)
    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.fill_color = "green"
    circle.attach_to(window)
    # -------------------------------------------------------------------------
    # Rectangle: needs two opposite corners.
    # -------------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)

    # -------------------------------------------------------------------------
    # render: Draw ALL the objects attached to this window.
    # -------------------------------------------------------------------------
    window.render()

    # -------------------------------------------------------------------------
    # A Rectangle has instance variables  corner_1  and  corner_2.
    # -------------------------------------------------------------------------
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    print(corner1, corner2)  # You can also PRINT RoseGraphics objects.
    print(rectangle)  # See the Console for the output.

    # -------------------------------------------------------------------------
    # close_on_mouse_click: Keeps the window open until user clicks.
    # -------------------------------------------------------------------------
    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
