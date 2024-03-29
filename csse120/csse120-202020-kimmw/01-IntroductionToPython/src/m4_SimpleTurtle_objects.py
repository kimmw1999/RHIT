"""
Demonstrates using OBJECTS via Turtle Graphics.

Concepts include:
  -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
  -- Make an object   ** DO **   something by using a METHOD.
  -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.

Also:
  -- ASSIGNING a VALUE to a NAME (VARIABLE).

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Derek Whitley, their colleagues, and Martino Kim.
"""
###############################################################################
# DONE: 1.
#   Yes, that means for YOU to DO things per the following instructions:
#  _
#   On Line 13 above, replace  PUT_YOUR_NAME_HERE  with your OWN name.
#  _
#   BTW, the top block of text above forms what is called a DOC-STRING.
#   It documents what this module does, in a way that exterior programs
#   can make sense of.  It has no other effect on this program.
###############################################################################

import rosegraphics as rg

###############################################################################
# DONE: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#  _
#     In the Project window (to the left), right click on the src  folder,
#     then select   Mark Directory As ~ Sources Root.
#  _
#   You will see that  rosegraphics  in the  import  statement above (line 26)
#   is no longer marked as an error.  You will do this in all projects
#   that use rosegraphics, so get used to it. :)
#  _
#   Once  rosegraphics  in the  import  statement is no longer marked as error,
#   change this _TODO_ to DONE and  ** continue to the next _TODO_ (below). **
###############################################################################

###############################################################################
# DONE: 3.
#   Run this module.  A window will pop up and Turtles will move around.
#   After the Turtles stop moving,
#      ** click anywhere in the window to close the window **.
#  _
#   Then look at the code below.  Raise your hand when you have questions about
#   what the code is doing.  Be sure that you understand the notations for:
#  _
#     -- CONSTRUCTING an instance of a CLASS, e.g.
#           rg.SimpleTurtle()
#  _
#     -- ASSIGNING the resulting OBJECT (instance of a class) a NAME, e.g.
#           natasha = rg.SimpleTurtle()
#  _
#     -- Applying a METHOD to an object to make the object DO something, e.g.
#           natasha.forward(100)
#  _
#     -- Accessing an INSTANCE VARIABLE of an object, e.g.
#           natasha.speed = 10
#           boris.speed = natasha.speed
#  _
#   After you are confident that you understand all the code below,
#   change this _TODO_ to DONE and  ** continue to the next _TODO_ (below). **
###############################################################################

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - CONSTRUCT (make and initialize) a   TurtleWindow   object for animation.
# The definition of a  TurtleWindow  is in the   rg
# (shorthand for rosegraphics) module.
# -----------------------------------------------------------------------------
window = rg.TurtleWindow()
window.delay(20)  # Bigger numbers mean slower animation.

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - CONSTRUCT (make) a  SimpleTurtle  object and ASSIGN a NAME to the object.
# -----------------------------------------------------------------------------
boris = rg.SimpleTurtle()

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - Ask the SimpleTurtle object to do things by applying METHODs to it.
# The numbers in the parentheses are called ARGUMENTS.
# -----------------------------------------------------------------------------
boris.forward(100)
boris.left(90)
boris.forward(200)

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - Construct a second SimpleTurtle
#       (using an optional argument that sets the shape displayed - try it!),
#     set its  pen  and  speed  INSTANCE VARIABLES, and ask it to do things.
# -----------------------------------------------------------------------------
natasha = rg.SimpleTurtle("turtle")
natasha.pen = rg.Pen("red", 30)  # Second argument is the Pen's thickness
natasha.speed = 5  # Bigger means faster, max is usually about 10

natasha.backward(50)
natasha.right(90)
natasha.forward(125)

natasha.speed = 1  # Now slower
natasha.go_to(rg.Point(-100, 200))

###############################################################################
# DONE: 4.
#   Add a few more lines of your own code to make one of the existing
#   SimpleTurtles move some more and/or have different characteristics.
#  _
#      ** Nothing fancy is required. **
#      ** A SUBSEQUENT exercise will let you show your creativity. **
#  _
#   As always, test by running the module.
###############################################################################
natasha.go_to(rg.Point(100,200))
boris.forward(200)
###############################################################################
# DONE: 5.
#   The above code  CONSTRUCTS  two SimpleTurtle objects
#   and gives those objects NAMES:
#       boris    natasha
#  _
#   Add code of your own that constructs another SimpleTurtle object,
#   naming it whatever you want.  Names cannot have spaces or special
#   characters, but they can have digits and underscores, e.g.
#      this_1_has
#  _
#   STYLE RULE: Your names should always begin with a LOWER_CASE letter.
#   So   mary   is OK   but   Mary   is NOT OK.
#  _
#   Then add more code that:
#     -- Constructs a Pen object,
#     -- Assigns your SimpleTurtle's  pen  to the constructed Pen object, and
#     -- Makes your SimpleTurtle move around a bit.
#  _
#      ** Nothing fancy is required. **
#      ** A SUBSEQUENT exercise will let you show your creativity. **
#  _
#   As always, test by running the module.
###############################################################################
kim = rg.SimpleTurtle()
kim.forward(100)
###############################################################################
# DONE: 6.
#   Ensure that no blue bars on the scrollbar-thing to the right remain.
#   Run one more time to be sure that all is still OK.
#  _
#   Then COMMIT-and-PUSH your work as before:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up,
#        press the   Commit and Push   button.
#           (Note: If you see only a Commit button:
#              - HOVER over the  Commit  button
#                (in the lower-right corner of the window)
#              - CLICK on  Commit and Push.)
#  _
#   You can COMMIT-and-PUSH as often as you like.
#   DO IT FREQUENTLY; AT LEAST once per module.
###############################################################################

# -----------------------------------------------------------------------------
# The next line keeps the window open until the user clicks in the window.
# Throughout this exercise, this  close_on_mouse_click   line
# should be the LAST line in the file.  DO NOT ADD CODE BELOW THIS LINE!
# -----------------------------------------------------------------------------
window.close_on_mouse_click()
