"""
Exam 2, problem 3.
Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time
import sys


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3a()
    run_test_problem3b()


def run_test_problem3a():
    """ Tests the   problem3a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3a  function:')
    print('--------------------------------------------------')

    format_string = '    problem3a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 22
    sequence = (30, 1, 22, 7, 5)
    r = 4
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 0
    sequence = (5, 20, 0, 0, 0, 0, 0, 0, 0)
    r = 7
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -2
    sequence = (100, -4, -11, -2, -4, -4)
    r = 5
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 0
    sequence = (4, 3, 2, 1, 0)
    r = 1
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 17
    sequence = [9, 15, 2, 20, 13, 6, 8, 1, 17]
    r = 5
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 11
    sequence = [5, 4, 11, 2, 4, 4]
    r = 5
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = -2
    sequence = [100, -4, -11, -2, -4, -4]
    r = 5
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 0
    sequence = (4, 3, 2, 1, 0)
    r = 1
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = None
    sequence = [1, 2, 15, 21]
    r = 0
    print_expected_result_of_test([sequence, r],
                                  expected, test_results, format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 100
    sequence = [1, 100, 1, 100]
    r = 3
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = -99999999999999999999999999999999
    sequence = [-99999999999999999999999999999999]
    r = 1
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = -99999999999999999999999999999999
    sequence = [-99999999999999999999999999999999,
                -99999999999999999999999999999999]
    r = 2
    print_expected_result_of_test([sequence, r], expected, test_results,
                                  format_string)
    actual = problem3a(sequence, r)
    print_actual_result_of_test(expected, actual, test_results)

    # Tests 13 and following try putting the biggest item in various places,
    #  with r being all values that include the place where the biggest is.
    #  More precisely:
    #    Start with a fixed sequence.
    #    For k in range(len(sequence)):
    #      Put BIGGEST, a slightly larger number than max(sequence),
    #      into index k.  Run problem3a on the new sequence
    #      with r in range(len(sequence) - k, en(sequence) + 1).
    #      Expected is always BIGGEST for these values of r,
    #      and is always max(sequence) for all other values of r
    #      because I put the max(sequence) at the end of the sequence.
    sequence = [10, 5, 20, -40, 133, 89, 90, 43, 99, 133.001]
    biggest = max(sequence) + 0.000001
    second_biggest = max(sequence)
    for k in range(len(sequence)):
        old = sequence[k]
        sequence[k] = biggest
        expected = biggest
        for r in range(len(sequence) - k, len(sequence) + 1):
            print_expected_result_of_test([sequence, r], expected,
                                          test_results, format_string)
            actual = problem3a(sequence, r)
            print_actual_result_of_test(expected, actual, test_results)
        expected = second_biggest
        for r in range(1, len(sequence) - k):
            print_expected_result_of_test([sequence, r], expected,
                                          test_results, format_string)
            actual = problem3a(sequence, r)
            print_actual_result_of_test(expected, actual, test_results)
        sequence[k] = old

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


# See the IMPORTANT NOTE in the _TODO_ for this problem.
def problem3a(sequence, r):
    """
    What comes in: A sequence of numbers and an integer r.
        You may assume that the sequence contains at least r numbers.
    What goes out:
        -- Returns the LARGEST of the LAST r numbers in the sequence.
            If r is 0, returns None.
    Side effects:   None.
    Examples:
        -- problem3a( [30, 1, 22, 7, 5],  4 )
               returns 22
            (which is the largest out of 1, 22, 7, and 5)
        -- problem3a( [5, 20, 0, 0, 0, 0, 0, 0, 0],  7 )
               returns 0
            (which is the largest out of 0, 0, 0, 0, 0, 0, and 0)
        -- problem3a( [100, -4, -11, -2, -4, -4],  5 )
               returns -2
            (which is the largest out of -4, -11, -2, -4, and -4)
        -- problem3a( [4, 3, 2, 1, 0],  1 )
               returns 0
            (which is the largest out of 0)
        -- problem3a( [1, 2, 15, 21],  0 )
               returns None
            (since r equals 0)
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #   ** IMPORTANT NOTE:
    #      You may NOT use the builtin   max   function on this problem,
    #      nor may you use slices (if you know what they are). **
    # -------------------------------------------------------------------------
    if r==0:
        return None
    largest=sequence[-1]
    for k in range(-2, -r-1, -1):
        if sequence[k]>largest:
            largest=sequence[k]
    return largest

def run_test_problem3b():
    """ Tests the   problem3a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3b  function:')
    print('--------------------------------------------------')

    format_string = '    problem3b( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [-5, -6 , 0, 7, 12, -15]
    seq = [-5, -6, 11, 7, 12, -15]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # Test 2:
    expected = [-5, -6 , 15, -5, 0, -15]
    seq = [-5, -6 , 15, -5, 1, -15]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # Test 3:
    expected = [0, -6 , 15, -5, 1, -15]
    seq = [0, -6 , 15, -5, 1, -15]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # Test 4:
    expected = [-5, 0, -5, 5, -5, 5, -5]
    seq = [-5, 5, -5, 5, -5, 5, -5]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # Test 5:
    expected = [-5, 100]
    seq = [-5, 100]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # Test 6:
    expected = [-4, 3, 0, 2, 0]
    seq = [-4, 3, 1, 2, 0]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # Test 7:
    expected = [-4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
    seq = [-4, 3, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # Test 8:
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    seq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print_expected_result_of_test(seq, expected, test_results, format_string,
                                  'for mutated argument')
    # noinspection PyNoneFunctionAssignment
    returned_value = problem3b(seq)
    print_actual_result_of_test(expected, seq, test_results)
    print_mutation_vs_returned(seq, expected, returned_value, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3b(sequence):
    """
       What comes in: A sequence of numbers.
       What goes out: Nothing.
       Side effects:  MUTATES the given list to replace the FIRST instance
         in which the sum of the numbers in the list up to that point equals 0
         with the number 0.  SEE EXAMPLES.
       Examples:
           -- problem3b([-5, -6, 11, 7, 12, -15]) MUTATES the given sequence
                     to [-5, -6,  0, 7, 12, -15]
                because -5 + -6 + 11 = 0
                so 11 is replaced by 0 in the sequence.
           -- problem3b([-5, -6 , 15, -5, 1, -15]) MUTATES the given sequence
                     to [-5, -6 , 15, -5, 0, -15]
                because -5 + -6 + 15 + -5 + 1 = 0,
                so 1 is replaced by 0 in the sequence.
           -- problem3b([0, -6, 6, -5, 1, -15])  DOES NOT CHANGE the given
                sequence because 0 is the FIRST item in which the sum of the
                numbers in the list up to that point is 0,
                so 0 is replaced by 0 (and no other changes are made).
           -- problem3b([-5, 5, -5, 5, -5, 5, -5]) MUTATES the given sequence
                     to [-5, 0, -5, 5, -5, 5, -5]
                because -5 + 5 = 0, so the FIRST 5 is replaced by 0
                in the sequence (and no other changes are made).
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    sum= sequence[0]
    k=1
    while True:
        sum=sum+sequence[k]
        if sum==0:
            sequence[k]=0
            break;
        k=k+1
        if k>len(sequence)-1:
            break;

###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_mutation_vs_returned(arg, expected, returned, test_results):
    if returned is None:
        return
    if arg == expected:
        print()
        print("You mutated the argument correctly,", color="blue")
        print("but you incorrectly returned a value.", color="red")
        test_results[0] = test_results[0] - 1
        test_results[1] = test_results[1] + 1
    elif returned == expected:
        print()
        print("You did NOT mutate the argument correctly,", color="red")
        print("but you DID ** return ** the value", color="blue")
        print("to which the argument SHOULD mutate.", color="blue")
        print("If you cannot get the mutation to work,", color="red")
        print("leave your solution as is for partial credit.", color="red")
    else:
        print()
        print("You did NOT mutate the argument correctly (see above).",
              color="red")
        print("Also, this function should NOT return a value.", color="red")
        print("You returned " + str(returned), color="red")


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
