"""
Exam 1, problem 1.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time

###############################################################################
# DONE: 2. Right-click on the  src  folder and
#              Mark Directory as ... Sources Root,
#          if you have not already done so.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1a   function:")
    print("--------------------------------------------------")

    format_string = '    problem1a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 22143
    print_expected_result_of_test([5, 3], expected, test_results,
                                  format_string)
    actual = problem1a(5, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 10922
    print_expected_result_of_test([7, 2], expected, test_results,
                                  format_string)

    actual = problem1a(7, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 0.65625
    print_expected_result_of_test([3, 0.5], expected, test_results,
                                  format_string)
    actual = problem1a(3, 0.5)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 1071292029505993517027974728227441735014801995855195223534250
    print_expected_result_of_test([100, 2], expected, test_results,
                                  format_string)
    actual = problem1a(100, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 123456789
    print_expected_result_of_test([1, 123456789], expected, test_results,
                                  format_string)
    actual = problem1a(1, 123456789)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = -1071292029505993517027974728227441735014801995855195223534250
    print_expected_result_of_test([100, -2], expected, test_results,
                                  format_string)
    actual = problem1a(100, -2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 951512.6098151148
    print_expected_result_of_test([35, 1.2], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem1a(35, 1.2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 8:
    expected = 951512.6098151148 + (1.2 ** ((2 * 35) + 1))
    print_expected_result_of_test([36, 1.2], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem1a(36, 1.2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 9:
    expected = 951512.6098151148 - (1.2 ** ((2 * 34) + 1))
    print_expected_result_of_test([34, 1.2], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem1a(34, 1.2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 10:
    expected = 101.0066492971527
    print_expected_result_of_test([100, 1.0001], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem1a(100, 1.0001)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results, precision=10)

    # Test 11:
    expected = 1107.0080699082819
    print_expected_result_of_test([1000, 1.0001], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem1a(1000, 1.0001)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results, precision=10)

    # Test 12:
    expected = -1107.0080699082819
    print_expected_result_of_test([1000, -1.0001], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem1a(1000, -1.0001)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results, precision=10)

    print_summary_of_test_results(test_results)


def problem1a(m, r):
    """
    What comes in:  A positive integer m and a number r.
    What goes out:
      -- Returns the sum of the first  m  terms of the series that begins:
             r  +  (r ** 3)  +  (r ** 5)  +  (r ** 7)  +  (r ** 9)  +  ...
    Side effects:   None.
    Examples:
      -- If m = 5 and r = 3, this function returns:
            3  +  (3 ** 3)  +  (3 ** 5)  +  (3 ** 7)  +  (3 ** 9),
              which is 22143
      -- If m = 7 and r = 2, this function returns:
            2 + 8 + 32 + 128 + 512 + 2048 + 8192,    which is 10922
      -- If m = 3 and r = 0.5, this function returns
            0.5  +  (0.5 ** 3)  +  (0.5 ** 5),       which is 0.65625
      -- Ask for help if you do not understand the above examples.
    """
    ###########################################################################
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    sum=0
    for k in range(m):
        sum=sum+r**(2*k+1)
    return sum

def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    format_string = '    problem1b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 682
    print_expected_result_of_test([5],
                                  expected, test_results, format_string)
    actual = problem1b(5)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 10
    print_expected_result_of_test([2],
                                  expected, test_results, format_string)
    actual = problem1b(2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)

    # Test 3:
    expected = 267823007376498379256993682056860433753700498963798805883562
    print_expected_result_of_test([99],
                                  expected, test_results, format_string)
    actual = problem1b(99)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)

    # Test 4:
    expected = 2
    print_expected_result_of_test([1], expected, test_results,
                                  format_string)
    actual = problem1b(1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 699050
    print_expected_result_of_test([10], expected, test_results,
                                  format_string)
    actual = problem1b(10)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 2796202
    print_expected_result_of_test([11], expected, test_results,
                                  format_string)
    actual = problem1b(11)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 174762
    print_expected_result_of_test([9], expected, test_results,
                                  format_string)
    actual = problem1b(9)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 1071292029505993517027974728227441735014801995855195223534250
    print_expected_result_of_test([100], expected, test_results,
                                  format_string)
    actual = problem1b(100)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem1b(m):
    """
    What comes in:  A positive integer m.
    What goes out:
      -- Returns the sum of the first  m  terms of the series that begins:
             2  +  (2 ** 3)  +  (2 ** 5)  +  (2 ** 7)  +  (2 ** 9)  +   ...
    Side effects:   None.
    Examples:
      -- If m = 5, this function returns:
            2 + 8 + 32 + 128 + 512, which is 682
      -- If m = 2, this function returns:
            2 + 8, which is 10
      -- Ask for help if you do not understand the above examples.
    """
    ###########################################################################
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################

    return problem1a(m, 2)
###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=""):
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
    time.sleep(1)
    raise
