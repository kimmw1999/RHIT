"""
Exam 3, problem 1.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
from numbers import Number
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
    print()

    run_test_init()
    run_test_get_total_cost()
    run_test_clone()
    run_test_travel()
    run_test_puncture_tires()
    run_test_new_tires()


###############################################################################
# The   Tire   class (and its methods) begins here.
# Students: You may not modify the Tire class.  It is finished for you.
#           You will be writing the Bicycle class that uses the Tire class.
###############################################################################
class Tire(object):
    """ Represents a single tire that might go on the front or rear of a Bicycle. """

    def __init__(self, size, pressure, cost):
        """
        What comes in:
          -- self and three non-negative numbers.
        Note: Units don't matter, but the units would be inches, psi, and dollars
        What goes out: Nothing (i.e., None).
        Side effects:
           Sets instance variables to the given arguments, naming them:
             -- self.size
             -- self.pressure
             -- self.cost
           Also, initializes variables called mileage, num_flats, original_pressure,
             num_clones (students, you probably only care about mileage of those).
        Example:
               t1 = Tire(21, 55.0, 15.99)
          should create instance variables that could be printed like this:
               print(t1.size, t1.pressure, t1.cost, t1.mileage)
        Type hints:
          :type size: int
          :type pressure: float
          :type cost: float
        """
        self.size = size
        self.pressure = pressure
        self.original_pressure = pressure
        self.cost = cost
        self.mileage = 0
        self.num_flats = 0
        self.num_clones = 0

    def __repr__(self):
        """ Returns a string that represents a Tire. """
        return "Tire({}, {}, {})".format(self.size, self.pressure, self.cost)

    def clone(self):
        """
        What comes in:
          -- self
        What goes out:
          -- creates a new tire that has the same size and cost of this tire.  The pressure of the tire is set
             to the original pressure of the tire.
        Side effects: none
        Example:
               t1 = Tire(21, 55.0, 15.99)
               t2 = t1.clone()
               t1.puncture()  # sets the pressure of t1 to zero
               t3 = t1.clone()  # creates a clone of t1, but with the original pressure
               print(t1.size, t2.size, t3.size)
            would print 21 21 21
               print(t1.pressure, t2.pressure, t3.pressure)
            would print 0 55.0 55.0   Notice that t3 has the original tire pressure not 0!
               print(t1.cost, t2.cost, t3.cost)
            would print 15.99 15.99 15.99

        """
        self.num_clones = self.num_clones + 1  # Note, this can be use to know for sure you used this method
        return Tire(self.size, self.original_pressure, self.cost)

    def travel(self, miles):
        """
        What comes in:
          -- self and a non-negative number.
        What goes out: Nothing (i.e., None).
        Side effects:
           MUTATES the mileage based on the number of miles traveled.
           Note, this method  would  allow the tire to travel even if it is flat (0 pressure)
        Example:
               t1 = Tire(21, 55.0, 15.99)
               t1.travel(40)
               t1.travel(15)
               print(t1.mileage)
          would print 55.
        Type hints:
          :type miles: float
        """
        self.mileage = self.mileage + miles
        
    def puncture(self):
        """
        What comes in:
          -- self.
        What goes out: Nothing (i.e., None).
        Side effects:
           MUTATES the num_flats (increasing it by 1) and sets
            the pressure of this tire to 0.
        Example:
               t1 = Tire(21, 55.0, 15.99)
               t1.puncture()
               print(t1.pressure, t1.num_flats)
          would print 0, 1.
        """
        self.num_flats = self.num_flats + 1  # Note, this can be use to know for sure you used this method
        self.pressure = 0


###############################################################################
# The   Bicycle   class (and its methods) begins here.
###############################################################################
class Bicycle(object):
    """ Represents a Bicycle. """
    front_tire: Tire  # Note, these type hints will help PyCharm with auto-completes for these properties
    rear_tire: Tire   # but they don't otherwise effect your code.

    def __init__(self, size, front_tire, rear_tire, frame_cost):
        """
        What comes in:
          -- self
          -- a non-negative number for the bicycle size
              (i.e. what size tires this bicycle must use)
          -- two Tires (see Tire class above)
          -- a non-negative number for the bicycle's cost, which does   *not*
              include the cost of the two tires (i.e. just the cost of the frame).
        What goes out: Nothing (i.e., None).
        Side effects:
           Sets instance variables to the given arguments (or None, see comments
             below), naming them:
             -- self.size
             -- self.front_tire 
             -- self.rear_tire
             -- self.frame_cost
           Also, initializes other instance variables as needed by other Bicycle methods.
           Note: A bicycle of size 17 can only use tires that are size 17.  If
            a new bicycle is made and given a tire size that does not match the
            bike size then the instance variable for that tire should become None.
           Additional comment: Do *not* make clones of bike tires, just use the ones given.
        Example:
               t1 = Tire(21, 55.0, 15.99)
               t2 = Tire(21, 58.5, 15.99)
               b = Bicycle(21, t1, t2, 65.50)
          should create instance variables that could be printed like this:
               print(b.front_tire.size, b.front_tire.pressure, b.front_tire.cost,
                     b.front_tire.mileage, b.front_tire.num_flats)
               print(b.rear_tire.size, b.rear_tire.pressure, b.rear_tire.cost,
                     b.rear_tire.mileage, b.rear_tire.num_flats)
               print(b.size, b.frame_cost)
          In this example  front_tire and rear_tire are set to t1 and t2

        Another example:
               t1 = Tire(8, 25.0, 5.99)  # Notice the different tire size value!
               t2 = Tire(21, 58.5, 15.99)
               b = Bicycle(21, t1, t2, 65.50)
          In this example  front_tire is set to None since you can't (well shouldn't)
             put an 8 inch Tire onto a Bicycle made for 21 inch tires.  So in this
             example front_tire is set to None, but rear_tire is set to t2.
        Type hints:
          :type size:   int
          :type front_tire: Tire
          :type rear_tire: Tire
          :type frame_cost:   float
        """
        # ---------------------------------------------------------------------
        # DONE: 2. READ the above specification (including its example), then
        #  implement and test this method.  Tests are already written (below).
        #  ** ASK QUESTIONS ** if you do not understand the specification.
        # ---------------------------------------------------------------------
        self.size = size
        self.front_tire= front_tire
        self.rear_tire= rear_tire
        self.frame_cost= frame_cost
        if front_tire.size != size:
            self.front_tire= None
        if rear_tire.size != size:
            self. rear_tire= None
        self.mileage=0
    def get_total_cost(self):
        """
        What comes in
          -- self
        What goes out: Returns the total cost of the Bicycle
          (i.e. the cost of the frame plus the cost of each tire).
        Side effects: none
        Example:
               t1 = Tire(21, 55.0, 16.00)
               t2 = Tire(21, 58.5, 16.00)
               b = Bicycle(21, t1, t2, 65.50)
               cost = b.get_total_cost()
               print(cost)
            would print 97.50
        Type hints:
          :rtype: float
        """
        # ---------------------------------------------------------------------
        # DONE: 3. READ the above specification (including its example), then
        #  implement and test this method.  Tests are already written (below).
        #  ** ASK QUESTIONS ** if you do not understand the specification.
        # ---------------------------------------------------------------------
        return self.frame_cost+ self.front_tire.cost+ self.rear_tire.cost
    def clone(self):
        """
        What comes in:
          -- self
        What goes out:
          -- returns a new Bicycle that has two new Tires that are clones of the old tires.
              same size bicycle, and same frame cost.
        Side effects: none
        Example:
               t1 = Tire(21, 55.0, 15.99)
               t2 = Tire(21, 58.5, 15.99)
               b = Bicycle(21, t1, t2, 65.50)
               b2 = b.clone()
        """
        # ---------------------------------------------------------------------
        # DONE: 4. READ the above specification (including its example), then
        #  implement and test this method.  Tests are already written (below).
        #  ** ASK QUESTIONS ** if you do not understand the specification.
        # ---------------------------------------------------------------------
        new_front=self.front_tire.clone()
        new_rear=self.rear_tire.clone()
        return Bicycle(self.size, new_front, new_rear, self.frame_cost)
    def travel(self, miles):
        """
        What comes in:
          -- self and a non-negative number.
        What goes out:
          -- the    total    number of miles that the   bicycle frame   has traveled.
          Note: this might be different from either Tire
        Side effects:
           Uses the Tire travel method to MUTATES the mileage of each Tire.
           MUTATES the total mileage of the bicycle frame
           Note: A bicycle frame has a mileage tracker and both tires have
                 their own mileage trackers (in their own class).
        Note for later:
           Once your bicycle can potentially have flat tires you must check
           that your bicycle can only travel when both tires have some tire
           pressure that is greater than zero.  If either tire is flat then
           the bicycle can't travel at all.
        Example:
               t1 = Tire(21, 55.0, 15.99)
               t1.travel(40)  # A used tire at this point
               t2 = Tire(21, 58.5, 15.99)  # A new tire
               b = Bicycle(21, t1, t2, 65.50)
               bike_frame_milage1 = b.travel(35)
               bike_frame_milage2 = b.travel(35)
               bike_frame_milage3 = b.travel(0)
               print(bike_frame_milage1, bike_frame_milage2, bike_frame_milage3)
          would print 35 70 70, and:
               print(b.front_tire.mileage, b.rear_tire.mileage)
          would print 110 70, since t1 was used for 40 miles before being on the bicycle named b.
        Another example:
               t1 = Tire(21, 55.0, 15.99)
               t2 = Tire(21, 58.5, 15.99)
               b = Bicycle(21, t1, t2, 65.50)
               bike_frame_milage1 = b.travel(40)
               b.rear_tire = Tire(21, 58.5, 15.99) # A new tire was placed on the rear.
               bike_frame_milage2 = b.travel(50)
               print(bike_frame_milage1, bike_frame_milage2)
          would print 40 90
               print(b.front_tire.mileage, b.rear_tire.mileage)
          would print 90 50, since the rear_tire was replaced by a new tire after 40 miles. BTW:
               print(t1.mileage, t2.mileage)
          would print 90 40, since the front tire was t1 for the whole 90 miles, but t2 was only
          the rear tire of the bike for the first 40 miles.

        A later example (once you have implemented the puncture_tires method).
               t1 = Tire(21, 55.0, 15.99)
               t2 = Tire(21, 58.5, 15.99)
               b = Bicycle(21, t1, t2, 65.50)
               bike_frame_milage1 = b.travel(40)
               b.puncture_tires()
               bike_frame_milage2 = b.travel(50)
               print(bike_frame_milage1, bike_frame_milage2)
          would print 40 40
               print(b.front_tire.mileage, b.rear_tire.mileage)
          would print 40 40
               print(t1.mileage, t2.mileage)
          would print 40 40
          since the tires were flat, the second travel did not happen.
        Type hints:
          :type miles: float
        """
        # ---------------------------------------------------------------------
        # DONE: 5. READ the above specification (including its example), then
        #  implement and test this method.  Tests are already written (below).
        #  ** ASK QUESTIONS ** if you do not understand the specification.
        # ---------------------------------------------------------------------
        if self.front_tire.pressure > 0:
            if self.rear_tire.pressure >0:
                self.mileage= self.mileage+miles
                self.front_tire.mileage= self.front_tire.mileage+ miles
                self.rear_tire.mileage= self.rear_tire.mileage+miles
        return self.mileage
    def puncture_tires(self):
        """
        What comes in
          -- self
        What goes out: Nothing (i.e. None)
        Side effects:

        Example:
          t1 = Tire(21, 55.0, 15.99)
          t2 = Tire(21, 58.5, 15.99)
          b = Bicycle(21, t1, t2, 65.50)
          b.puncture_tires()
          print(b.front_tire.pressure, b.rear_tire.pressure)
        would print 0, 0.
        """
        # ---------------------------------------------------------------------
        # DONE: 6. READ the above specification (including its example), then
        #  implement and test this method.  Tests are already written (below).
        #  ** ASK QUESTIONS ** if you do not understand the specification.
        # ---------------------------------------------------------------------
        self.front_tire.pressure=0
        self.rear_tire.pressure=0
    def new_tires(self):
        """
        What comes in:  self.
        What goes out:
          MUTATES this bike to give it 2 new tires (clones of the old tires).
          -- the front_tire is set to a clone of the old front_tire
          -- the rear_tire is set to a clone of the old rear_tire
        Side effects:  None.
        Example:
           t1 = Tire(21, 55.0, 15.99)
           t2 = Tire(21, 58.5, 15.99)
           b = Bicycle(21, t1, t2, 65.50)
           bike_frame_milage1 = b.travel(40)
           b.puncture_tires()
           b.new_tires()
           bike_frame_milage2 = b.travel(50)
           print(bike_frame_milage1, bike_frame_milage2)
          would print 40 90, as you might expect
               print(b.front_tire.mileage, b.rear_tire.mileage)
          would print 50 50, since the tires were replaced by new tires after 40 miles.
               print(t1.mileage, t2.mileage)
          btw would print 40 40, since they were only on the bike for the first 40 miles.
        """
        # ---------------------------------------------------------------------
        # DONE: 7. READ the above specification (including its example), then
        #  implement and test this method.  Tests are already written (below).
        #  ** ASK QUESTIONS ** if you do not understand the specification.
        # ---------------------------------------------------------------------
        self.front_tire= self.front_tire.clone()
        self.rear_tire= self.rear_tire.clone()

###############################################################################
# The TEST functions for the  Bicycle  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the Bicycle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Bicycle class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    t1 = Tire(21, 55.0, 15.99)
    t2 = Tire(21, 58.5, 15.99)
    b = Bicycle(21, t1, t2, 65.50)
    run_test_instance_variables(b, 21, t1, t2, 65.50)

    # Test 2
    print('\nTest 2:')
    t1 = Tire(21, 55.0, 15.99)
    t2 = Tire(22, 58.5, 15.99)
    b = Bicycle(21, t1, t2, 65.50)
    run_test_instance_variables(b, 21, t1, None, 65.50)


def run_test_get_total_cost():
    """ Tests the   get_total_cost()   method of the Bicycle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_total_cost   method of the Bicycle class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    t1 = Tire(21, 55.0, 16.00)
    t2 = Tire(21, 58.5, 16.00)
    b = Bicycle(21, t1, t2, 65.50)
    actual_cost = b.get_total_cost()
    expected_cost = 97.50
    print('Expected cost:', expected_cost)
    print('Actual:       ', actual_cost)
    print_result_of_test(expected_cost, actual_cost)

    # Test 2
    print('\nTest 2:')
    t1.cost = t1.cost + 5
    actual_cost = b.get_total_cost()
    expected_cost = 97.50 + 5  # Tire +5 so total +5
    print('Expected cost:', expected_cost)
    print('Actual:       ', actual_cost)
    print_result_of_test(expected_cost, actual_cost)

    # Test 3
    print('\nTest 3:')
    b.rear_tire.cost = b.rear_tire.cost + 3
    actual_cost = b.get_total_cost()
    expected_cost = 97.50 + 5 + 3 # Both tires cost more
    print('Expected cost:', expected_cost)
    print('Actual:       ', actual_cost)
    print_result_of_test(expected_cost, actual_cost)

    # Test 4
    print('\nTest 4:')
    b.rear_tire = Tire(21, 55.0, 1.00)
    actual_cost = b.get_total_cost() # Change a tire
    expected_cost = 65.50 + 16.00 + 5 + 1.00
    print('Expected cost:', expected_cost)
    print('Actual:       ', actual_cost)
    print_result_of_test(expected_cost, actual_cost)

    # Test 5
    print('\nTest 5:')
    b.frame_cost = b.frame_cost + 2 # More expensive frame
    actual_cost = b.get_total_cost()
    expected_cost = 65.50 + 16.00 + 5 + 1.00 + 2
    print('Expected cost:', expected_cost)
    print('Actual:       ', actual_cost)
    print_result_of_test(expected_cost, actual_cost)


