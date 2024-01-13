"""
Exam 1, problem 2.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time
import math


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2a()
    run_test_problem2b()


###############################################################################
# DONE: 2.  READ the green doc-strings for the:
#     -- get_triangle_perimeter
#     -- get_triangle_area
#   functions defined below.  You do NOT need to understand their
#   implementations, just their specifications (per the doc-strings).
#   You should  ** CALL **  those functions as needed in implementing the
#   other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################
def get_triangle_perimeter(a, b, c):
    """
    What comes in: Three positive integers a, b, and c.
    What goes out:
      -- Returns the perimeter of a triangle formed by sides of
           length a, b, and c.
    Side effects:   None.
    Examples:
      -- get_triangle_perimeter(3, 4, 5) returns  12
      -- get_triangle_perimeter(4, 5, 3) returns  12
      -- get_triangle_perimeter(30, 40, 50) returns  120
      -- get_triangle_perimeter(1, 1, 1) returns  3
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  get_triangle_perimeter   function
    #     - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    return a + b + c


def get_triangle_area(a, b, c):
    """
    What comes in: Three positive integers a, b, and c.
    What goes out:
      -- Returns a floating point approximation of
           the area of a triangle formed by sides of length a, b, and c.
    Side effects:   None.
    Examples:
      -- get_triangle_area(3, 4, 5) returns  6.0
      -- get_triangle_area(4, 5, 3) returns  6.0
      -- get_triangle_area(30, 40, 50) returns  600.0
      -- get_triangle_area(1, 1, 1) returns  0.43301 (approximately)
    Note: The algorithm used here is called Heron's formula.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  get_triangle_perimeter function
    #     - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    s = (a + b + c) / 2
    product = s * (s - a) * (s - b) * (s - c)
    return math.sqrt(product)


def run_test_problem2a():
    """ Tests the   problem2a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('--------------------------------------------------')

    format_string = '    problem2a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 6.0621778
    print_expected_result_of_test([3], expected, test_results, format_string,
                                  suffix="(approximately)")
    actual = problem2a(3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    # Test 2:
    expected = 0.4330127
    print_expected_result_of_test([1], expected, test_results, format_string,
                                  suffix="(approximately)")
    actual = problem2a(1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    # Test 3:
    expected = 2.1650635
    print_expected_result_of_test([2], expected, test_results, format_string,
                                  suffix="(approximately)")
    actual = problem2a(2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    # Test 4:
    expected = 146509.8476852
    print_expected_result_of_test([100], expected, test_results, format_string,
                                  suffix="(approximately)")
    actual = problem2a(100)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    # Test 5:
    expected = 12.9903811
    print_expected_result_of_test([4], expected, test_results, format_string,
                                  suffix="(approximately)")
    actual = problem2a(4)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    # Test 6:
    expected = 142179.7206663
    print_expected_result_of_test([99], expected, test_results, format_string,
                                  suffix="(approximately)")
    actual = problem2a(99)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    # Test 7:
    expected = 150927.0102572
    print_expected_result_of_test([101], expected, test_results, format_string,
                                  suffix="(approximately)")
    actual = problem2a(101)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    # Test 8:
    expected = 144554145.8171362
    print_expected_result_of_test([1000], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem2a(1000)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results,
                                precision=7)

    print_summary_of_test_results(test_results)


def problem2a(n):
    """
    What comes in:  A positive integer n.
    What goes out:
      -- Returns the following sum:
           area of an equilateral triangle each of whose sides has length 1
         + area of an equilateral triangle each of whose sides has length 2
         + area of an equilateral triangle each of whose sides has length 3
         + ...
         + area of an equilateral triangle each of whose sides has length n
      Note: An equilateral triangle is a triangle whose sides
        all have the SAME length.
    Side effects:   None.
    Examples:
        All numbers in the following examples are rounded to 7 decimal places,
        hence approximate.
      -- If n is 3, this function returns 6.0621778 (approximately), since:
           - the area of the triangle (1, 1, 1) is 0.4330127
           - the area of the triangle (2, 2, 2) is 1.7320508
           - the area of the triangle (3, 3, 3) is 3.8971143
                 and 0.4330127 + 1.7320508 + 3.8971143 = 6.0621778

      -- If n is 1, this function returns 0.4330127 (approximately), since:
           - the area of the triangle (1, 1, 1) is 0.4330127

      -- If n is 2, this function returns 2.1650635 (approximately), since:
           - the area of the triangle (1, 1, 1) is 0.4330127
           - the area of the triangle (2, 2, 2) is 1.7320508
                 and 0.4330127 + 1.7320508 = 2.1650635

      -- If n is 100, this function returns 146509.8476852 (approximately),
           since:
           - the area of the triangle (1, 1, 1) is 0.4330127
           - the area of the triangle (2, 2, 2) is 1.7320508
           ...
           - the area of the triangle (99, 99, 99) is 4243.9574912
           - the area of the triangle (100, 100, 100) is 4330.1270189
             and those 100 numbers add up to 146509.8476852 (approximately).

      -- Ask for help if you do not understand the above examples.
     """
    ###########################################################################
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
    ###########################################################################
    total=0
    for k in range(1,n+1):
        total=total+get_triangle_area(k,k,k)
    return total

def run_test_problem2b():
    """ Tests the   problem2b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')

    format_string = '    problem2b( {}, {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 4
    print_expected_result_of_test([10, 2, 8], expected, test_results,
                                  format_string)
    actual = problem2b(10, 2, 8)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 2
    print_expected_result_of_test([5, 3, 5], expected, test_results,
                                  format_string)
    actual = problem2b(5, 3, 5)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 0
    print_expected_result_of_test([100, 50, 150], expected, test_results,
                                  format_string)
    actual = problem2b(100, 50, 150)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 4
    print_expected_result_of_test([100, 1, 199], expected, test_results,
                                  format_string)
    actual = problem2b(100, 1, 199)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 3
    print_expected_result_of_test([10, 2, 5], expected, test_results,
                                  format_string)
    actual = problem2b(10, 2, 5)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 4
    print_expected_result_of_test([10, 2, 6], expected, test_results,
                                  format_string)
    actual = problem2b(10, 2, 6)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 4
    print_expected_result_of_test([10, 2, 7], expected, test_results,
                                  format_string)
    actual = problem2b(10, 2, 7)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 1
    print_expected_result_of_test([10, 5, 6], expected, test_results,
                                  format_string)
    actual = problem2b(10, 5, 6)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 2
    print_expected_result_of_test([10, 4, 6], expected, test_results,
                                  format_string)
    actual = problem2b(10, 4, 6)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 1
    print_expected_result_of_test([10, 5, 7], expected, test_results,
                                  format_string)
    actual = problem2b(10, 5, 7)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 0
    print_expected_result_of_test([10, 6, 7], expected, test_results,
                                  format_string)
    actual = problem2b(10, 6, 7)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 3
    print_expected_result_of_test([5, 3, 6], expected, test_results,
                                  format_string)
    actual = problem2b(5, 3, 6)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 6
    print_expected_result_of_test([5, 3, 9], expected, test_results,
                                  format_string)
    actual = problem2b(5, 3, 9)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 7
    print_expected_result_of_test([5, 3, 10], expected, test_results,
                                  format_string)
    actual = problem2b(5, 3, 10)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 4
    print_expected_result_of_test([8, 1, 5], expected, test_results,
                                  format_string)
    actual = problem2b(8, 1, 5)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = 5
    print_expected_result_of_test([8, 1, 6], expected, test_results,
                                  format_string)
    actual = problem2b(8, 1, 6)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17:
    expected = 5
    print_expected_result_of_test([8, 1, 7], expected, test_results,
                                  format_string)
    actual = problem2b(8, 1, 7)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = 3
    print_expected_result_of_test([8, 5, 16], expected, test_results,
                                  format_string)
    actual = problem2b(8, 5, 16)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    print_summary_of_test_results(test_results)

    # Test 19:
    expected = 2
    print_expected_result_of_test([8, 6, 16], expected, test_results,
                                  format_string)
    actual = problem2b(8, 6, 16)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    print_summary_of_test_results(test_results)

    # Test 20:
    expected = 1
    print_expected_result_of_test([8, 6, 15], expected, test_results,
                                  format_string)
    actual = problem2b(8, 6, 15)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    print_summary_of_test_results(test_results)

    # Test 21:
    expected = 0
    print_expected_result_of_test([8, 6, 14], expected, test_results,
                                  format_string)
    actual = problem2b(8, 6, 14)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    print_summary_of_test_results(test_results)


def problem2b(a, min_value, max_value):
    """
    What comes in:  Positive integers a, min_value, max_value,
                    where max_value > min_value
    What goes out:
      --  Loops through all the possible isosceles triangles whose sides
           have lengths that are, respectively,
             -- the given a,
             -- the given a (again), and
             -- some third integer.
           where the third integer ranges from min_value to max_value
             (including min_value but NOT including max_value)
      -- Returns the number of those isosceles triangles
           whose perimeter is bigger than its area.
      Note: An isosceles triangle is a triangle that has at least two sides
        that are the same length.
    Side effects:   None.
    Examples:  (All floating point numbers in the following examples are
                approximate, i.e., rounded to 7 decimal places.)
      -- If a = 10, min_value = 2, and max_value = 8,
           then this function returns 4, since:
            -- Perimeter of triangle (10, 10, 2) is 22, area is  9.9498744
            -- Perimeter of triangle (10, 10, 3) is 23, area is 14.8302899
            -- Perimeter of triangle (10, 10, 4) is 24, area is 19.5959179
            -- Perimeter of triangle (10, 10, 5) is 25, area is 24.2061459
            -- Perimeter of triangle (10, 10, 6) is 26, area is 28.6181760
            -- Perimeter of triangle (10, 10, 7) is 27, area is 32.7862395
          and 4 of the above triangles (namely, the first 4 listed)
          have a perimeter greater than its area.

      -- If a = 5, min_value = 3, and max_value = 5,
           then this function returns 2, since:
            -- Perimeter of triangle (5, 5, 3) is 13, area is 7.1545440
            -- Perimeter of triangle (5, 5, 4) is 14, area is 9.1651514
          and both of the above triangles have perimeter greater than its area.

      -- If a = 100, min_value = 50, max_value = 150 this function returns 0,
           since triangles (100, 100, 50) up to (100, 100, 149)
             all have smaller perimeter than area.

      -- Ask for help if you do not understand the above examples.
     """
    ###########################################################################
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
    ###########################################################################
    total = 0

    for k in range(max_value-min_value):
        if(get_triangle_perimeter(a,a,k+min_value)>=get_triangle_area(a,a,k+min_value)):
            total=total+1
    return total



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
