"""
Exam 2, problem 1.
Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time
import sys


def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    run_test_problem1a()
    run_test_problem1b()


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a  function:')
    print('--------------------------------------------------')

    format_string = '    problem1a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 3
    sequence = (3, 1, 5, 5, 2, 8, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 2
    sequence = (30, 1, 22, 8, 5)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 1
    sequence = (20, -20)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 0
    sequence = [20, 20]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 4
    sequence = [8, 30, 40, 50, 1, 3, 66, 8]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence = (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    sequence = [10000000000000000000000]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 0
    sequence = [-100000000000000000000]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    sequence = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.001)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 2
    sequence = (1.1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 9
    sequence = (-0.999, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 9
    sequence = (1, 1, 1, 1, 1, 1, 1, 1, 1, -0.999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 3
    sequence = (100, 110, 90, 5000, 4000, 4000, 33, 50, 100)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 6
    sequence = (9.998, 10, 10, 10, 10, 10, 9.998, 10)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 4
    sequence = (9.998, 10, 10, 10, 10, 9.998, 9.998)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = 1
    sequence = (0, 0, 0, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17:
    expected = 2
    sequence = (0, 0, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = 3
    sequence = (0, 1, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19:
    expected = 0
    sequence = (1, 1, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 20:
    expected = 500
    sequence = []
    for k in range(1000):
        sequence.append(k)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 21:
    expected = 499
    sequence = []
    for k in range(999):
        sequence.append(998 - k)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1a(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


# See IMPORTANT NOTE in the _TODO_ for this problem!
def problem1a(sequence):
    """
    What comes in: A sequence of numbers.
    What goes out:
        -- Returns the number of items in the sequence that are strictly
             greater than the average of the items in the sequence.
    Side effects: None.
    Examples:
        -- problem1a ( [3, 1, 5, 5, 2, 8, 4] ) has an average of
             (3 + 1 + 5 + 5 + 2 + 8 + 4) / 7, which is 28 / 7, which is 4.
             There are 3 items that are strictly greater than 4
             (namely 5, 5, and 8) so this function call returns 3.
        -- problem1a ( [30, 1, 22, 8, 5] ) has an average of 66/5 which is 13.2.
                There are 2 items that are strictly greater than 13.2
                (namely 30 and 22) so this function call returns 2.
        -- problem1a ( [20, -20] ) has an average of 0.
                There is 1 item that is strictly greater than 0 (namely 20)
                so this function call returns 1.
        -- problem1a ( [20, 20] ) has an average of 20.
                There are 0 items that are STRICTLY greater than 20
                so this function call returns 0.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #   ** IMPORTANT NOTE:
    #      You may NOT use the builtin function   sum   in this problem. ***
    # -------------------------------------------------------------------------
    sum=0
    for k in sequence:
        sum=sum+k
    average=sum/len(sequence)
    count=0
    for k in sequence:
        if k>average:
            count=count+1
    return count

def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b  function:')
    print('--------------------------------------------------')

    format_string = '    problem1b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [2, 3, 5]
    sequence = (3, 1, 5, 5, 2, 8, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [0, 2]
    sequence = (30, 1, 22, 8, 5)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = [0]
    sequence = (20, -20)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = []
    sequence = [20, 20]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [1]
    sequence = [-20, 20]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = [1, 2, 3, 6]
    sequence = [8, 30, 40, 50, 1, 3, 66, 8]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = [1, 3]
    sequence = [24, 905, 3, 1234]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = []
    sequence = [905]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = [6]
    sequence = [0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = [5, 15]
    sequence = [0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sequence = (-0.999, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    sequence = (1, 1, 1, 1, 1, 1, 1, 1, 1, -0.999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = [3, 4, 5]
    sequence = (100, 110, 90, 5000, 4000, 4000, 33, 50, 100)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = [1, 2, 3, 4, 5, 7]
    sequence = (9.998, 10, 10, 10, 10, 10, 9.998, 10)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = [1, 2, 3, 4]
    sequence = (9.998, 10, 10, 10, 10, 9.998, 9.998)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = [3]
    sequence = (0, 0, 0, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17:
    expected = [2, 3]
    sequence = (0, 0, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = [1, 2, 3]
    sequence = (0, 1, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19:
    expected = []
    sequence = (1, 1, 1, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 20:
    expected = [0, 2]
    sequence = (1, 0, 1, 0)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 21:
    expected = [1, 3]
    sequence = (0, 1, 0, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 22:
    expected = [0, 1, 3]
    sequence = (1, 1, 0, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 23:
    expected = [0, 3]
    sequence = (1, 0, 0, 1)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 24:
    expected = []  # With numbers appended below
    sequence = []
    for k in range(1000):
        sequence.append(k)
        if k >= 500:
            expected.append(k)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 25:
    expected = []  # With numbers appended below
    sequence = []
    for k in range(1001):
        sequence.append(998 - k)
        if k < 500:
            expected.append(k)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


# See IMPORTANT NOTE in the _TODO_ for this problem!
def problem1b(sequence):
    """
    What comes in: A sequence of numbers.
    What goes out:
        -- Returns a list of the indices (places) of the given sequence
             at which the item at that index (place) is strictly greater than
             the average of the given sequence.  The numbers in the returned
             list should be in increasing order -- see the examples.
    Side effects: None.
    Examples:
        --- problem1b ( [3, 1, 5, 5, 2, 8, 4] ) has an average of
             (3 + 1 + 5 + 5 + 2 + 8 + 4) / 7, which is 28 / 7, which is 4.
             There are 3 items that are strictly greater than 4
             (namely 5, 5, and 8) and those items are at indices 2, 3, and 5,
             so this function call returns [2, 3, 5].
        -- problem1b ( [30, 1, 22, 8, 5] ) has an average of 66/5 which is 13.2.
                There are 2 items that are strictly greater than 13.2
                (namely 30 and 22, at indices 0 and 2)
                so this function call returns [0, 2].
        -- problem1b ( [20, -20] ) has an average of 0.
                There is 1 item that is strictly greater than 0 (namely 20,
                at index 0, so this function call returns [0].
        -- problem1b ( [20, 20] ) has an average of 20.
                There are 0 items that are STRICTLY greater than 20
                so this function call returns [].
     """
    ###########################################################################
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #   ** IMPORTANT NOTE:
    #      You may NOT use the builtin function   sum   in this problem. ***
    ###########################################################################
    list=[]
    sum=0
    for k in sequence:
        sum=sum+k
    average=sum/len(sequence)
    for k in range(len(sequence)):
        if sequence[k]>average:
            list.append(k)
    return list

###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


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
    sys.stdout.flush()
    time.sleep(1)
    raise