def run_test_clone():
    """ Tests the   clone()   method of the Bicycle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   clone   method of the Bicycle class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    t1 = Tire(21, 55.0, 15.99)
    t2 = Tire(21, 58.5, 15.99)
    b = Bicycle(21, t1, t2, 65.50)
    t1.puncture() # Make the front tire flat of the original bicycle
    t1.cost = 5
    b2 = b.clone()
    t3 = b2.front_tire  # Doesn't seem like a valid way to test, so done manually below
    t4 = b2.rear_tire
    run_test_instance_variables(b, 21, t1, t2, 65.50)
    run_test_instance_variables(b2, 21, t3, t4, 65.50)

    print('Expected pressure:', 0.0)
    print('Actual:           ', t1.pressure)
    print_result_of_test(0.0, t1.pressure)
    print('Expected pressure:', 58.5)
    print('Actual:           ', t2.pressure)
    print_result_of_test(58.5, t2.pressure)
    print('Expected pressure:', 55.0)
    print('Actual:           ', t3.pressure)
    print_result_of_test(55.0, t3.pressure)
    print('Expected pressure:', 58.5)
    print('Actual:           ', t4.pressure)
    print_result_of_test(58.5, t4.pressure)

    print_result_of_test(5, t1.cost)
    print_result_of_test(15.99, t2.cost)
    print_result_of_test(5, t3.cost)
    print_result_of_test(15.99, t4.cost)

    print_result_of_test(1, t1.num_clones)
    print_result_of_test(1, t2.num_clones)
    print_result_of_test(0, t3.num_clones)
    print_result_of_test(0, t4.num_clones)

    print_result_of_test(1, t1.num_flats)
    print_result_of_test(0, t2.num_flats)
    print_result_of_test(0, t3.num_flats)
    print_result_of_test(0, t4.num_flats)

    # Test 2
    print('\nTest 2:')
    t1 = Tire(21, 55.0, 15.99)


def run_test_travel():
    """ Tests the   travel()   method of the Bicycle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   travel   method of the Bicycle class.')
    print('-----------------------------------------------------------')

    # Tests 1 and more:
    print('\nTest 1:')
    t1 = Tire(21, 55.0, 15.99)
    t1.travel(40)  # A used tire at this point
    t2 = Tire(21, 58.5, 15.99)  # A new tire
    b = Bicycle(21, t1, t2, 65.50)
    bike_frame_mileage1 = b.travel(35)
    bike_frame_mileage2 = b.travel(35)
    bike_frame_mileage3 = b.travel(0)

    print_result_of_test(35, bike_frame_mileage1)
    print_result_of_test(70, bike_frame_mileage2)
    print_result_of_test(70, bike_frame_mileage3)

    print_result_of_test(110, b.front_tire.mileage)
    print_result_of_test(70, b.rear_tire.mileage)


