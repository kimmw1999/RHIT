"""
A simple   Point   class.
NOTE: This is NOT rosegraphics -- it is your OWN Point class.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Martino Kim.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_init()
    run_test_repr()
    run_test_clone()
    run_test_move_to()
    run_test_move_by()
    run_test_get_number_of_moves_made()
    run_test_get_distance_from()
    run_test_get_distance_from_start()
    run_test_get_distance_traveled()
    run_test_closer_to()
    run_test_halfway_to()

###############################################################################
# IMPORTANT:
#   Your instructor will help you get started on this exercise.
###############################################################################
import math
# -----------------------------------------------------------------------------
# DONE: 2. With your instructor, implement a class called   Point
#   that has NO METHODS (yet); just the lines of code
#   that start the definition of any class:
#   _
#      class NAME_OF_CLASS(object):
#          """ Brief description of what objects of the class 'are'."""
#   _
#   Run the program and correct any syntax (notational) errors.
# -----------------------------------------------------------------------------
class Point(object):
#          """ Brief description of what objects of the class 'are'.
#              Represents a 2D point with x and y values."""
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.total=0
        self.distance=0

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def clone(self):
        """creates a new point(using the values as this point) and return that new point."""
        return Point(self.x, self.y)
    def move_to(self,x,y):
        self.distance= self.distance+ math.sqrt((self.x-x)**2+(self.y-y)**2)
        Point(0, 0)
        if(self.total==0):
            Point.x=self.x
            Point.y=self.y
        self.x=x
        self.y=y

        self.total=self.total+1

    def move_by(self, dx, dy):
        Point(0, 0)
        if (self.total == 0):
            Point.x = self.x
            Point.y = self.y
        self.distance=self.distance+math.sqrt(dx**2+dy**2)

        self.x=self.x+dx
        self.y=self.y+dy
        self.total=self.total+1

    def get_number_of_moves_made(self):
        """"""
        return self.total

    def get_distance_from(self, another_point):
        delta_x=self.x-another_point.x
        delta_y=self.y-another_point.y
        return math.sqrt(delta_x**2+delta_y**2)

    def get_distance_from_start(self):
        return math.sqrt((Point.x-self.x)**2+(Point.y-self.y)**2)

    def get_distance_traveled(self):
        return self.distance

    def closer_to(self, p1, p2):
        if(self.get_distance_from(p1)> self.get_distance_from(p2) ):
            return p2
        else:
            return p1

    def halfway_to(self, p1):

        return Point((self.x+p1.x)/2, (self.y+p1.y)/2)
