"""
Exam 3, problem 3.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3  function:')
    print('--------------------------------------------------')

    format_string = '    problem3( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Tests 1 and 2:
    numbers = ([5, 2],  # indices sum to 0 and 1, respectively - no match
               [3, 1, 2],  # indices sum to 1, 2 and 3, respectively - no match
               [6, 3, 4, 5, 6, 10],  # indices for 3 sum to 3, so MATCH
               [3, 6, 5, 0])  # Past a match, not examined)
    expected_for_mutation = ([5, 2],
                             [3, 1, 2],
                             [6, -1, 4, 5, 6, 10],  # The 3 changed to a -1
                             [3, 6, 5, 0])
    expected = (2, 1)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 3 and 4:
    numbers = ([0, 1, 2, 3, 4],
               [1, 4, 4, 1, 1, 1, 7],
               [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 7])
    expected_for_mutation = ([-1, 1, 2, 3, 4],  # The 0 changed to -1
                             [1, 4, 4, 1, 1, 1, 7],
                             [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
                             [1, 2, 3, 4, 7])
    expected = (0, 0)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 5 and 6:
    numbers = ([10, 1, 2, 3, 4],
               [1, 4, 4, 1, 1, 1, 7],
               [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 7])
    expected_for_mutation = ([10, -1, 2, 3, 4],  # The 1 changed to -1
                             [1, 4, 4, 1, 1, 1, 7],
                             [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
                             [1, 2, 3, 4, 7])
    expected = (0, 1)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 7 and 8:
    numbers = ([10, 0, 0, 30, 4],
               [1, 4, 4, 1, 1, 1, 7],
               [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 7])
    expected_for_mutation = ([10, 0, 0, 30, -1],  # The 4 changed to -1
                             [1, 4, 4, 1, 1, 1, 7],
                             [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
                             [1, 2, 3, 4, 7])
    expected = (0, 4)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 9 and 10:
    numbers = ([10, 0, 0, 30, 14],
               [1, 4, 4, 1, 1, 1, 7],
               [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 7])
    expected_for_mutation = ([10, 0, 0, 30, 14],
                             [-1, 4, 4, 1, 1, 1, 7],  # The 1 changed to -1
                             [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
                             [1, 2, 3, 4, 7])
    expected = (1, 0)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 11 and 12:
    numbers = ([10, 0, 0, 30, 0],
               [0, 4, 4, 1, 1, 1, 7],
               [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 7])
    expected_for_mutation = ([10, 0, 0, 30, 0],
                             [0, 4, 4, 1, 1, 1, -1],  # The 7 changed to -1
                             [6, 3, 4, 3, 4, 5, 6, 7, 8, 9],
                             [1, 2, 3, 4, 7])
    expected = (1, 6)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 13 and 14:
    numbers = ([10, 0, 0, 30, 40],
               [10, 4, 4, 1, 1, 1, 70],
               [100],
               [100, 200],
               [6, 5, 4, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 7])
    expected_for_mutation = ([10, 0, 0, 30, 40],
                             [10, 4, 4, 1, 1, 1, 70],
                             [100],
                             [100, 200],
                             [6, -1, 4, 3, 4, 5, 6, 7, 8, 9],  # The 5 to -1
                             [1, 2, 3, 4, 7])
    expected = (4, 1)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 15 and 16:
    numbers = ([10, 0, 0, 30, 0],
               [10, 4, 4, 1, 1, 1, 6],
               [6],
               [1, 2, 3, 4, 7])
    expected_for_mutation = ([10, 0, 0, 30, 0],
                             [10, 4, 4, 1, 1, 1, 6],
                             [6],
                             [1, 2, 3, 4, -1])  # The 7 changed to -1
    expected = (3, 4)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # Tests 17 and 18:
    numbers = ([10, 0, 0, 30, 14],
               [0, 4, 4, 1, 1, 1, 17],
               [6],
               [1, 2, 3, 4, 6])
    expected_for_mutation = ([10, 0, 0, 30, 14],
                             [0, 4, 4, 1, 1, 1, 17],
                             [6],
                             [1, 2, 3, 4, 6])  # No changes
    expected = None
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem3(numbers)
    print_actual_result_of_test(expected, actual, test_results)
    print_result_of_mutation(expected_for_mutation, numbers, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3(numbers):
    """
    What comes in:  A non-empty sequence of non-empty sequences
      of positive integers.
    What goes out:  Finds the first integer in the sub-sequences that
      is equal to the sum of its indices, and returns a 2-tuple that contains
      those indices.  Returns None if there are no such numbers.
    Side effects:  Mutates the found integer to -1.
    Examples:
      Suppose that  numbers  is:
          ([5, 2],  # indices sum to 0 and 1, respectively - no match
           [3, 1, 2],  # indices sum to 1, 2 and 3, respectively - no match
           [6, 3, 4, 5, 6, 10],  # indices for 3 sum to 3, so MATCH
           [3, 6, 5, 0])  # Past a match, not examined
      Then: problem3(numbers) mutates the 3 whose indices are 2 and 1 to -1
                       and    returns (2, 1).
      ** ASK YOUR INSTRUCTOR FOR HELP **
      ** if this example and the above specification are not clear to you. **
     """
    ###########################################################################
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #  IMPORTANT: The test cases do NOT test what gets printed!
    #  See the testing code above for what should get printed on each test.
    ###########################################################################
    for k in range(len(numbers)):
        for j in range(len(numbers[k])):
            if numbers[k][j]== k+j:
                numbers[k][j]=-1
                return (k, j)
    return None

###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(arguments, expected, test_results,
                                  format_string, suffix=""):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_result_of_mutation(expected, after_function_call, test_results):
    print("Regarding the mutation, after the function call,")
    print("the list was expected to be and actually was as follows:")
    print("  Expected:", expected)
    print_actual_result_of_test(expected, after_function_call, test_results)


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