def run_test_puncture_tires():
    """ Tests the   puncture_tires()   method of the Bicycle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   puncture_tires   method of the Bicycle class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    t1 = Tire(21, 55.0, 15.99)
    t2 = Tire(21, 58.5, 15.99)
    b = Bicycle(21, t1, t2, 65.50)

    print("b.front_tire.pressure:", b.front_tire.pressure)
    print("b.rear_tire.pressure: ", b.rear_tire.pressure)

    print_result_of_test(55, b.front_tire.pressure)
    print_result_of_test(58.5, b.rear_tire.pressure)

    b.puncture_tires()
    print("b.front_tire.pressure:", b.front_tire.pressure)
    print("b.rear_tire.pressure: ", b.rear_tire.pressure)
    print_result_of_test(0, b.front_tire.pressure)
    print_result_of_test(0, b.rear_tire.pressure)


def run_test_new_tires():
    """ Tests the   new_tires()   method of the Bicycle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   new_tires   method of the Bicycle class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')

    t1 = Tire(21, 55.0, 15.99)
    t2 = Tire(21, 58.5, 15.99)
    b = Bicycle(21, t1, t2, 65.50)
    bike_frame_mileage1 = b.travel(40)
    b.puncture_tires()
    b.new_tires()
    bike_frame_mileage2 = b.travel(50)

    print("bike_frame_mileage1:", bike_frame_mileage1)
    print("bike_frame_mileage2:", bike_frame_mileage2)
    print_result_of_test(40, bike_frame_mileage1)
    print_result_of_test(90, bike_frame_mileage2)

    print("b.front_tire.mileage:", b.front_tire.mileage)
    print("b.rear_tire.mileage: ", b.rear_tire.mileage)
    print_result_of_test(50, b.front_tire.mileage)
    print_result_of_test(50, b.rear_tire.mileage)

    print("t1.mileage:", t1.mileage)
    print("t2.mileage:", t2.mileage)
    print_result_of_test(40, t1.mileage)
    print_result_of_test(40, t2.mileage)


