# Magic methods are the methods that have two underscores at the beginning and end of their name,
# and they are called automatically by Python interpreter depending on how we use our objects and classes.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define str method
    def __str__(self):  # one parameter self
        # we should simply return a string representation of this point object
        return f'({self.x}, {self.y})'

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
point.draw()

# For example here (line 6) we have this init magic method, we don't directly call it, it's called automatically by
# Python interpreter when we create a new Point object.

# We have quite a few magic methods in Python, over the next few lectures you're going to learn about the keys ones.
# If you wanna see the complete list google: python 3 magic methods.


# __str__ magic method

# if we print point object(14 line)

# print(point) # with no str reimplementation
# We get <__main__.Point object at 0x01576820>  --> the name of our module followed by the class name and
# the address of this point object in memory.This is the default implementation of the str magic method in our point object.

# If we write point. you can see all the magic methods that are available in our point object.
# We didn't explicitly create these methods, our point object inherited them from another object. This is what we call
# INHERITANCE - coming soon.

# Now in this list you can see we have this str method

# point.__str__ # By default this returns the name of our module followed by the class name and
# the address of this point object in memory

# Now, let's reimplement this method to get a better result. # Back to our class.

print(point)  # we get (1, 2)
# this is very useful, we get the same result

# We get the same result if we also try to convert a point object to a string using the str function.

print(str(point))