###############################################################################
# NOTE: For ALL of the methods that you implement, the method is allowed
# to have additional side effects as needed by it and/or other methods.
###############################################################################
def run_test_init():
    """
    Tests the   __init__   method of the Point class.
      -- IMPORTANT:  There are   TWO  underscores on each side.
      -- Note:  the   __init__  method runs when one constructs
         a Point.  See examples below.

    Here is the specification for the   __init__   method:
    What comes in:
       -- self
       -- an integer x
       -- an integer y
       where (x, y) is to be the initial position of this Point.
    What goes out:  Nothing (i.e., None).
    Side effects:  Sets two instance variables named:
           x
           y
       to the given coordinate (i.e., to the given x and y).
       Other methods should modify the instance variables
           x
           y
       as needed so that they always indicate the CURRENT position
       of the Point.

    EXAMPLE: The following shows   __init__   in action.
    You should also use this example to test this method.

        p1 = Point(30, 18)
        print()
        print('Expected for p1: 30 18')
        print('Actual for p1:  ', p1.x, p1.y)

        p2 = Point(100, -40)
        print()
        print('Expected for p2: 100 -40')
        print('Actual for p2:  ', p2.x, p2.y)
        print('Expected for p1: 30 18')
        print('Actual for p1:  ', p1.x, p1.y)

        p1.y = 999
        print()
        print('Expected for p1: 30 999')
        print('Actual for p1:  ', p1.x, p1.y)
        print('Expected for p2: 100 -40')
        print('Actual for p2:  ', p2.x, p2.y)
    """
    # -------------------------------------------------------------------------
    # DONE: 3.  With your instructor, READ and UNDERSTAND the instructions
    #   in this _TODO_, since you will do similarly for each of the methods
    #   that you implement in this exercise.  Then, still with your instructor,
    #   carry out the following instructions to complete this _TODO_.
    #  -
    #   a. Read the above specification of the   __init__   method.
    #        Do NOT proceed until you understand WHAT it should do
    #        (but not necessarily HOW it will do it).
    #        NO CODE YET.  Ask questions as needed.
    #   b. Examine the EXAMPLE code in the doc-string above.
    #        Make sure that you see how that code works, and how it
    #        TESTS the  __init__  method.  ** ASK QUESTIONS AS NEEDED. **
    #   c. SCROLL DOWN past this comment to see the CODE for this TEST function.
    #        It is the same as the EXAMPLE code above, but is COMMENTED-OUT.
    #   d. SELECT (highlight) all that commented-out code, then HOLD
    #        the CTRL key down and press the  /  key  (the same key
    #        that has the ? symbol, toward the bottom-right of keyboard).
    #        This will UN-comment that code.  Try the same key-combination
    #        again to see that it then COMMENTS-OUT the code.  Do the
    #        key-combination once more to end up with the code UN-commented.
    #      _
    #      The tests will not RUN successfully because you have not (yet)
    #        implemented the   __init__   method.
    #      _
    #   e. Below the code that you just UN-commented, add one more test
    #        of your OWN choosing.  It does not have to be a profound test,
    #        but it must at least CALL the method being tested
    #        and then PRINT relevant values: the objects involved
    #        and the returned value, if any.
    #   f. Implement and test the   __init__   method in the Point class,
    #        per the above specification.  Use the  Structure  window
    #        to find where the Point class is.  Make sure that you UNDERSTAND
    #        your code and are not just "pattern matching" from examples.
    #        ASK QUESTIONS AS NEEDED.  COMMIT AND PUSH YOUR WORK.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(30, 18)
    print()
    print('Expected for p1: 30 18')
    print('Actual for p1:  ', p1.x, p1.y)

    p2 = Point(100, -40)
    print()
    print('Expected for p2: 100 -40')
    print('Actual for p2:  ', p2.x, p2.y)
    print('Expected for p1: 30 18')
    print('Actual for p1:  ', p1.x, p1.y)

    p1.y = 999
    print()
    print('Expected for p1: 30 999')
    print('Actual for p1:  ', p1.x, p1.y)
    print('Expected for p2: 100 -40')
    print('Actual for p2:  ', p2.x, p2.y)


def run_test_repr():
    """
    Tests the   __repr__   method of the Point class.
      -- IMPORTANT:  There are   TWO  underscores on each side.
      -- Note:  the   __repr__  method is called by the PRINT
           function and other functions that DISPLAY a Point object.
           See examples below.

    Here is the specification for the   __repr__   method:
    What comes in:
       -- self
    What goes out:
      Returns a string that represents a Point like this:
         'Point(x, y)'
      where   x   and   y   are replaced by this Point's
      x and y coordinates.
    Side effects: None.

    EXAMPLE: The following shows   __repr__   in action.
    You should also use this example to test this method.

        p1 = Point(30, 18)
        print()
        print('Expected for p1: Point(30, 18)')
        print('Actual for p1:  ', p1)

        p2 = Point(100, -40)
        print()
        print('Expected for p2: Point(100, -40)')
        print('Actual for p2:  ', p2)
        print('Expected for p1: Point(30, 18)')
        print('Actual for p1:  ', p1)

        p1.y = 999
        print()
        print('Expected for p1: Point(30, 999)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(100, -40)')
        print('Actual for p2:  ', p2)
    """
    # -------------------------------------------------------------------------
    # DONE: 4.  Follow the same instructions as in _TODO_3 above,
    #           but for the  __repr__  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __repr__   method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(30, 18)
    print()
    print('Expected for p1: Point(30, 18)')
    print('Actual for p1:  ', p1)

    p2 = Point(100, -40)
    print()
    print('Expected for p2: Point(100, -40)')
    print('Actual for p2:  ', p2)
    print('Expected for p1: Point(30, 18)')
    print('Actual for p1:  ', p1)

    p1.y = 999
    print()
    print('Expected for p1: Point(30, 999)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(100, -40)')
    print('Actual for p2:  ', p2)