###############################################################################
# The following are HELPER functions that display error messages in RED
# and help make it easier for us to write tests.
# Do NOT change any of the following.
###############################################################################
def run_test_instance_variables(bicycle, expected_size, expected_front_tire,
                                expected_rear_tire, expected_frame_cost):
    """
    Tests whether the instance variables for the given Bicycle
    are per the given expected values.
      -- Prints relevant messages.
      -- Returns True if all is OK, else returns False.
    """
    try:
        return (run_test_type_of_object(bicycle) and
                run_test_types_of_instance_variables(bicycle) and
                run_test_values_of_instance_variables(
                    bicycle,
                    expected_size,
                    expected_front_tire,
                    expected_rear_tire,
                    expected_frame_cost))
    except Exception:
        something_unexpected_happened_in_our_testing_code()
        return False


def run_test_values_of_instance_variables(bicycle, expected_size,
                                          expected_front_tire,
                                          expected_rear_tire,
                                          expected_frame_cost):
    # Print the EXPECTED and ACTUAL values of the instance variables
    format_string = '{:7} {:>4} {:>21} {:>21} {:>8}'
    print('  Testing instance variables:')
    print('          size       front_tire            rear_tire        frame_cost')
    print('          ---- --------------------- ---------------------  ----------')
    print(format_string.format('Expected:',
                               str(expected_size),
                               str(expected_front_tire),
                               str(expected_rear_tire),
                               str(expected_frame_cost)))
    print(format_string.format('Actual:  ',
                               str(bicycle.size),
                               str(bicycle.front_tire),
                               str(bicycle.rear_tire),
                               str(bicycle.frame_cost)))

    # Print a message indicating whether or not
    # the EXPECTED values are equal to the ACTUAL values.
    expected = (expected_size, expected_front_tire, expected_rear_tire, expected_frame_cost)
    actual = (bicycle.size, bicycle.front_tire, bicycle.rear_tire, bicycle.frame_cost)
    return print_result_of_test(expected, actual)


