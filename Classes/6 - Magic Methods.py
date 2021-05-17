# Magic methods are the methods that have two underscores at the beginning and end of their name,
# and they are called automatically by Python interpreter depending on how we use our objects and classes.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

print(point)
# We get <__main__.Point object at 0x01576820>  --> the name of our module followed by the class name and
# the address of this point object in memory.This is the default implementation of the str magic method in our point object.