def run_test_clone():
    """
    Tests the   clone   method of the Point class.  (NO MORE UNDERSCORES!)

    Here is the specification for the   clone   method:
    What comes in:
       -- self
    What goes out:
      Returns a new Point whose x and y coordinates are the same
      as the x and y coordinates of this Point.
    Side effects: None.

    EXAMPLE: The following shows   clone   in action.
    You should also use this example to test this method.

        p1 = Point(10, 8)
        print()
        print('Expected for p1: Point(10, 8)')
        print('Actual for p1:  ', p1)

        p2 = p1.clone()
        p3 = p2.clone()
        print()
        print('Expected for p1: Point(10, 8)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(10, 8)')
        print('Actual for p2:  ', p2)
        print('Expected for p3: Point(10, 8)')
        print('Actual for p3:  ', p3)

        p1.x = 999
        print()
        print('Expected for p1: Point(999, 8)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(10, 8)')
        print('Actual for p2:  ', p2)
        print('Expected for p3: Point(10, 8)')
        print('Actual for p3:  ', p3)

        p1.y = 333
        p2 = Point(11, 22)
        p3.x = 777
        p3.y = 555
        print()
        print('Expected for p1: Point(999. 333)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(11, 22)')
        print('Actual for p2:  ', p2)
        print('Expected for p3: Point(777, 555)')
        print('Actual for p3:  ', p3)
   """
    # -------------------------------------------------------------------------
    # DONE: 5.  Follow the same instructions as in _TODO_3 above,
    #           but for the  clone  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   clone   method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(10, 8)
    print()
    print('Expected for p1: Point(10, 8)')
    print('Actual for p1:  ', p1)

    p2 = p1.clone()
    p3 = p2.clone()
    print()
    print('Expected for p1: Point(10, 8)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(10, 8)')
    print('Actual for p2:  ', p2)
    print('Expected for p3: Point(10, 8)')
    print('Actual for p3:  ', p3)

    p1.x = 999
    print()
    print('Expected for p1: Point(999, 8)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(10, 8)')
    print('Actual for p2:  ', p2)
    print('Expected for p3: Point(10, 8)')
    print('Actual for p3:  ', p3)

    p1.y = 333
    p2 = Point(11, 22)
    p3.x = 777
    p3.y = 555
    print()
    print('Expected for p1: Point(999. 333)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(11, 22)')
    print('Actual for p2:  ', p2)
    print('Expected for p3: Point(777, 555)')
    print('Actual for p3:  ', p3)


def run_test_move_to():
    """
    Tests the   move_to   method of the Point class.

    Here is the specification for the   move_to   method:
    What comes in:
       -- self
       -- an integer x
       -- an integer y
    What goes out:  Nothing (i.e., None).
    Side effects:  Changes the instance variables
          x
          y
       that set the position of this Point to the given x and y.
       This has the effect of "moving" this Point TO the given (x, y).

    EXAMPLE: The following shows   move_to   in action.
    You should also use this example to test this method.

        p1 = Point(10, 8)
        p2 = Point(50, 20)
        print()
        print('Expected for p1: Point(10, 8)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(50, 20)')
        print('Actual for p2:  ', p2)

        p1.move_to(5, -1)
        p2.move_to(0, 0)
        print()
        print('Expected for p1: Point(5, -1)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(0, 0)')
        print('Actual for p2:  ', p2)

        p2.y = 99
        print()
        print('Expected for p1: Point(5, -1)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(0, 99)')
        print('Actual for p2:  ', p2)

        check_has_no_return = p2.move_to(0, 222)
        print()
        print('Expected for p1: Point(5, -1)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(0, 222)')
        print('Actual for p2:  ', p2)
        if check_has_no_return is not None:
            print('** FAILED: This method should NOT return an explicit')
            print('** value; in fact, it returned:', check_has_no_return)
    """
    # -------------------------------------------------------------------------
    # DONE: 6.  Follow the same instructions as in _TODO_3 above,
    #           but for the  move_to  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   move_to   method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(10, 8)
    p2 = Point(50, 20)
    print()
    print('Expected for p1: Point(10, 8)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(50, 20)')
    print('Actual for p2:  ', p2)

    p1.move_to(5, -1)
    p2.move_to(0, 0)
    print()
    print('Expected for p1: Point(5, -1)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(0, 0)')
    print('Actual for p2:  ', p2)

    p2.y = 99
    print()
    print('Expected for p1: Point(5, -1)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(0, 99)')
    print('Actual for p2:  ', p2)

    check_has_no_return = p2.move_to(0, 222)
    print()
    print('Expected for p1: Point(5, -1)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(0, 222)')
    print('Actual for p2:  ', p2)
    if check_has_no_return is not None:
        print('** FAILED: This method should NOT return an explicit')
        print('** value; in fact, it returned:', check_has_no_return)


