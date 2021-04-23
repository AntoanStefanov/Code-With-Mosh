class Point:
    def __init__(self, x, y):
        self.x = x  # we can set it to default value like zero or the recieved x argument
        self.y = y

    def draw(self):  # We have the self parameter here, using this we have a reference to the current point object
        # and with that we can read the x and y values and print them on the terminal
        print(f'x: {self.x} y: {self.y}')
        # Using self we can read attributes of the current point object or we can also call other method in this object.



# when we create a point object, we want to supply initial values for x and y coordinates.
point = Point(1, 2)
# Like 1 and 2. For that we need a constructor, which is a special method that is called when we create a new point object.
# So,in our point class we define a new function-the name of this function should be double underline init double underline.
# This is a special method that we call a magic method. In Python classes we have several magic methods.
# This magic method is called a constructor, it's executed when we create a new point object. Earlier I told you,
# that all the methods we define in a class should have ATLEAST ONE PARAMETER which we call self by convetion.
# We add self and then optionally we add any additional parameteres for initializing our point object.
# Now what is this self. Self is a reference to a current point object, for example here on line 9.
# When you call the point class, python will internally create the point object in memory, and set self
# # to reference that point object, now this point object has a bunch of methods that you've seen before.
# For example when you use the dot operator, you can see all the methods in this point object, but an object can also have
# attributes, which are basically variables that include data about that object, we can have attributes like x and y,
# that we can easily print on terminal. In other words, class or an object bundles data and functions related to that data
# into one unit. Metaphor, think of a human. The human can have attributes like eye color, height, weight and so on,
# as well as function like walk talk and so on.
# Back to constructor, you learned that SELF IS A REFERENCE TO THE CURRENT OBJECT. So we can use that to set the x and y
# attributes, like this.

# Now with point.we have the two new attributes
print(point.x)
print(point.y)

point.draw() # When calling draw method we didn't have to supply a value for the self parameter, bcs python does that
# by default. Now technically we can pass this point object as a reference to the current point object - point.draw(point)
# But this is unnecessary and makes our code easy or noisy.
# Take away:
# THE METHODS WE DEFINE IN A CLASS SHOULD HAVE ATLEAST ONE PARAMETER BY CONVETION called SELF.
# SELF REFERENCES THE CURRENT OBJECT we re working with.
# WHEN CALLING METHODS WE NEVER HAVE TO SUPPLY A VALUE FOR THIS PARAMETER, PYTHON INTERPRETER DOES THAT FOR US
