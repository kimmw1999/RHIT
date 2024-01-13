"""
Exam 1, problem 4.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


def run_test_problem4():
    """ Tests the   problem4  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  problem4  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # ONE test on this window:
    title = "Test 1 of problem4: 5 new PLUS signs, wider than tall,"
    title += " magenta and blue."
    window = rg.RoseWindow(600, 150, title)

    center = rg.Point(50, 25)
    line1 = rg.Line(rg.Point(center.x, center.y - 15),
                    rg.Point(center.x, center.y + 15))
    line1.thickness = 3
    line2 = rg.Line(rg.Point(center.x - 45, center.y),
                    rg.Point(center.x + 45, center.y))
    line2.thickness = 8
    problem4(line1, line2, 5, "magenta", "blue", 3, window)
    window.close_on_mouse_click()

    # THREE tests on ANOTHER window.
    title = "Tests 2, 3 and 4: 3 new tall at bottom;"
    title += " 4 new wide at top; 26 new small in middle."
    window = rg.RoseWindow(600, 300, title)

    center = rg.Point(400, 230)
    line1 = rg.Line(rg.Point(center.x, center.y - 50),
                    rg.Point(center.x, center.y + 50))
    line1.thickness = 8
    line2 = rg.Line(rg.Point(center.x - 10, center.y),
                    rg.Point(center.x + 10, center.y))
    line2.thickness = 3
    problem4(line1, line2, 3, "cyan", "brown", 30, window)
    window.continue_on_mouse_click()

    center = rg.Point(100, 50)
    line1 = rg.Line(rg.Point(center.x, center.y - 20),
                    rg.Point(center.x, center.y + 20))
    line1.thickness = 10
    line2 = rg.Line(rg.Point(center.x - 50, center.y),
                    rg.Point(center.x + 50, center.y))
    line2.thickness = 20
    problem4(line1, line2, 4, "red", "blue", 5, window)
    window.continue_on_mouse_click()

    center = rg.Point(25, 150)
    line1 = rg.Line(rg.Point(center.x, center.y - 10),
                    rg.Point(center.x, center.y + 10))
    line1.thickness = 3
    line2 = rg.Line(rg.Point(center.x - 10, center.y),
                    rg.Point(center.x + 10, center.y))
    line2.thickness = 3
    problem4(line1, line2, 26, "magenta", "chartreuse", 1, window)
    window.close_on_mouse_click()


def problem4(vertical_line, horizontal_line, number, color1, color2, gap,
             window):
    """
    See   problem4_pictures.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- Two rg.Line objects,
           The first is vertical (start is at the top, end at the bottom).
           The second is horizontal (start is at the left, end is at the right).
           The lines intersect at their centers, thus forming a "PLUS" sign.
           See the pictures!
      -- A positive integer for the number of NEW "plus" signs to draw.
      -- Two strings that represent colors in RoseGraphics.
      -- A positive integer "gap".
      -- A rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      [Throughout, attach each vertical line AFTER its corresponding
       horizontal line, so that vertical lines are "on top"]
      -- Draws, on the given RoseWindow, the two given lines
            (that form a "PLUS" sign").  See the pictures!.
      -- Draws, on the given RoseWindow, copies of the given PLUS, as follows:
         See the pictures!
           -- HOW MANY?  There are the given  number  of copies.
           -- WHAT SIZE?
              -- Each vertical line has the same length
                   as the given vertical line.
              -- Each horizontal line has the same length
                   as the given horizontal line.
           -- SHIFTED RIGHT: Each PLUS sign is shifted to the right from
                the previous PLUS sign by the length of the given horizontal
                line plus the given gap.  See the pictures!
           -- THICKNESS:
              -- Each vertical line has the same thickness as the given one.
              -- Each horizontal line has the same thickness as the given one.
           -- COLORS: The new lines alternate colors, as follows:
                -- New vertical lines use:
                     color1, then color2, then color1, then color2, etc.
                -- New horizontal lines use:
                     color2, then color1, then color2, then color1, etc.
      Must render but   ** NOT close **   the window.

    ** Ask for help if, AFTER you have looked at the file in this project:
    **     problem4_pictures.pdf
    ** you do not understand what this problem asks you to do.

    Type hints:
      :type vertical_line:    rg.Line
      :type horizontal_line:  rg.Line
      :type number:           int
      :type color1:           str
      :type color2:           str
      :type gap:              int
      :type window:           rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    horizontal_line.attach_to(window)
    vertical_line.attach_to(window)
    cent_x=horizontal_line.get_midpoint().x
    cent_y=horizontal_line.get_midpoint().y
    center=horizontal_line.get_midpoint()
    hori_len=2*(cent_x-horizontal_line.start.x)
    distance1=hori_len+gap


    for k in range(1,number+1):

        hori_p1x=horizontal_line.start.x+distance1*k
        hori_p2x=horizontal_line.end.x+distance1*k
        hori_p1y=horizontal_line.start.y
        hori_p2y=hori_p1y
        line=rg.Line(rg.Point(hori_p1x,hori_p1y),rg.Point(hori_p2x,hori_p2y))
        line.thickness=horizontal_line.thickness
        if(k%2==1):
            line.color=color1
        else:
            line.color=color2
        line.attach_to(window)

        vert_p1x=vertical_line.start.x+distance1*k
        vert_p2x=vert_p1x
        vert_p1y=vertical_line.start.y
        vert_p2y=vertical_line.end.y
        line2=rg.Line(rg.Point(vert_p1x,vert_p1y),rg.Point(vert_p2x, vert_p2y))
        line2.thickness=vertical_line.thickness
        if(k%2==1):
            line2.color=color2
        else:
            line2.color=color1
        line2.attach_to(window)


    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