def run_test_move_by():
    """
    Tests the   move_by   method of the Point class.

    Here is the specification for the   move_by   method:
    What comes in:
       -- self
       -- an integer dx
       -- an integer dy
    What goes out:  Nothing (i.e., None).
    Side effects:  Increments the current values of the instance variables
       that store the position of this Point:
          x
          y
       by the given  dx  and  dy.
       This has the effect of "moving" this Point BY the given (dx, dy).

    EXAMPLE: The following shows   move_by   in action.
    You should also use this example to test this method.

        p1 = Point(10, 8)
        p2 = Point(50, 20)
        print()
        print('Expected for p1: Point(10, 8)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(50, 20)')
        print('Actual for p2:  ', p2)

        p1.move_by(5, -1)
        p2.move_by(0, 0)
        print()
        print('Expected for p1: Point(15, 7)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(50, 20)')
        print('Actual for p2:  ', p2)

        p2.move_by(200, 0)
        print()
        print('Expected for p1: Point(15, 7)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(250, 20)')
        print('Actual for p2:  ', p2)

        check_has_no_return = p2.move_by(-100, 300)
        print()
        print('Expected for p1: Point(15, 7)')
        print('Actual for p1:  ', p1)
        print('Expected for p2: Point(150, 320)')
        print('Actual for p2:  ', p2)
        if check_has_no_return is not None:
            print('** FAILED: This method should NOT return an explicit')
            print('** value; in fact, it returned:', check_has_no_return)
        """
    # -------------------------------------------------------------------------
    # DONE: 7.  Follow the same instructions as in _TODO_3 above,
    #           but for the  move_by  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   move_by   method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(10, 8)
    p2 = Point(50, 20)
    print()
    print('Expected for p1: Point(10, 8)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(50, 20)')
    print('Actual for p2:  ', p2)

    p1.move_by(5, -1)
    p2.move_by(0, 0)
    print()
    print('Expected for p1: Point(15, 7)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(50, 20)')
    print('Actual for p2:  ', p2)

    p2.move_by(200, 0)
    print()
    print('Expected for p1: Point(15, 7)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(250, 20)')
    print('Actual for p2:  ', p2)

    check_has_no_return = p2.move_by(-100, 300)
    print()
    print('Expected for p1: Point(15, 7)')
    print('Actual for p1:  ', p1)
    print('Expected for p2: Point(150, 320)')
    print('Actual for p2:  ', p2)
    if check_has_no_return is not None:
        print('** FAILED: This method should NOT return an explicit')
        print('** value; in fact, it returned:', check_has_no_return)


