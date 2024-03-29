"""
This module demonstrates the WAIT-FOR-EVENT pattern using
the ITCH pattern:

   Initialize as needed so that the CONDITION can be TESTED.
   while <some CONDITION>: # Test the CONDITION, continue WHILE it is true.
       ...
       ...
       CHange something that (eventually) affects the CONDITION.
         (else otherwise you will be in an infinite loop)

See the module that is the COMPANION to this one for the same examples,
but using the WHILE TRUE pattern for WHILE loops.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# DONE: 2.  Read and run this program.  Then do the following problems,
#   putting your answers RIGHT HERE IN THIS DOCUMENT.
#  __
#   1. Which version of   demonstrate_wait_for_sentinel  feels clearer to you? Version in this module
#        -- The version in this module, or
#        -- The version in the previous module
#   Note: reasonable people could disagree on the answer to this question.
#  __
#   2. Can you READ and TRACE-BY-HAND   while CONDITION:   loops,
#        as exemplified in this module?             yes
#        Yes or No?     [If No, ASK FOR HELP NOW!]
###############################################################################

###############################################################################
# Students: Before you leave these examples,
#   *** MAKE SURE YOU UNDERSTAND THE   WAIT-FOR-EVENT   PATTERN,
#   *** with its use of a    WHILE <condition>:   statement.
###############################################################################

import math
import random
import rosegraphics as rg


def main():
    """ Demonstrates applications of the wait-for-event pattern. """
    demonstrate_wait_for_circle_to_reach_edge()
    demonstrate_wait_for_sentinel()
    demonstrate_wait_for_small_enough_number()


# -----------------------------------------------------------------------------
# Demonstrates waiting for a sequence of "growing" circles
# to reach the edge of the window in which they are drawn.
# -----------------------------------------------------------------------------
def demonstrate_wait_for_circle_to_reach_edge():
    """
    Demonstrates the   wait_for_event   pattern, where the event
    is that a growing graphical object has grown beyond the window size.

    This particular example draws, moves and grows purple circles
    until a circle extends beyond the border of the window.
    """
    print()
    print('---------------------------------------------------------')
    print('Demonstrating the WAIT FOR EVENT pattern in graphics:')
    print('See the graphics window that pops up.')
    print('---------------------------------------------------------')

    window = rg.RoseWindow(700, 450, 'Animation until a TOO-BIG circle')

    x = 20
    y = 50
    radius = 5
    k = 0
    window.continue_on_mouse_click()

    # If the circle has reached a right/bottom border of the window,
    # exit the loop
    right_edge = x + radius
    bottom_edge = y + radius

    while right_edge < window.width and bottom_edge < window.height:
        # Construct and draw a purple circle.
        circle = rg.Circle(rg.Point(x, y), radius)
        circle.fill_color = 'purple'
        circle.attach_to(window)

        # Make the next circle be down, to the right, and bigger.
        k = k + 1
        x = x + 2
        y = y + 1
        radius = radius + (k / 100)

        right_edge = x + radius
        bottom_edge = y + radius

        # Render.  Allow a little time to elapse,
        #          else the animation flashes by.
        window.render(0.01)

    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Demonstrates waiting for a "sentinel" value to be input.
# -----------------------------------------------------------------------------
def demonstrate_wait_for_sentinel():
    """
    Demonstrates the   wait_for_event   pattern, where the event
    is inputting a SENTINEL value to signal the end of user input.

    This particular example inputs positive integers and processes them
    by printing their square roots, and when input is finished,
    printing the sum of those square roots.  User input stops when
    the user inputs the agreed-upon SENTINEL value of -1.
    """
    print()
    print('----------------------------------------------')
    print('Demonstrating the WAIT FOR SENTINEL pattern:')
    print('----------------------------------------------')

    total = 0
    number = int(input('Enter a positive integer, or -1 to quit: '))
    while number != -1:
        print('The square root of {} is about {:0.5f}.\n'.
              format(number, math.sqrt(number)))
        total = total + math.sqrt(number)
        number = int(input('Enter a positive integer, or -1 to quit: '))

    print('The total of the square roots is', total)


# -----------------------------------------------------------------------------
# Demonstrates waiting for a "small enough" random number
# to be generated.
# -----------------------------------------------------------------------------
def demonstrate_wait_for_small_enough_number():
    """
    Demonstrates the   wait_for_event   pattern, by generating
    random numbers between 1 and 50, inclusive,
    and stopping when the following event occurs:
      a number less than or equal to 10 is generated.
    """
    print()
    print('----------------------------------------------------------')
    print('Demonstrating WAIT FOR A SMALL ENOUGH')
    print('  randomly generated number')
    print('----------------------------------------------------------')

    print('I will now genenerate random integers')
    print('between 1 and 50, stopping when a generated')
    print('random integer is less than or equal to 10.')
    print()

    n = wait_for_small_enough_number(10, 50)

    print()
    print(n, 'random integers between 1 and 50 were generated')
    print('before one was less than or equal to 10.')


def wait_for_small_enough_number(small_number, max_number):
    """
    What comes in:  Two non-negative integers.
    What goes out:
      Returns the number of random integers that are generated,
      as described below.
    Side effects:
      -- Repeatedly generates random integers between 1 and max_number,
           inclusive, where max_number is the second given integer.
      -- Stops when the random integer is less than or equal to
           small_number, where small_number is the first given integer.
      -- Prints the random numbers as they are generated.
    """
    number = random.randrange(1, max_number + 1)
    print(number)
    count = 1
    while number > small_number:
        number = random.randrange(1, max_number + 1)
        print(number)
        count = count + 1

    return count


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
