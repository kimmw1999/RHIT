"""
PRACTICE Exam 2, practice_problem 2.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Exam 2 question.
#     5 is a "typical" Exam 2 question.
#     7 is a "hard" Exam 2 question.
#    10 is an EXTREMELY hard problem (too hard for an Exam 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
###############################################################################

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_practice_problem2a()
    run_test_practice_problem2b()
    run_test_practice_problem2c()
    run_test_practice_problem2d()


###############################################################################
# Students: Some of the testing code below uses a simple testing framework.
# Ask for help if the tests that we supply are not clear to you.
###############################################################################

def run_test_practice_problem2a():
    """ Tests the   practice_problem2a  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2a   function:')
    print('--------------------------------------------------')

    format_string = '    problem1a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [8, 16, 11, -14, 14]
    print_expected_result_of_test([[2, 10, 5, -20, 8], 6], expected,
                                  test_results, format_string)
    actual = practice_problem2a([2, 10, 5, -20, 8], 6)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [800]
    print_expected_result_of_test([[795], 5], expected, test_results,
                                  format_string)
    actual = practice_problem2a([795], 5)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    print_expected_result_of_test([[], 50], expected, test_results,
                                  format_string)
    actual = practice_problem2a([], 50)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [1, 1, 2, 3, 10, -11, 12, 0, 0, 1]
    print_expected_result_of_test([[1, 1, 2, 3, 10, -11, 12, 0, 0, 1], 0],
                                  expected, test_results, format_string)
    actual = practice_problem2a([1, 1, 2, 3, 10, -11, 12, 0, 0, 1], 0)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [-99, -99, -110, -100, -100, 0]
    print_expected_result_of_test([[1, 1, -10, 0, 0, 100], -100],
                                  expected, test_results, format_string)
    actual = practice_problem2a([1, 1, -10, 0, 0, 100], -100)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def practice_problem2a(sequence, delta):
    """
    What comes in:
      -- A sequence of integers, e.g. ([2, 10, 5, -20, 8])
      -- A number  delta
    What goes out:
      -- Returns a new list that is the same as the given list,
           but with each number in the list having had the given
             delta
           added to it (see example below)
    Side effects: None.
    Example:
       Given the list  [2, 10, 5, -20, 8]  and the number  6,
         this problem returns  [8, 16, 11, -14, 14]
    Type hints:
      :type sequence: [int]
      :type delta:    int
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------
    newList=[]
    for k in range(len(sequence)):
        newList.append(sequence[k]+ delta)
    return newList

def run_test_practice_problem2b():
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this TEST function.
    #   It TESTS the  practice_problem2b  function defined below.
    #   Include at least **   4    ** tests that, taken together,
    #   would form a    ** REASONABLY GOOD test set **
    #   for testing the   practice_problem2b   function defined below.
    #   (We supplied 3 tests, so you need supply only one more.)
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   10 minutes.
    #  --------------------------------------------------------------------
    """ Tests the   practice_problem2b  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2b  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem2b( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    arg1 =  [2, 10, 5, -20, 8]
    correct_arg1_after = [8, 16, 11, -14, 14]
    expected = None

    testing_helper.print_function_call_of_test([arg1, 6], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2b(arg1, 6)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1

    # Test 2:
    arg1 = [1, 1, 2, 3, 10, -11, 12, 0, 0, 1]
    correct_arg1_after = [1, 1, 2, 3, 10, -11, 12, 0, 0, 1]
    expected = None

    testing_helper.print_function_call_of_test([arg1, 0], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2b(arg1, 0)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1

    # Test 3:
    arg1 = [795, -795, 0]
    correct_arg1_after = [-1, -1591, -796]
    expected = None

    testing_helper.print_function_call_of_test([arg1, -796], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2b(arg1, -796)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1

    # -------------------------------------------------------------------------
    # DONE: 3 (continued): Add your ADDITIONAL test(s) below here.
    #   You do NOT have to use the "fancy" parts of the above example tests,
    #   but you MUST test BOTH the returned value AND the mutated list.
    # -------------------------------------------------------------------------
    # Test 4:
    arg1 = [100, 101, 102]
    correct_arg1_after = [0, 1, 2]
    expected = None

    testing_helper.print_function_call_of_test([arg1, -100], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2b(arg1, -100)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1
    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem2b(sequence, delta):
    """
    What comes in:
      -- A sequence of integers, e.g. ([2, 10, 5, -20, 8])
      -- A number  delta
    What goes out: Nothing (i.e., None).
    Side effects:
           MUTATES the given list so that each number in the list has the given
             delta
           added to it (see example below).
    Example:
       Given the list  [2, 10, 5, -20, 8]  and the number  6,
       after the call to this function the value of that given list should be:
         [8, 16, 11, -14, 14]
    Type hints:
      :type sequence: [int]
      :type delta:    int
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #     WRITE THE TESTS FIRST (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------
    for k in range(len(sequence)):
        sequence[k]= sequence[k]+delta

def run_test_practice_problem2c():
    """ Tests the   practice_problem2c  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2c  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem2c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 'hBo'
    print_expected_result_of_test([('hello', 'Bye', 'ok joe')], expected,
                                  test_results, format_string)
    actual = practice_problem2c(('hello', 'Bye', 'ok joe'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 'ABCD'
    print_expected_result_of_test([('Alice', 'Bob', 'Carson', 'Devi')],
                                  expected, test_results, format_string)
    actual = practice_problem2c(('Alice', 'Bob', 'Carson', 'Devi'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 'to!'
    print_expected_result_of_test([('', 'tricky', '', 'one, no?', '!')],
                                  expected, test_results, format_string)
    actual = practice_problem2c(('', 'tricky', '', 'one, no?', '!'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 'mom'
    print_expected_result_of_test([('my very long string', 'ok', 'mmmm')],
                                  expected,
                                  test_results, format_string)
    actual = practice_problem2c(('my very long string', 'ok', 'mmmm'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    jokes = """
        Q: What is it called when a cat wins a dog show?
        A: A CAT-HAS-TROPHY!

        Q: What do you call a pile of kittens?
        A: a meowntain

        Q: Why don't cats like online shopping?
        A: They prefer a cat-alogue.

        Q: What did the cat say when he lost all his money?
        A: I'm paw!

        Q: Did you hear about the cat who swallowed a ball of yarn?
        A: She had a litter of mittens.

        Q: What do you call a lion who has eaten your mother's sister?
        A: An aunt-eater!

        Q: What is it called when a cat wins a dog show?
        A: A CAT-HAS-TROPHY!

        source: http://www.jokes4us.com/animaljokes/catjokes.html
        """
    # 5th test: Split  jokes  at spaces to get a list of strings.
    sequence = jokes.split()
    expected = ('QWiicwacwadsAACQWdycapokAamQWdclosAT' +
                'pacQWdtcswhlahmAIpQDyhatcwsaboyAShalom' +
                'QWdycalwheymsAAaQWiicwacwadsAACsh')

    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem2c(sequence):
    """
    What comes in:
      -- A sequence of strings, e.g. ('hello', 'Bye', 'ok joe')
    What goes out:
      -- Returns the string that contains the first letter in
           each of the strings in the given sequence,
           in the order in which they appear in the sequence.
           (So 'hBo' for the example sequence above).
    Side effects: None.
    Examples:
       Given ['hello', 'Bye', 'ok joe']          returns 'hBo'.
       Given ('Alice, 'Bob', 'Carson', 'Devi')   returns 'ABCD'.
       Given ('', 'tricky', '', 'one, no?', '!') returns 'to!'
       Given [] returns ''
       Given ('my very long string', 'ok', 'mmmm') returns 'mom'
    Type hints:
      :type sequence: [str]
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------
    string=""
    for k in sequence:
        if(len(k)>0):
            string=string+ k[0]
    return string

def run_test_practice_problem2d():
    """ Tests the   practice_problem2d  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2d  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem2d( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2d   function:')
    print('--------------------------------------------------')

    # Test 1:
    arg1 =  [10, -3, 20, 4]
    correct_arg1_after = [20, -6, 40, 8]
    arg2 = [5, 0, 8]
    correct_arg2_after = [5, 0, 8]
    expected = [10, 0, 16]

    testing_helper.print_function_call_of_test([arg1, arg2], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2d(arg1, arg2)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('  Argument 2 is:       ', arg2)
    print('  Argument 2 should be:', correct_arg2_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (arg2 == correct_arg2_after)\
                and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1

    # Test 2:
    arg1 =  []
    correct_arg1_after = []
    arg2 = []
    correct_arg2_after = []
    expected = []

    testing_helper.print_function_call_of_test([arg1, arg2], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2d(arg1, arg2)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('  Argument 2 is:       ', arg2)
    print('  Argument 2 should be:', correct_arg2_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (arg2 == correct_arg2_after)\
                and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1

    # Test 3:
    arg1 =  [1, 2, 3, 0, 1, 2, 3]
    correct_arg1_after = [2, 4, 6, 0, 2, 4, 6]
    arg2 = [0]
    correct_arg2_after = [0]
    expected = [0]

    testing_helper.print_function_call_of_test([arg1, arg2], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2d(arg1, arg2)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('  Argument 2 is:       ', arg2)
    print('  Argument 2 should be:', correct_arg2_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (arg2 == correct_arg2_after)\
                and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1

    # Test 4:
    arg1 = [0]
    correct_arg1_after = [0]
    arg2 = [1, 2, 3, 0, 1, 2, 3]
    correct_arg2_after = [1, 2, 3, 0, 1, 2, 3]
    expected = [2, 4, 6, 0, 2, 4, 6]

    testing_helper.print_function_call_of_test([arg1, arg2], test_results,
                                               format_string)
    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)

    answer = practice_problem2d(arg1, arg2)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)

    print('  Argument 2 is:       ', arg2)
    print('  Argument 2 should be:', correct_arg2_after)

    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    if (arg1 == correct_arg1_after) and (arg2 == correct_arg2_after)\
                and (answer == expected):
        testing_helper.print_colored("  PASSED the above test -- good!",
                                     color='blue')
        test_results[0] = test_results[0] + 1
    else:
        testing_helper.print_colored("  *** FAILED the above test. ***",
                                     color='red')
        test_results[1] = test_results[1] + 1

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem2d(list1, list2):
    """
    What comes in:
      -- Two lists of integers.
    What goes out:
       -- RETURNs a new list that is the same as list2 but with each
          number in the list doubled.
    Side effects:
      -- MUTATEs the first list by doubling each number in the list
    Examples:
      If the two arguments are:
         [10, -3, 20, 4]  and  [5, 0, 8]
      then this method MUTATEs the first argument to [20, -6, 40, 8]
      and RETURNs the list [10, 0, 16]

    Preconditions:
        :type list1: [int]]
        :type list2: [int]]
    """
    # -------------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    #  -------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------
    newList=[]
    for k in range(len(list2)):
        newList.append(list2[k]*2)
    for m in range(len(list1)):
        list1[m]=list1[m]*2
    return newList

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
    time.sleep(1)
    raise
