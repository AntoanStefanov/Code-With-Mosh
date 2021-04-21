# Let's see how to create point class in Python.
# Start with keyword class, give our class a name, like Point.
# Note that here I'm using pascal naming convention, which is different from the naming convetion
# that we use for naming our variables and functions.
# To name our variables and functions we use all lowercase letters and underscore for seperation.
# But to name our classes we use a different convention which is called Pascal naming convention.
# Basically it says that the first letter of every word should be uppercase, and we shouldn't use underscore for separation.

# MyPoint , MyClassCalledPoint etc.


class Point:  # colon to indicate a block. In this block we define all the functions related to points
    # For example: we can define functions for drawing a point or moving a point to a new location
    # or getting the distance from point x to point y.
    # Example:
    # ALL FUNCTIONS IN OUR CLASSES SHOULD HAVE ATLEAST ONE PARAMETER by convetion we call that parameter self.
    def draw(self):  # we define function called draw.
        print('Draw')
    # Now we have a class or a blueprint for creating Point objects, every Point object that we create
    # will have this draw method


point = Point()
# To create a point object we call this class like a function, now this return a point object
# that we can assign to a variable like point.
# point.
# So if we use the dot operator, you can see we have the draw method as well as a bunch of
# other methods that we didn't define, but our point object got these methods from 

