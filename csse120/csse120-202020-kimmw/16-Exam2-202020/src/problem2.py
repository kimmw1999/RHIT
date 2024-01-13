"""
Exam 2, problem 2.
Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import typing
import testing_helper


###############################################################################
# The  main  function and the TODOs for you are after this:
###############################################################################
def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    run_test_init()
    run_test_produce_electricity()
    run_test_get_remaining_balance()
    run_test_reset_remaining_balance()
    run_test_get_number_of_balance_resets()
    run_test_double_area_array()
    run_test_change_efficiency()
    run_test_get_best_efficiency()
    run_test_combine_arrays()


###############################################################################
# The   SolarPanelArray   class (and its methods) begins here.
###############################################################################
class SolarPanelArray(object):
    """ Represents a Solar Panel Array that might be on the roof of a house. """

    def __init__(self, efficiency, area, cost):
        """
        What comes in:
          -- self
          -- the efficiency of the panels (% of sun's energy that is
               converted to electricity, often 0.15 to 0.18)
          -- the area of this SolarPanelArray
          -- the cost of this SolarPanelArray, in dollars
        What goes out: Nothing (i.e., None).
        Side effects:
           Sets instance variables:
              self.efficiency
              self.area
              self.cost
           to the given area, efficiency, and cost, respectively.
        Examples:  See tests.
        """
        # ---------------------------------------------------------------------
        # DONE: 2.
        #   a. READ the above specification.
        #      READ the test case supplied in the testing section below.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        A FEW tests are already written (below), but they may not
        #        be adequate to expose all bugs.  Add more tests as desired.
        # ---------------------------------------------------------------------
        self.efficiency=efficiency
        self.area=area
        self.cost=cost
        self.balance=cost
        self.original_cost=cost
        self.count=0
        self.best_efficiency=efficiency
    def produce_electricity(self, sun_energy, cost_of_energy):
        """
        What comes in:
          -- self
          -- the amount of sun energy received today
          -- the cost of energy (Duke Energy's current rate is 11 cents per kWh)
        What goes out:
          -- Returns the amount of energy created IN DOLLARS,
               where the number of dollars produced is equal to
               the given sun energy,
               times the area of this SolarArrayPanel,
               times the efficiency of this SolarArrayPanel,
               times the given cost of energy.
        NOTE: This formula oversimplifies solar energy production,
              but use the formula as specified.
        """
        # ---------------------------------------------------------------------
        # DONE: 3.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        produce=sun_energy * self.area * self.efficiency * cost_of_energy
        self.balance=self.balance-produce
        return produce
    def get_remaining_balance(self):
        """
        When you buy a solar panel array, it has an up-front cost
        but the energy produced that would otherwise cost money is "free"
        in that it comes from the sun (instead of from the power company).
        This  get_remaining_balance  function returns how much of
        the up-front cost remains before this solar panel array has
        "paid for itself", computed as follows:
          -- Originally, the remaining balance is the cost of this
               SolarArrayPanel. (You should have stored that cost
               as an instance variable.)
          -- Every time that the  produce_electricity  method runs,
               the remaining balance should be reduced by the dollars that
               the  produce_electricity  method computes (and returns).
        SEE THE TEST CASES to clarify this specification.
        What comes in:
          -- self
        What goes out:
          -- The remaining balance until this solar panel array has paid
               for itself.
        Side effects: None.
        """
        # ---------------------------------------------------------------------
        # DONE: 4.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        return self.balance
    def reset_remaining_balance(self):
        """
        This method resets the remaining balance.
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        Side effects: Mutates this SolarPanelArray to reset the remaining balance
        back to the original cost of the system.
        """
        # ---------------------------------------------------------------------
        # DONE: 5.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        self.count=self.count+1
        self.balance=self.original_cost
    def get_number_of_balance_resets(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns the number of times the balance has been reset.
        Side effects: None.
        """
        # ---------------------------------------------------------------------
        # DONE: 6.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        return self.count
    def double_area_array(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Return a new SolarPanelArray that costs twice as much as this system
               and has twice as much area, but the same efficiency.
        Side effects: None.
        """
        # ---------------------------------------------------------------------
        # DONE: 7.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        return SolarPanelArray(self.efficiency, self.area*2, self.cost*2)
    def change_efficiency(self, multiplier):
        """
        What comes in:
          -- self
          -- a positive float often between 0.5 and 2.0 that will mutate the
               efficiency.  This value is a multiplier to change the efficiency.
               For example a 2.0 would mean the system efficiency is now twice as
               good (it's double), a 0.9 would mean the system has lost 10% of it's
               efficiency (whatever it is currently, multiplied by 0.9)
        What goes out: Nothing (i.e., None).
        Side effects: Mutates this SolarPanelArray's efficiency
          Note: In real life panels only ever get worse, but this method can mutate
                the efficiency to improve the panels if the multiplier is >1.0.
        """
        # ---------------------------------------------------------------------
        # DONE: 8.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        self.efficiency=self.efficiency*multiplier
        if self.efficiency>self.best_efficiency:
            self.best_efficiency=self.efficiency
    def get_best_efficiency(self):
        """
        What comes in:
          -- self
        What goes out:
          -- The best efficiency this system has ever had
        Side effects: None.
        """
        # ---------------------------------------------------------------------
        # DONE: 9.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        return self.best_efficiency
    def combine_arrays(self, another_solar_panel_array):
        """
        What comes in:
          -- self
        What goes out:
          -- Return a new SolarPanelArray that is the combination of self and
               another_solar_panel_array.  The area is the total area of the
               two systems.  The efficiency is equal to the WORSE of the two
               systems (the bad one bring down the other one to match). And
               the cost is the sum of the initial cost of both systems.
               Note, things like the remaining balance and number of number of
               resets should behave as if the system is new (no resets and the
               remaining balance is the same as the cost).
        Side effects: None.
        """
        # ---------------------------------------------------------------------
        # DONE: 10.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------
        if self.efficiency<= another_solar_panel_array.efficiency:
            worse_efficiency=self.efficiency
        else:
            worse_efficiency=another_solar_panel_array.efficiency
        area=self.area+another_solar_panel_array.area
        cost=self.cost+another_solar_panel_array.cost

        return SolarPanelArray(worse_efficiency, area, cost)

###############################################################################
# The TEST functions for the  SolarPanelArray  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the SolarPanelArray class. """
    print()
    print('--------------------------------')
    print('Testing the   __init__   method.')
    print('--------------------------------')

    # Test 1
    print('\nTest 1:')
    array1 = SolarPanelArray(0.15, 38, 35000)
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # Test 2
    print('\nTest 2:')
    array2 = SolarPanelArray(0.20, 84.5, 40000.10)
    run_test_instance_variables(array2, 0.20, 84.5, 40000.10)

    # Test 3
    print('\nTest 3:')
    array2 = SolarPanelArray(0.34, 184.0, 40000.12)
    run_test_instance_variables(array2, 0.34, 184.0, 40000.12)


def run_test_produce_electricity():
    """ Tests the   produce_electricity   method of the SolarPanelArray class. """
    print()
    print('-------------------------------------------')
    print('Testing the   produce_electricity   method.')
    print('-------------------------------------------')

    format_string = '    produce_electricity( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)
    dollars = array0.produce_electricity(100, 0.20)

    expected = 100 * 50 * 0.15 * 0.20
    print("Expected:",expected )
    print("Actual:  ", dollars)

    if expected == dollars:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    # Test 1: New SolarArrayPanel, produce electricity
    array1 = SolarPanelArray(0.15, 38, 35000)
    sun_energy = 600
    cost_of_energy = 0.10
    expected = 342.0
    print_expected_result_of_test([sun_energy, cost_of_energy], expected,
                                  test_results, format_string,
                                  ' for the returned value')
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    print_actual_result_of_test(expected, dollars_saved, test_results)

    print()  # These instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # Test 2: Produce more electricity
    sun_energy = 1000.5
    cost_of_energy = 0.11
    expected = 627.3135
    print_expected_result_of_test([sun_energy, cost_of_energy], expected,
                                  test_results, format_string,
                                  ' for the returned value')
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    print_actual_result_of_test(expected, dollars_saved, test_results)

    print()  # These instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # Test 3:  Double the SolarArrayPanel's area, then produce more electicity
    array1.area = 76  # Doubling the area, which affects the formula
    sun_energy = 1000.5
    cost_of_energy = 0.1
    expected = 570.285 * 2
    print_expected_result_of_test([sun_energy, cost_of_energy], expected,
                                  test_results, format_string,
                                  ' for the returned value')
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    print_actual_result_of_test(expected, dollars_saved, test_results)

    print()  # These instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 76, 35000)

    # Test 4: Test on another SolarArrayPanel
    array2 = SolarPanelArray(0.23, 50, 20000)
    sun_energy = 800
    cost_of_energy = 0.271
    expected = 2493.2
    print_expected_result_of_test([sun_energy, cost_of_energy], expected,
                                  test_results, format_string,
                                  ' for the returned value')
    dollars_saved = array2.produce_electricity(sun_energy, cost_of_energy)
    print_actual_result_of_test(expected, dollars_saved, test_results)

    print()  # These instance variables should be unchanged.
    run_test_instance_variables(array2, 0.23, 50, 20000)


def run_test_get_remaining_balance():
    """ Tests the   get_remaining_balance   method of the SolarPanelArray class. """
    print()
    print('---------------------------------------------')
    print('Testing the   get_remaining_balance   method.')
    print('---------------------------------------------')

    format_string = '    get_remaining_balance( )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)
    dollars = array0.produce_electricity(100, 0.20)
    remaining_balance = array0.get_remaining_balance()

    expected = 10000 - dollars
    print("Expected:", expected)
    print("Actual:  ", remaining_balance)

    if expected == remaining_balance:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    more_dollars = array0.produce_electricity(900, 0.12)
    remaining_balance = array0.get_remaining_balance()

    expected = 10000 - dollars - more_dollars
    print("Expected:", expected)
    print("Actual:  ", remaining_balance)

    if expected == remaining_balance:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    print("\n*******")
    print("NOTE: These tests require that")
    print("your  produce_electricity  be correct.")
    print("*******")

    # Test 1: New SolarArrayPanel, no electricity produced yet,
    #         so get_remaining_balance should be the initial cost
    array1 = SolarPanelArray(0.15, 38, 35000)
    expected = 35000
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array1.get_remaining_balance()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # These instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # Test 2: Produce some electricity.
    #   This should reduce the remaining balance by the dollars that
    #   produce_electricity returns.
    sun_energy = 600
    cost_of_energy = 0.10
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    expected = 35000 - dollars_saved  # reduce balance remaining by dollars_saved
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array1.get_remaining_balance()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # These instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # Test 3: Produce still more electricity.
    #   This should reduce the remaining balance still further
    #   by the dollars that  produce_electricity  returns.
    sun_energy = 500
    cost_of_energy = 0.20
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    expected = expected - dollars_saved  # reduce balance remaining by dollars_saved
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array1.get_remaining_balance()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # Instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # Test 4: Test on another SolarArrayPanel,
    #   after producing some electricity, twice.
    array2 = SolarPanelArray(0.23, 50, 20000)
    sun_energy = 800
    cost_of_energy = 0.271
    # Produce electricity once:
    dollars_saved = array2.produce_electricity(sun_energy, cost_of_energy)
    expected = 20000 - dollars_saved
    # Produce electricity again:
    sun_energy = 430
    cost_of_energy = 0.123
    array2.area = 150  # Triple the area
    dollars_saved = array2.produce_electricity(sun_energy, cost_of_energy)
    expected = expected - dollars_saved

    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array2.get_remaining_balance()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # Instance variables should be unchanged except triple area.
    run_test_instance_variables(array2, 0.23, 150, 20000)


def run_test_reset_remaining_balance():
    """ Tests the   reset_remaining_balance   method of the SolarPanelArray class. """
    print()
    print('-----------------------------------------------')
    print('Testing the   reset_remaining_balance   method.')
    print('-----------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)
    dollars = array0.produce_electricity(100, 0.20)
    remaining_balance = array0.get_remaining_balance()

    expected = 10000 - dollars
    print("Expected:", expected)
    print("Actual:  ", remaining_balance)

    if expected == remaining_balance:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    array0.reset_remaining_balance()
    remaining_balance = array0.get_remaining_balance()

    expected = 10000
    print("Expected:", expected)
    print("Actual:  ", remaining_balance)

    if expected == remaining_balance:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    print("\n*******")
    print("NOTE: These tests require that")
    print("your  get_remaining_balance  is correct.")
    print("*******")

    format_string = '    reset_remaining_balance( )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # The tests start as they did for get_remaining_balance.

    # Pre-test 1: New SolarArrayPanel, no electricity produced yet,
    #         so get_remaining_balance should be the initial cost.
    array1 = SolarPanelArray(0.15, 38, 35000)
    expected = 35000

    # Pre-test 2: Produce some electricity.
    #   This should reduce the remaining balance by the dollars that
    #   produce_electricity returns.
    sun_energy = 600
    cost_of_energy = 0.10
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    expected = 35000 - dollars_saved  # reduce balance remaining by dollars_saved

    # Pre-test 3: Produce still more electricity.
    #   This should reduce the remaining balance still further
    #   by the dollars that  produce_electricity  returns.
    sun_energy = 500
    cost_of_energy = 0.20
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    expected = expected - dollars_saved  # reduce balance remaining by dollars_saved
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array1.get_remaining_balance()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # Instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # REAL TEST BEGINS HERE: Now do a reset_remaining_balance.
    #   This should return the remaining balance to the original cost.
    array1.reset_remaining_balance()

    # Test 3 (continued): Produce still more electricity.
    #   This should reduce the remaining balance FROM ITS ORIGINAL COST
    #   of 35000 by the dollars that  produce_electricity  returns.
    sun_energy = 500
    cost_of_energy = 0.20
    dollars_saved = array1.produce_electricity(sun_energy, cost_of_energy)
    expected = 35000 - dollars_saved  # reduce balance remaining by dollars_saved
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array1.get_remaining_balance()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # Instance variables should be unchanged.
    run_test_instance_variables(array1, 0.15, 38, 35000)


def run_test_get_number_of_balance_resets():
    """ Tests the   get_number_of_balance_resets   method of the SolarPanelArray class. """
    print()
    print('----------------------------------------------------')
    print('Testing the   get_number_of_balance_resets   method.')
    print('----------------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)

    array0.reset_remaining_balance()
    array0.reset_remaining_balance()
    array0.reset_remaining_balance()

    expected = 3
    number_of_resets = array0.get_number_of_balance_resets()
    print("Expected:", expected)
    print("Actual:  ", number_of_resets)

    if expected == number_of_resets:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    format_string = '    get_number_of_balance_resets( )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1: Make a SolarArrayPanel, produce some electricity.
    #   No balance_resets yet.
    array2 = SolarPanelArray(0.23, 50, 20000)
    sun_energy = 800
    cost_of_energy = 0.271
    # Produce electricity once:
    dollars_saved = array2.produce_electricity(sun_energy, cost_of_energy)
    # Produce electricity again:
    sun_energy = 430
    cost_of_energy = 0.123
    array2.area = 150  # Triple the area
    dollars_saved = array2.produce_electricity(sun_energy, cost_of_energy)

    expected = 0  # No resets yet.
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array2.get_number_of_balance_resets()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # Instance variables should be unchanged except triple area.
    run_test_instance_variables(array2, 0.23, 150, 20000)

    # Test 2: Do a balance_reset.
    array2.reset_remaining_balance()
    expected = 1  # One reset so far.
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array2.get_number_of_balance_resets()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # Instance variables should be unchanged except triple area.
    run_test_instance_variables(array2, 0.23, 150, 20000)

    # Test 2: Do another balance_reset.
    array2.reset_remaining_balance()
    expected = 2  # Two resets so far.
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    remaining_balance = array2.get_number_of_balance_resets()
    print_actual_result_of_test(expected, remaining_balance, test_results)

    print()  # Instance variables should be unchanged except triple area.
    run_test_instance_variables(array2, 0.23, 150, 20000)


def run_test_double_area_array():
    """ Tests the   double_area_array   method of the SolarPanelArray class. """
    print()
    print('-----------------------------------------')
    print('Testing the   double_area_array   method.')
    print('-----------------------------------------')

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)

    new_solar_array = array0.double_area_array()

    # The original solar array should NOT change:
    run_test_instance_variables(array0, 0.15, 50, 10000)

    # The returned solar array should be double the area and cost,
    # per the specification.
    run_test_instance_variables(new_solar_array, 0.15, 100, 20000)

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    # Test 1
    print('\nTest 1:')
    array1 = SolarPanelArray(0.15, 38, 35000)
    print("For the ORIGINAL solar array:")
    run_test_instance_variables(array1, 0.15, 38, 35000)

    returned_array = array1.double_area_array()

    print()
    print("For the RETURNED (doubled) solar array:")
    run_test_instance_variables(returned_array, 0.15, 76, 70000)

    print()
    print("Checking that the ORIGINAL solar array is unchanged:")
    run_test_instance_variables(array1, 0.15, 38, 35000)


def run_test_change_efficiency():
    """ Tests the   change_efficiency   method of the SolarPanelArray class. """
    print()
    print('-----------------------------------------')
    print('Testing the   change_efficiency   method.')
    print('-----------------------------------------')

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)

    array0.change_efficiency(2)

    # The solar array should have its efficiency multiplied by 2, per the spec.
    run_test_instance_variables(array0, 0.30, 50, 10000)

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    # Test 1
    print('\nTest 1:')
    array1 = SolarPanelArray(0.15, 38, 35000)
    print("For the ORIGINAL solar array:")
    run_test_instance_variables(array1, 0.15, 38, 35000)

    array1.change_efficiency(0.234)

    print()
    print("After running the  change_efficiency  method:")
    run_test_instance_variables(array1, 0.15 * 0.234, 38, 35000)

    # Test 2
    array1.change_efficiency(3.0)

    print()
    print("After running the  change_efficiency  method:")
    run_test_instance_variables(array1, 0.15 * 0.234 * 3.0, 38, 35000)


def run_test_get_best_efficiency():
    """ Tests the   get_best_efficiency   method of the SolarPanelArray class. """
    print()
    print('-----------------------------------------')
    print('Testing the   get_best_efficiency   method.')
    print('-----------------------------------------')

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)

    array0.change_efficiency(2.0)  # Efficiency is now 0.30
    array0.change_efficiency(0.1)  # Efficiency is now 0.03
    array0.change_efficiency(8)  # Efficiency is now 0.24

    expected = 0.30  # The biggest efficiency so far is the 0.30 from earlier
    best_efficiency = array0.get_best_efficiency()
    print("Expected:", expected)
    print("Actual:  ", best_efficiency)

    if expected == best_efficiency:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    array0.change_efficiency(2)  # Efficiency is now 0.48, which is best so far

    expected = 0.48  # The biggest efficiency so far is this new 0.48
    best_efficiency = array0.get_best_efficiency()
    print("Expected:", expected)
    print("Actual:  ", best_efficiency)

    if expected == best_efficiency:
        print("  PASSED the above test -- good!", color='blue')
    else:
        print("  *** FAILED the above test. ***", color='red')

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    format_string = '    get_best_efficiency( )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    print('\nTest 1:')
    array1 = SolarPanelArray(0.15, 38, 35000)
    print("For the ORIGINAL solar array:")
    run_test_instance_variables(array1, 0.15, 38, 35000)

    # Test 2: Do a change_efficiency.
    array1.change_efficiency(0.80)
    expected = 0.15  # New efficiency is NOT better, keep with the old
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    best = array1.get_best_efficiency()
    print_actual_result_of_test(expected, best, test_results)

    print()
    print("Instance variables should now be:")
    run_test_instance_variables(array1, 0.12, 38, 35000)

    # Test 4: Do a change_efficiency.
    array1.change_efficiency(2.0)
    expected = .24  # New efficiency is better
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    best = array1.get_best_efficiency()
    print_actual_result_of_test(expected, best, test_results)

    print()
    print("Instance variables should now be:")
    run_test_instance_variables(array1, 0.24, 38, 35000)

    # Test 5: Do a change_efficiency.
    array1.change_efficiency(0.01)
    expected = .24  # New efficiency is NOT better
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    best = array1.get_best_efficiency()
    print_actual_result_of_test(expected, best, test_results)

    print()
    print("Instance variables should now be:")
    run_test_instance_variables(array1, 0.0024, 38, 35000)

    # Test 6: Do a change_efficiency.
    array1.change_efficiency(20.0)
    expected = .24  # New efficiency is NOT better
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    best = array1.get_best_efficiency()
    print_actual_result_of_test(expected, best, test_results)

    print()
    print("Instance variables should now be:")
    run_test_instance_variables(array1, 0.048, 38, 35000)

    # Test 7: Do a change_efficiency.
    array1.change_efficiency(5.0001)
    expected = .2400048  # New efficiency is (slightly) better than any other
    print_expected_result_of_test([], expected, test_results, format_string,
                                  ' for the returned value')
    best = array1.get_best_efficiency()
    print_actual_result_of_test(expected, best, test_results)

    print()
    print("Instance variables should now be:")
    run_test_instance_variables(array1, 0.2400048, 38, 35000)


def run_test_combine_arrays():
    """ Tests the   combine_arrays   method of the SolarPanelArray class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   combine_arrays   method.')
    print('-----------------------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 0 (intended to be easy to read, to help clarify the specification):
    # -------------------------------------------------------------------------
    print()
    print("A simple test to illustrate the specification (READ THE TEST CODE):")
    array0 = SolarPanelArray(0.15, 50, 10000)
    array1 = SolarPanelArray(0.25, 30, 40000)

    new_solar_array = array0.combine_arrays(array1)

    # The original solar arrays should NOT change:
    run_test_instance_variables(array0, 0.15, 50, 10000)
    run_test_instance_variables(array1, 0.25, 30, 40000)

    # The returned solar array should be the smaller of the two efficiencies,
    # and the sum of the areas and costs, per the specification.
    run_test_instance_variables(new_solar_array, 0.15, 80, 50000)

    # -------------------------------------------------------------------------
    # End of Test 0.
    # -------------------------------------------------------------------------

    # Test 1
    print('\nTest 1:')
    array1 = SolarPanelArray(0.32, 70, 42001)
    array2 = SolarPanelArray(0.15, 20, 10000)

    print("For the ORIGINAL first solar array:")
    run_test_instance_variables(array1, 0.32, 70, 42001)

    print()
    print("For the ORIGINAL second solar array:")
    run_test_instance_variables(array2, 0.15, 20, 10000)

    print()
    print("For the returned COMBINED solar array:")
    combined = array1.combine_arrays(array2)
    run_test_instance_variables(combined, 0.15, 90, 52001)

    print()
    print("For the ORIGINAL first solar array after the combining:")
    run_test_instance_variables(array1, 0.32, 70, 42001)

    print("For the ORIGINAL second solar array after the combining:")
    run_test_instance_variables(array2, 0.15, 20, 10000)


###############################################################################
# The following are HELPER functions that display error messages in RED
# and help make it easier for us to write tests.
# Do NOT change any of the following.
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


def run_test_instance_variables(solar_panel_array, expected_efficiency,
                                expected_area, expected_cost,
                                show_not_test=False):
    """
    Tests whether the instance variables for the given SolarArrayPanel
    are per the given expected values.
      -- Prints relevant messages.
      -- Returns True if all is OK, else returns False.
    """
    # noinspection PyBroadException
    try:
        return (run_test_type_of_object(solar_panel_array) and
                run_test_types_of_instance_variables(solar_panel_array) and
                run_test_values_of_instance_variables(
                    solar_panel_array,
                    expected_efficiency,
                    expected_area,
                    expected_cost, show_not_test=False))
    except Exception:
        something_unexpected_happened_in_our_testing_code()
        return False


def run_test_values_of_instance_variables(solar_panel_array,
                                          expected_efficiency,
                                          expected_area,
                                          expected_cost,
                                          show_not_test=False):
    # Print the EXPECTED and ACTUAL values of the instance variables
    format_string = '  {:12} {:>5} {:>9} {:>9}'
    if show_not_test:
        print('   Showing instance variables BEFORE test:')
    else:
        print('  Testing instance variables:')
    print('            efficiency    area    cost')
    print('            ----------    ----    ----')
    if show_not_test:
        print(format_string.format('Before test:',
                                   str(expected_efficiency),
                                   str(expected_area),
                                   str(expected_cost)))
        return
    print(format_string.format('Expected:   ',
                               str(expected_efficiency),
                               str(expected_area),
                               str(expected_cost)))
    print(format_string.format('Actual:', str(solar_panel_array.efficiency),
                               str(solar_panel_array.area),
                               str(solar_panel_array.cost)))

    # Print a message indicating whether or not
    # the EXPECTED values are equal to the ACTUAL values.
    expected = (expected_efficiency, expected_area, expected_cost)
    actual = (solar_panel_array.efficiency, solar_panel_array.area,
              solar_panel_array.cost)
    return print_result_of_test(expected, actual)


def something_unexpected_happened_in_our_testing_code():
    print_failure_message()
    explanation = (
            '  Something unexpected has happened in the testing \n' +
            '  code that we supplied.  You should probably\n' +
            '  SEEK HELP FROM YOUR INSTRUCTOR NOW.')
    print_failure_message(explanation)


def run_test_type_of_object(solar_panel_array):
    """ Returns True if the argument is in fact a SolarPanelArray object """
    if isinstance(solar_panel_array, SolarPanelArray):
        return True
    else:
        explanation = ('  The following object to test:\n' +
                       '     ' + str(solar_panel_array) + '\n' +
                       '  should be a SolarPanelArray object,\n' +
                       '  but it is not.  Perhaps your code\n' +
                       '  returned something of the wrong type?')
        print_failure_message()
        print_failure_message(explanation)
        return False


def run_test_types_of_instance_variables(solar_panel_array):
    """
    Returns True if the argument has the right instance variables
    and they are all numbers.
    """
    # If NONE of the expected instance variables exist,
    # then perhaps the only "problem" is that the  __init__  method
    # has not yet been implemented.
    attributes = dir(solar_panel_array)
    if ('efficiency' not in attributes or 'area' not in attributes
        or 'cost' not in attributes):
        explanation = (
                '  This object:\n' +
                '     ' + str(solar_panel_array) + '\n' +
                '  should have these instance variables:\n' +
                '     self.efficiency\n' +
                '     self.area\n' +
                '     self.cost\n' +
                '  but it has lacks at least one of them.\n' +
                '  Perhaps you simply have not yet\n' +
                '  implemented the   __init__   method?\n' +
                '  (If so, implement it now.)\n' +
                '  Or perhaps you misspelled an instance variable?')
        print_failure_message()
        print_failure_message(explanation)
        return False
    return True


def is_list_of_strings(strings):
    return ((strings == [])
            or (isinstance(strings[0], str)
                and is_list_of_strings(strings[1:])))


def print_result_of_test(expected, actual):
    if are_equal(expected, actual):
        print("  PASSED the above test -- good!", color="blue")
        return True

    print_failure_message()

    # if isinstance(expected, list) or isinstance(expected, tuple):
    #     explanation = (
    #             '  For at least one of the above, its Expected value\n' +
    #             '  does not equal its Actual value.'
    #             'Note: the printed\n' +
    #             '  values are the actual values ROUNDED to 1 decimal place.')
    #     print_failure_message(explanation)

    return False


def are_equal(a, b):
    # We will treat two numbers as being "equal" if they are
    # the same when each is rounded to 12 decimal places.
    if ((isinstance(a, float) or isinstance(a, int))
            and (isinstance(b, float) or isinstance(b, int))):
        return round(a, 12) == round(b, 12)

    # For lists and tuples, their items have to be equal for the
    # lists/tuples to be equal.
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    # For all else, they must be equal in the "usual" way:
    return a == b


def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=0.5):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message, flush=True, color="red")
    time.sleep(flush_time)


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
