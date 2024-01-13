"""
This module demonstrates the WAIT-FOR-EVENT pattern using
the WHILE TRUE pattern:

   while True:
       ...
       if <event has occurred>:
           break
       ...

See the module that is the COMPANION to this one for the same examples,
but using the ITCH pattern for WHILE loops.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# DONE: 2.  Read and run this program.  Then do the following problems,
#   putting your answers RIGHT HERE IN THIS DOCUMENT.
#  __
#   1. True or False?  Write your answer here: ___True____
#      In the approach demonstrated in this module, all the loops begin with:
#         while True:
#  __
#   2. What 5-letter word causes the program to break out of a loop
#      and continue execution below the loop?
#          Write your answer here: __count____
#  __
#   3. True or False?  Write your answer here: _Ture______
#      A  break  statement works in a  FOR   loop as well as in a  WHILE  loop.
#  __
#   4. Run and read the code below for:
#            demonstrate_wait_for_circle_to_reach_edge.
#      Where in the loop are the   IF and break   statements:
#      Choose your answer from:
#          -- At the beginning of the loop
#          -- In the middle of the loop
#          -- At the end of the loop
#  __
#   5. Is   demonstrate_wait_for_circle_to_reach_edge   100% clear to you?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#   6. Run and read the code below for:
#            demonstrate_wait_for_sentinel.
#      What number is used as the SENTINEL in that function? ________
#  __
#   7. Is the concept of a SENTINEL and the code for
#      demonstrate_wait_for_sentinel   100% clear to you?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#   8. Run and read the code below for:
#            wait_for_small_enough_number.
#      Where in the loop are the   IF and break   statements:
#      Choose your answer from:
#          -- At the beginning of the loop
#          -- In the middle of the loop----this one
#          -- At the end of the loop
#  __
#   9. Is   wait_for_small_enough_number   100% clear to you?
#        Yes or No?     [If No, ASK FOR HELP NOW!] yes
#  __
#  10. Read the comment about   random.seed(...)   that begins at about
#      line number 87 below.  Do you understand what  random.seed(...) does?
#        Yes or No?     [If No, ASK FOR HELP NOW!] yes
#  __
#   After you have PUT YOUR ANSWERS IN THIS COMMENT as described above,
#     a. Find someone who has had THEIR answer checked.
#     b. Ask THEM to check YOUR answers to the above.
#     c. Change the above _TODO_ to DONE.
#  __
#   As always, ask questions as needed!
###############################################################################

###############################################################################
# Students: Before you leave these examples,
#   *** MAKE SURE YOU UNDERSTAND THE   WAIT-FOR-EVENT   PATTERN,
#   *** with its use of   while True:   and   break.
###############################################################################

import math
import random
import time
import rosegraphics as rg

# -----------------------------------------------------------------------------
# There are two   random.seed(...)   statements below.
#   -- The first (commented out) initializes the pseudo-random number generator
#        to a fixed starting place.  Hence, the random numbers generated
#        will be the same in each run of the file, if that form were used.
#   -- The second form initializes the pseudo-random number generator
#        to a more-or-less random starting place, based on the time at which
#        this program runs.  Hence, the random numbers generated
#        will be different from one run of this program to another.
# -----------------------------------------------------------------------------
# random.seed(12)  # The number  12   was picked arbitrarily.
random.seed((time.time() * 100) % 1000)


def main():
    """ Demonstrates applications of the wait-for-event pattern. """
    demonstrate_wait_for_circle_to_reach_edge()
    demonstrate_wait_for_sentinel()
    demonstrate_wait_for_small_enough_number()

    # The rest of  main  is just for fun, for those interested:
    just_for_fun_long_waits()


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

    while True:
        # Construct and draw a purple circle.
        circle = rg.Circle(rg.Point(x, y), radius)
        circle.fill_color = 'purple'
        circle.attach_to(window)

        # If the circle has reached a right/bottom border of the window,
        # break out of the loop
        right_edge = x + radius
        bottom_edge = y + radius

        if right_edge >= window.width or bottom_edge >= window.height:
            break

        # Make the next circle be down, to the right, and bigger.
        k = k + 1
        x = x + 2
        y = y + 1
        radius = radius + (k / 100)

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
    while True:
        number = int(input('Enter a positive integer, or -1 to quit: '))
        if number == -1:
            break
        print('The square root of {} is about {:0.5f}.\n'.
              format(number, math.sqrt(number)))
        total = total + math.sqrt(number)

    print('The total of the square roots is', total)


# -----------------------------------------------------------------------------
# Demonstrates waiting for a "small enough" random number to be generated.
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

    print('I will now generate random integers')
    print('between 1 and 50, stopping when a generated')
    print('random integer is less than or equal to 10.')
    print()

    n = wait_for_small_enough_number(10, 50)

    print()
    print(n, 'random integers between 1 and 50 were generated')
    print('before one was less than or equal to 10.')


def wait_for_small_enough_number(small_number, max_number, print_it=True):
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
    count = 0
    while True:
        count = count + 1
        number = random.randrange(1, max_number + 1)
        if print_it:
            print("   Randomly generated number: {}".format(number))
        if number <= small_number:
            break

    return count


# -----------------------------------------------------------------------------
# Demonstrates more waiting for events, this time waiting
# for statistically unlikely events.
# -----------------------------------------------------------------------------
def just_for_fun_long_waits():
    """
    Demonstrates how long you have to wait for statistically unlikely events.
    """
    print('Modify the first few lines in just_for_fun_long_waits')
    print('if you want to play around with statistics.')
    iterations_asked_for = 60
    probability_required = 0.2
    max_number = 50
    count = waiting_again(round(max_number * probability_required),
                          max_number, iterations_asked_for)

    print('{} calls to  wait_for_small_enough_number'.format(count))
    print('   were required for  wait_for_small_enough_number  to do')
    print('{} iterations before the "waited for" event occurred,'.
          format(iterations_asked_for))
    print('   where the event occurs with probability')
    print('{:0.2f}'.format(probability_required))


def waiting_again(small_number, max_number, number_of_numbers):
    """
    What comes in:  Three non-negative integers.
    What goes out:
      Calls   wait_for_small_enough_number   repeatedly, using the first
      two arguments to this function as arguments in the call.
      Each call returns a number  N  that is the number of numbers generated
      randomly by the call.  This function waits until a call returns a value
      Returns the number of calls required to achieve that result.
    Side effects:
      -- Per wait_for_small_enough_number.
    """
    print()
    print('----------------------------------------------------------')
    print('Demonstrating WAIT FOR AN UNLIKELY EVENT, namely,')
    print('that it requires a lot of calls to')
    print('  wait_for_small_enough_number')
    print('for a call that took a lot of iterations before returning.')
    print('----------------------------------------------------------')
    count = 0
    while True:
        count = count + 1
        n = wait_for_small_enough_number(small_number, max_number,
                                         print_it=False)
        if n >= number_of_numbers:
            return count  # Note that RETURN can sometimes substitute for BREAK


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
