"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in PRINTING-TO-CONSOLE problems.  ***

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# DONE: 2.  [Note: same _TODO_ as its matching one in module m1.]
#  Students:
#  __
#  These problems have DIFFICULTY and TIME ratings:
#    DIFFICULTY rating:  1 to 10, where:
#       1 is very easy
#       3 is an "easy" Exam 3 question.
#       5 is a "typical" Exam 3 question.
#       7 is a "hard" Exam 3 question.
#      10 is an EXTREMELY hard problem (too hard for a Exam 3 question)
#  __
#    TIME ratings: A ROUGH estimate of the number of minutes that we
#       would expect a well-prepared student to take on the problem.
#  __
#    IMPORTANT: For ALL the problems in this module,
#      if you reach the time estimate and are NOT close to a solution,
#      STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP on it,
#      in class or via Piazza.
#  __
#  After you read (and understand) the above, change this _TODO_ to DONE.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: r=7')
    shape(7)

    print()
    print('Test 2 of shape: r=4')
    shape(4)

    print()
    print('Test 3 of shape: r=2')
    shape(2)


def shape(r):
    """
    Prints a shape with r rows that looks like this example where r=7:
    +++++++!7654321
     ++++++!654321-
      +++++!54321--
       ++++!4321---
        +++!321----
         ++!21-----
          +!1------

    Another example, where r=4:
    ++++!4321
     +++!321-
      ++!21--
       +!1---

    Preconditions:  r is a positive number.
    For purposes of "lining up", assume r is a single digit.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    ###########################################################################
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:  15 minutes.
    # -------------------------------------------------------------------------
    for k in range(r, 0, -1):
        for space in range(r-k):
            print(" ", end="")
        for count in range(k):
            print("+", end="")
        print("!", end="")
        for j in range(k, 0, -1):
            print(j, end="")
        print()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
