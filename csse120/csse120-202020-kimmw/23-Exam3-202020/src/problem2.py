"""
Exam 3, problem 2.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time
import random
import sys

# Checks that your version of Python is reasonably up to date, which is
# important to the pseudo-random number generation in a function below.
if int(sys.version[2]) < 5:
    print("WARNING: Your version of Python may not work correctly")
    print("for this exam.  SEE YOUR INSTRUCTOR FOR WHAT TO DO.")
    exit(1)


def main():
    """ Calls the   TEST   functions in this module. """
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')
    print()

    run_test_problem2a()
    run_test_problem2b()


def run_test_problem2a():
    """ Tests the   problem2a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a  function:')
    print('--------------------------------------------------')

    format_string = '    problem2a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = ([5, 1, 8, 3],
               [0, -3, 7, 8, 1],
               [6, 3, 5, 5, -10, 12])
    expected = 5 + 8 + 7 + 8 + 6 + 5 + 5 + 12  # which is 56 (A = 17/4 = 4.25)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    numbers = ([5, 1, 1, 1, 1, 3],
               [1, 4, 4, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 2, 1])
    # so A = 12/6 = 2 and
    expected = 5 + 3 + 4 + 4 + 6 + 3 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 3  # = 70
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    numbers = ([5, 1, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 151
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    numbers = ([1, 2, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 148
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    numbers = ([100, 200, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 300
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = ([100, 200, 99],
               [300])
    expected = 500
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    numbers = ([98, 200, 99],
               [300])
    expected = 500
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    numbers = ([100, 200, 99],
               [50])
    expected = 200
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    numbers = ([-4],
               [],
               [],
               [-3, 0, 1, 2, 3],
               [-3.99],
               [-4.0000000001])
    expected = -0.99  # from -3 + 0 + 1 + 2 + 3 + (-3.99)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results, precision=6)

    # Test 10:
    numbers = ([-99999999999],
               [],
               [])
    expected = 0
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    numbers = ([1, 4],
               [3, 3, 3, 3],
               [],
               [2.49, 2.48, 2.49],
               [])
    expected = 4 + 3 + 3 + 3 + 3  # = 16
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    numbers = ([1, -1],)
    expected = 1
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem2a(numbers):
    """
    What comes in:  A non-empty sequence of sequences of numbers,
      with the first sub-sequence being non-empty.
    What goes out:  Returns the sum of all the numbers in the subsequences
      that are bigger than A,
      where A is the average of the numbers in the FIRST sub-sequence.
    Side effects:  None.
    Examples:
      Suppose that  numbers  is:
          ([5, 1, 8, 3],
           [0, -3, 7, 8, 1],
           [6, 3, 5, 5, -10, 12])
      Then: the average of the numbers in the first sub-sequence is
        (5 + 1 + 8 + 3) / 4, which is 17 / 4, which is 4.25, and so
        problem2a(numbers)   returns   (5 + 8 + 7 + 8 + 6 + 5 + 5 + 12),
        which is 56, since the numbers in that sum are the numbers
        in the subsequences that are bigger than 4.25.
      ** ASK YOUR INSTRUCTOR FOR HELP **
      ** if this example and the above specification are not clear to you. **

     """
    ###########################################################################
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    A=0
    for k in range(len(numbers[0])):
        A=A+numbers[0][k]
    A=A/len(numbers[0])
    print(A)
    sum=0
    for k in range(len(numbers)):
        for j in range(len(numbers[k])):
            if numbers[k][j]>A:
                sum=sum+numbers[k][j]
    return sum


###############################################################################
# DONE: 3.
#   READ the doc-string for the   is_interesting   function defined below.
#   *** Do not continue until you UNDERSTAND the DOC-STRING
#       for the  is_interesting  function.  ASK QUESTIONS AS NEEDED!
###############################################################################
def is_interesting(r):
    """
    What comes in: A positive integer r.
    What goes out:  Returns True if r is "interesting", returns False otherwise.
      You do not need to know exactly what "interesting" means.
    Type hints:
      :type r: int
      :rtype   bool
    """
    # The following CODE is of NO INTEREST to you.
    # Do NOT attempt to figure it out.  Just accept what the doc-string says.
    random.seed(r)
    return random.randrange(5) == 0


def run_test_problem2b():
    """ Tests the   problem2b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b  function:')
    print('--------------------------------------------------')

    format_string = '    problem2b( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    n = 5
    m = 22
    expected = 28 + 31 + 32 + 42 + 43  # which is 176
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    n = 3
    m = 14
    expected = 14 + 19 + 28  # which is 61
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    n = 4
    m = 14
    expected = 14 + 19 + 28 + 31  # which is 92
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    n = 5
    m = 1
    expected = 2 + 14 + 19 + 28 + 31  # which is 94
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    n = 1
    m = 16
    expected = 19
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    n = 0
    m = 16
    expected = 0
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    n = 1000
    m = 103
    expected = 2493116
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    n = 3000
    m = 1923
    expected = 27891567
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    n = 50000
    m = 367
    expected = 6248470683
    print_expected_result_of_test([n, m], expected, test_results,
                                  format_string)
    actual = problem2b(n, m)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem2b(n, m):
    """
    What comes in: Positive integers n and m.
    What goes out:  Returns the sum of the first  n  integers,
      starting with m, that are "interesting",
      according to the  is_interesting  function defined above.
    Side effects:  None.
    Examples:
      It so happens that the only "interesting" numbers between 1 and 50 are:
          2, 14, 19, 28, 31, 32, 42, 43, 46 and 49.  (Take my word for it!)
      Hence:
         problem2b(5, 22)   returns  28 + 31 + 32 + 42 + 43, which is 176
         problem2b(3, 14)   returns  14 + 19 + 28, which is 61
         problem2b(4, 14)   returns  14 + 19 + 28 + 31, which is 92
         problem2b(5, 1)    returns   2 + 14 + 19 + 28 + 31, which ix 94
         problem2b(1, 16)   returns  19
         problem2b(0, 16)   returns  0
      ** Do NOT make any assumptions about what   is_interesting   returns;
      ** just call it as needed!  ASK YOUR INSTRUCTOR FOR HELP
      ** if these examples and the above specification are not clear to you.
    :type n: int
    :type m: int
    :type p: float
    :rtype   list[int]
    """
    ###########################################################################
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    start=m
    sum=0
    while True:
        if is_interesting(start)== True:
            break
        start=start+1
    count=0

    while count<n:
        if is_interesting(start) is True:
            sum=sum+start
            start=start+1
            count=count+1
        else:
            start=start+1
    return sum

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
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