def something_unexpected_happened_in_our_testing_code():
    print_failure_message()
    explanation = (
            '  Something unexpected has happened in the testing \n' +
            '  code that we supplied.  You should probably\n' +
            '  SEEK HELP FROM YOUR INSTRUCTOR NOW.')
    print_failure_message(explanation)


def run_test_type_of_object(bicycle):
    """ Returns True if the argument is in fact a Bicycle object """
    if isinstance(bicycle, Bicycle):
        return True
    else:
        explanation = ('  The following object to test:\n' +
                       '     ' + str(bicycle) + '\n' +
                       '  should be a Bicycle object,\n' +
                       '  but it is not.  Perhaps your code\n' +
                       '  returned something of the wrong type?')
        print_failure_message()
        print_failure_message(explanation)
        return False


def run_test_types_of_instance_variables(bicycle):
    """
    Returns True if the argument has the right instance variables.
    # and they are all numbers.
    """
    # If NONE of the expected instance variables exist,
    # then perhaps the only "problem" is that the  __init__  method
    # has not yet been implemented.
    attributes = dir(bicycle)
    if ('size' not in attributes
            or 'front_tire' not in attributes
            or 'rear_tire' not in attributes
            or 'frame_cost' not in attributes):
        explanation = (
                '  This object:\n' +
                '     ' + str(bicycle) + '\n' +
                '  should have these instance variables:\n' +
                '     self.size\n' +
                '     self.front_tire\n' +
                '     self.rear_tire\n' +
                '     self.frame_cost\n' +
                '  but it does not have them all as expected.\n' +
                '  Perhaps you simply have not yet\n' +
                '  implemented the   __init__   method?\n' +
                '  (If so, implement it now.)')
        print_failure_message()
        print_failure_message(explanation)
        return False

    # If SOME (but not all) of the expected instance variables exist,
    # then perhaps something was misspelled in __init__.
    # if not ('front_tire' in attributes
    #         and 'amount' in attributes):
    #     explanation = (
    #             '  This object:\n' +
    #             '     ' + str(bicycle) + '\n' +
    #             '  should have these instance variables:\n' +
    #             '     self.front_tire\n' +
    #             '     self.amount\n' +
    #             '  but it is missing some of them.\n' +
    #             '  Perhaps you misspelled something\n' +
    #             '  in your   __init__   code?')
    #     print_failure_message()
    #     print_failure_message(explanation)
    #     return False

    # Check that the instance variables are of the right types:
    #     if not isinstance(cloud.front_tire, str):
    #         explanation = (
    #             '  This object:\n' +
    #             '     ' + str(cloud) + '\n' +
    #             '  has an instance variable  front_tire  with this value:\n' +
    #             '     front_tire: ' + str(cloud.front_tire) +
    #             '  That value should be a STRING, but is isn\'t.\n')
    #         print_failure_message()
    #         print_failure_message(explanation)
    #         return False
    #
    #     if not isinstance(cloud.water, list):
    #         explanation = (
    #             '  This object:\n' +
    #             '     ' + str(cloud) + '\n' +
    #             '  has an instance variable  water  with this value:\n' +
    #             '     water: ' + str(cloud.water) +
    #             '  That value should be a LIST, but is isn\'t.\n')
    #         print_failure_message()
    #         print_failure_message(explanation)
    #         return False
    #
    #     if not is_list_of_strings(cloud.water):
    #         explanation = (
    #             '  This object:\n' +
    #             '     ' + str(cloud) + '\n' +
    #             '  has an instance variable  water  with this value:\n' +
    #             '     water: ' + str(cloud.water) +
    #             '  That value should be a list of STRINGS, but is isn\'t.\n')
    #         print_failure_message()
    #         print_failure_message(explanation)
    #         return False

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

    if isinstance(expected, list) or isinstance(expected, tuple):
        explanation = (
                '  For at least one of the above, its Expected value\n' +
                '  does not equal its Actual value.')
        #          Note: the printed\n' +
        #             '  values are the actual values ROUNDED to 1 decimal place.')
        print_failure_message(explanation)

    return False


def are_equal(a, b):
    # We will treat two numbers as being "equal" if they are
    # the same when each is rounded to 12 decimal places.
    if isinstance(a, Number) and isinstance(b, Number):
        return (round(a, 12) == round(b, 12))

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