def run_test_get_number_of_moves_made():
    """
    Tests the   get_number_of_moves_made   method of the Point class.

    Here is the specification for the  get_number_of_moves_made  method:
    What comes in:
       -- self
    What goes out:  Returns an integer that is the number of times that
       this Point has "moved" via calls to   move_to  and/or   move_by.
    Side effects:
       ** You figure out what side effect(s) MUST happen! **

    EXAMPLE: The following shows   get_number_of_moves_made   in action.
    You should also use this example to test this method.

        p1 = Point(10, 8)
        p2 = Point(50, 20)
        print()
        print('Expected for p1 moves made: 0')
        print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
        print('Expected for p2 moves made: 0')
        print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

        p1.move_by(5, -1)
        p2.move_by(0, 0)
        print()
        print('Expected for p1 moves made: 1')
        print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
        print('Expected for p2 moves made: 1')
        print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

        p2.move_by(200, 0)
        p2.move_by(-100, 300)
        p2.move_to(-100, 300)
        p1.move_to(3, 3)
        print()
        print('Expected for p1 moves made: 2')
        print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
        print('Expected for p2 moves made: 4')
        print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

        p1.move_by(200, 0)
        p1.move_by(-100, 300)
        p1.move_to(-100, 300)
        p1.move_to(3, 3)
        print()
        print('Expected for p1 moves made: 6')
        print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
        print('Expected for p2 moves made: 4')
        print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

        p1.x = 400
        print()
        print('Expected for p1 moves made: 6')
        print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
        print('Expected for p2 moves made: 4')
        print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

        p1.move_to(3, 3)
        p2.move_by(0, 0)
        print()
        print('Expected for p1 moves made: 7')
        print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
        print('Expected for p2 moves made: 5')
        print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())
    """
    # -------------------------------------------------------------------------
    # DONE: 8.  Follow the same instructions as in _TODO_3 above,
    #    but for the  get_number_of_moves_made  method specified above.
    #   _
    #    HINT: What must a Point REMEMBER for this method?
    #          How does an object REMEMBER (i.e., STORE) data?
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_number_of_moves_made   method')
    print('of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(10, 8)
    p2 = Point(50, 20)
    print()
    print('Expected for p1 moves made: 0')
    print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
    print('Expected for p2 moves made: 0')
    print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

    p1.move_by(5, -1)
    p2.move_by(0, 0)
    print()
    print('Expected for p1 moves made: 1')
    print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
    print('Expected for p2 moves made: 1')
    print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

    p2.move_by(200, 0)
    p2.move_by(-100, 300)
    p2.move_to(-100, 300)
    p1.move_to(3, 3)
    print()
    print('Expected for p1 moves made: 2')
    print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
    print('Expected for p2 moves made: 4')
    print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

    p1.move_by(200, 0)
    p1.move_by(-100, 300)
    p1.move_to(-100, 300)
    p1.move_to(3, 3)
    print()
    print('Expected for p1 moves made: 6')
    print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
    print('Expected for p2 moves made: 4')
    print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

    p1.x = 400
    print()
    print('Expected for p1 moves made: 6')
    print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
    print('Expected for p2 moves made: 4')
    print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())

    p1.move_to(3, 3)
    p2.move_by(0, 0)
    print()
    print('Expected for p1 moves made: 7')
    print('Actual for p1 moves made:  ', p1.get_number_of_moves_made())
    print('Expected for p2 moves made: 5')
    print('Actual for p2 moves made:  ', p2.get_number_of_moves_made())


