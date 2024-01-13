"""
Exam 3, problem 4.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


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
    print('Test 1 of shape: r=5')
    shape(5)

    print()
    print('Test 2 of shape: r=3')
    shape(3)

    print()
    print('Test 3 of shape: r=1')
    shape(1)

    print()
    print('Test 4 of shape: r=8')
    shape(8)


def shape(r):
    """
    Prints a shape with r rows that looks like this example where r=5:
    12345--54321@13579
    2345---54321@1357
    345----54321@135
    45-----54321@13
    5------54321@1
    5------54321@1
    45-----54321@13
    345----54321@135
    2345---54321@1357
    12345--54321@13579

    Another example, where r=3:
    123--321@135
    23---321@13
    3----321@1
    3----321@1
    23---321@13
    123--321@135

    Another example, where r=1:
    1--1@1
    1--1@1

    One more example, where r=8:
    12345678--87654321@13579111315   (the tail end here is 11, then 13, then 15)
    2345678---87654321@135791113      (the tail end here is 11, then 13)
    345678----87654321@1357911         (the tail end here is 11)
    45678-----87654321@13579
    5678------87654321@1357
    678-------87654321@135
    78--------87654321@13
    8---------87654321@1
    8---------87654321@1
    78--------87654321@13
    678-------87654321@135
    5678------87654321@1357
    45678-----87654321@13579
    345678----87654321@1357911         (the tail end here is 11)
    2345678---87654321@135791113      (the tail end here is 11, then 13)
    12345678--87654321@13579111315   (the tail end here is 11, then 13, then 15)

    Preconditions:  r is a positive number.
    For purposes of "lining up", assume r is a single digit.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION:
    #    You may NOT use string multiplication in this problem.
    #  HINT:  PARTIAL CREDIT is available for each PIECE that you get right.
    #    Do part of the picture, get it right, then ... etc.
    #    If you cannot get a part right, skip to the next part.
    # -------------------------------------------------------------------------
    for k in range(1,r+1):
        num=k
        while num<=r:
            print(num, end="")
            num=num+1
        for j in range(k+1):
            print("-", end="")
        for m in range(r, 0, -1):
            print(m, end="")
        print("@", end="")
        new_num=k
        counter=1
        while new_num<=r:
            print(2*counter-1, end="")
            new_num=new_num+1
            counter=counter+1
        print()
    for k in range(r, 0, -1):
        num = k
        while num <= r:
            print(num, end="")
            num = num + 1
        for j in range(k + 1):
            print("-", end="")
        for m in range(r, 0, -1):
            print(m, end="")
        print("@", end="")
        new_num = k
        counter = 1
        while new_num <= r:
            print(2 * counter - 1, end="")
            new_num = new_num + 1
            counter = counter + 1
        print()



###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(arguments, expected, test_results,
                                  format_string, suffix=""):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results, precision=None):
    testing_helper.print_actual_result_of_test(expected, actual, test_results,
                                               precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