def run_test_get_distance_from():
    """
    Tests the   get_distance_from   method of the Point class.

    Here is the specification for the   get_distance_from   method:
    What comes in:
       -- self
       -- another Point object
    What goes out:
       Returns the distance from this Point to the given Point.
    Side effects:
       ** You figure out WHETHER OR NOT side effect(s) MUST happen! **

    EXAMPLE: The following shows   get_distance_from   in action.
    You should also use this example to test this method.

        p1 = Point(1, 5)
        p2 = Point(10, 5)
        p3 = Point(13, 9)

        print()
        print('Expected p1 to p2: 9.0')
        print('Actual   p1 to p2:', p1.get_distance_from(p2))

        print()
        print('Expected p2 to p3: 5.0')
        print('Actual   p2 to p3:', p2.get_distance_from(p3))
        print('Expected p3 to p2: 5.0')
        print('Actual   p3 to p2:', p3.get_distance_from(p2))

        print()
        print('Expected p1 to p3: about 12.65')
        print('Actual   p1 to p3:', p1.get_distance_from(p3))
        print('Expected p3 to p1: about 12.65')
        print('Actual   p3 to p1:', p3.get_distance_from(p1))

        print()
        print('Expected p1 to p1: 0.0')
        print('Actual   p1 to p1:', p1.get_distance_from(p1))
        print('Expected p2 to p2: 0.0')
        print('Actual   p2 to p2:', p2.get_distance_from(p2))
        print('Expected p3 to p3: 0.0')
        print('Actual   p3 to p3:', p3.get_distance_from(p3))

        p4 = p1.clone()
        print()
        print('Expected p1 to p4: 0.0')
        print('Actual   p1 to p4:', p1.get_distance_from(p4))
        print('Expected p4 to p1: 0.0')
        print('Actual   p4 to p1:', p4.get_distance_from(p1))
        print('Expected p4 to p2: 9.0')
        print('Actual   p4 to p2:', p4.get_distance_from(p2))
        print('Expected p2 to p4: 9.0')
        print('Actual   p2 to p4:', p2.get_distance_from(p4))
    """
    # -------------------------------------------------------------------------
    # DONE: 9.  Follow the same instructions as in _TODO_3 above,
    #    but for the  get_distance_from  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the  get_distance_from  method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(1, 5)
    p2 = Point(10, 5)
    p3 = Point(13, 9)

    print()
    print('Expected p1 to p2: 9.0')
    print('Actual   p1 to p2:', p1.get_distance_from(p2))

    print()
    print('Expected p2 to p3: 5.0')
    print('Actual   p2 to p3:', p2.get_distance_from(p3))
    print('Expected p3 to p2: 5.0')
    print('Actual   p3 to p2:', p3.get_distance_from(p2))

    print()
    print('Expected p1 to p3: about 12.65')
    print('Actual   p1 to p3:', p1.get_distance_from(p3))
    print('Expected p3 to p1: about 12.65')
    print('Actual   p3 to p1:', p3.get_distance_from(p1))

    print()
    print('Expected p1 to p1: 0.0')
    print('Actual   p1 to p1:', p1.get_distance_from(p1))
    print('Expected p2 to p2: 0.0')
    print('Actual   p2 to p2:', p2.get_distance_from(p2))
    print('Expected p3 to p3: 0.0')
    print('Actual   p3 to p3:', p3.get_distance_from(p3))

    p4 = p1.clone()
    print()
    print('Expected p1 to p4: 0.0')
    print('Actual   p1 to p4:', p1.get_distance_from(p4))
    print('Expected p4 to p1: 0.0')
    print('Actual   p4 to p1:', p4.get_distance_from(p1))
    print('Expected p4 to p2: 9.0')
    print('Actual   p4 to p2:', p4.get_distance_from(p2))
    print('Expected p2 to p4: 9.0')
    print('Actual   p2 to p4:', p2.get_distance_from(p4))


def run_test_get_distance_from_start():
    """
    Tests the   get_distance_from_start  method of the Point class.

    Here is the specification for the   get_distance_from_start  method:
    What comes in:
       -- self
    What goes out:
       Returns the distance from this Point's current position
       to the position that the Point was at when it was constructed.
    Side effects:
       ** You figure out WHETHER OR NOT side effect(s) MUST happen! **

    EXAMPLE: The following shows   get_distance_from_start   in action.
    You should also use this example to test this method.

        p1 = Point(20, 30)
        p1.move_to(111, 222)
        p1.move_by(10, 20)
        p1.move_to(0, 0)
        p1.move_to(21, 31)
        print()
        print('p1 from start to (21, 31), should be about 1.414')
        print('Actually is:', p1.get_distance_from_start())

        p1.move_by(29, 39)
        print()
        print('p1 from start to (50, 70), should be about 50.0')
        print('Actually is:', p1.get_distance_from_start())

        p2 = Point(1, 1)
        print()
        print('p2 from start to (1, 1), should be about 0.0')
        print('Actually is:', p2.get_distance_from_start())

        p2.move_to(11, 1)
        print()
        print('p2 from start to (11, 1), should be about 10.0')
        print('Actually is:', p2.get_distance_from_start())

        p2.move_to(999, 999)
        p2.move_to(1, 1)
        print()
        print('p2 from start to (1, 1), should be about 0.0')
        print('Actually is:', p2.get_distance_from_start())
    """
    # -------------------------------------------------------------------------
    # DONE: 10.  Follow the same instructions as in _TODO_3 above,
    #    but for the  get_distance_from_start  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_distance_from_start   method')
    print('of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(20, 30)
    p1.move_to(111, 222)
    p1.move_by(10, 20)
    p1.move_to(0, 0)
    p1.move_to(21, 31)
    print()
    print('p1 from start to (21, 31), should be about 1.414')
    print('Actually is:', p1.get_distance_from_start())

    p1.move_by(29, 39)
    print()
    print('p1 from start to (50, 70), should be about 50.0')
    print('Actually is:', p1.get_distance_from_start())

    p2 = Point(1, 1)
    print()
    print('p2 from start to (1, 1), should be about 0.0')
    print('Actually is:', p2.get_distance_from_start())

    p2.move_to(11, 1)
    print()
    print('p2 from start to (11, 1), should be about 10.0')
    print('Actually is:', p2.get_distance_from_start())

    p2.move_to(999, 999)
    p2.move_to(1, 1)
    print()
    print('p2 from start to (1, 1), should be about 0.0')
    print('Actually is:', p2.get_distance_from_start())


def run_test_get_distance_traveled():
    """
    Tests the   get_distance_traveled   method of the Point class.

    Here is the specification for the   get_distance_traveled   method:
    What comes in:
       -- self
    What goes out:  Returns the sum of all the distances that
       this Point has "moved" via calls to   move_to  and/or   move_by.
    Side effects:
       ** You figure out WHETHER OR NOT side effect(s) MUST happen! **

    EXAMPLE: The following shows   get_distance_traveled   in action.
    You should also use this example to test this method.

        p1 = Point(20, 30)
        p1.move_to(21, 30)
        p1.move_to(21, 38)
        print()
        print('Expected p1 has traveled 9.0')
        print('Actual:', p1.get_distance_traveled())

        p1.move_by(1, 1)
        print()
        print('Expected p1 has now traveled about 10.414')
        print('Actual:', p1.get_distance_traveled())

        p2 = Point(0, 0)
        p3 = Point(100, 22)
        p4 = Point(0, 555)
        for k in range(100):
            p2.move_by(0, k + 1)
            p3.move_by(k + 1, 0)
            p4.move_to(k + 1, 555)

        print()
        print('Expected p2 has now traveled', 101 * 50.0)
        print('Actual:', p2.get_distance_traveled())
        print('Expected p3 has now traveled', 101 * 50.0)
        print('Actual:', p3.get_distance_traveled())
        print('Expected p4 has now traveled 100.0')
        print('Actual:', p4.get_distance_traveled())
    """
    # -------------------------------------------------------------------------
    # DONE: 11.  Follow the same instructions as in _TODO_3 above,
    #    but for the  get_distance_traveled  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_distance_traveled   method')
    print('of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(20, 30)
    p1.move_to(21, 30)
    p1.move_to(21, 38)
    print()
    print('Expected p1 has traveled 9.0')
    print('Actual:', p1.get_distance_traveled())

    p1.move_by(1, 1)
    print()
    print('Expected p1 has now traveled about 10.414')
    print('Actual:', p1.get_distance_traveled())

    p2 = Point(0, 0)
    p3 = Point(100, 22)
    p4 = Point(0, 555)
    for k in range(100):
        p2.move_by(0, k + 1)
        p3.move_by(k + 1, 0)
        p4.move_to(k + 1, 555)

    print()
    print('Expected p2 has now traveled', 101 * 50.0)
    print('Actual:', p2.get_distance_traveled())
    print('Expected p3 has now traveled', 101 * 50.0)
    print('Actual:', p3.get_distance_traveled())
    print('Expected p4 has now traveled 100.0')
    print('Actual:', p4.get_distance_traveled())


def run_test_closer_to():
    """
    Tests the   closer_to   method of the Point class.

    Here is the specification for the   closer_to   method:
    What comes in:
       -- self
       -- a Point object p2
       -- a Point object p3
    What goes out:
        Returns whichever of p2 and p3 this Point is closer to.
        (Just to be specific, it should return p2 in the case of a tie.)
    Side effects:
       ** You figure out WHETHER OR NOT side effect(s) MUST happen! **

    EXAMPLE: The following shows   closer_to   in action.
    You should also use this example to test this method.

        p1 = Point(10, 20)
        p2 = Point(15, 20)
        p3 = Point(14, 24)

        print()
        print('Expected:', p2)
        print('Actual:  ', p1.closer_to(p2, p3))
        print('Expected:', p2)
        print('Actual:  ', p1.closer_to(p3, p2))

        print()
        print('Expected:', p1)
        print('Actual:  ', p1.closer_to(p1, p3))
        print('Expected:', p2)
        print('Actual:  ', p2.closer_to(p3, p2))
        print('Expected:', p3)
        print('Actual:  ', p3.closer_to(p3, p3))

        print()
        p4 = p1.clone()
        p5 = p1.clone()
        print('Expected:', p4)
        print('Actual:  ', p1.closer_to(p4, p5))
        print('Expected: True')
        print('Actual:  ', p1.closer_to(p4, p5) is p4)
        print('Expected: False')
        print('Actual:  ', p1.closer_to(p4, p5) is p5)
    """
    # -------------------------------------------------------------------------
    # DONE: 12.  Follow the same instructions as in _TODO_3 above,
    #    but for the  closer_to  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   closer_to   method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(10, 20)
    p2 = Point(15, 20)
    p3 = Point(14, 24)

    print()
    print('Expected:', p2)
    print('Actual:  ', p1.closer_to(p2, p3))
    print('Expected:', p2)
    print('Actual:  ', p1.closer_to(p3, p2))

    print()
    print('Expected:', p1)
    print('Actual:  ', p1.closer_to(p1, p3))
    print('Expected:', p2)
    print('Actual:  ', p2.closer_to(p3, p2))
    print('Expected:', p3)
    print('Actual:  ', p3.closer_to(p3, p3))

    print()
    p4 = p1.clone()
    p5 = p1.clone()
    print('Expected:', p4)
    print('Actual:  ', p1.closer_to(p4, p5))
    print('Expected: True')
    print('Actual:  ', p1.closer_to(p4, p5) is p4)
    print('Expected: False')
    print('Actual:  ', p1.closer_to(p4, p5) is p5)


def run_test_halfway_to():
    """
    Tests the   halfway_to   method of the Point class.

    Here is the specification for the   halfway_to   method:
    What comes in:
       -- self
       -- a Point object p2
    What goes out:
        Returns a new Point that is halfway between this Point and p2.
        That is, the x coordinate of the new Point is the average
        of the x coordinate of this Point and the x coordinate of p2,
        and likewise for the new Point's y coordinate.
    Side effects:
       ** You figure out WHETHER OR NOT side effect(s) MUST happen! **

    EXAMPLE: The following shows   halfway_to   in action.
    You should also use this example to test this method.

        p1 = Point(10, 20)
        p2 = Point(30, 100)

        print()
        print('Should be: Point(20.0, 60.0)')
        print('Actual is:', p1.halfway_to(p2))
        print('Should be: Point(20.0, 60.0)')
        print('Actual is:', p2.halfway_to(p1))

        print()
        print('Should be: Point(10.0, 20.0)')
        print('Actual is:', p1.halfway_to(p1))

        p3 = Point(-10, 20)
        p4 = Point(30, -100)

        print()
        print('Should be: Point(10.0, -40.0)')
        print('Actual is:', p3.halfway_to(p4))
        print('Should be: Point(10.0, -40.0)')
        print('Actual is:', p3.halfway_to(p4))

        print()
        print('Should be: Point(-10.0, 20.0)')
        print('Actual is:', p3.halfway_to(p3))

    """
    # -------------------------------------------------------------------------
    # DONE: 13.  Follow the same instructions as in _TODO_3 above,
    #    but for the  halfway_to  method specified above.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Testing the   halfway_to   method of the Point class.')
    print('-----------------------------------------------------------')

    p1 = Point(10, 20)
    p2 = Point(30, 100)

    print()
    print('Should be: Point(20.0, 60.0)')
    print('Actual is:', p1.halfway_to(p2))
    print('Should be: Point(20.0, 60.0)')
    print('Actual is:', p2.halfway_to(p1))

    print()
    print('Should be: Point(10.0, 20.0)')
    print('Actual is:', p1.halfway_to(p1))

    p3 = Point(-10, 20)
    p4 = Point(30, -100)

    print()
    print('Should be: Point(10.0, -40.0)')
    print('Actual is:', p3.halfway_to(p4))
    print('Should be: Point(10.0, -40.0)')
    print('Actual is:', p3.halfway_to(p4))

    print()
    print('Should be: Point(-10.0, 20.0)')
    print('Actual is:', p3.halfway_to(p3))


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
