# In the last lecture, we defined two attributes for our point objects in the constructor in the point class.


class Point:
    # for simplicity I am using string instead of color objects.
    default_color = 'red'  # Class attribute
    # Now we have a class level attribute, and we can read these via a class reference or an object reference. line 29

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


# Now whenever we create a Point object, this Point object will have these attributes by default.
# We can also define an attribute after we create a point object, so here we can set - point.z = 10
point = Point(1, 2)
# point.z = 10  # beacuse objects in Python are dynamic. Similar to JavaScript, so we don't have to define all the attributes
# in the constructor, we can define them later, whenever we need them.


# IMPORTANT TO UNDERSTAND: ALL THESE ATTRIBUTES WE HAVE DEFINED SO FAR, x, y and z. THESE ARE INSTANCES ATTRIBUTES.
# IN OTHER WORDS, THESE ARE ATTRIBUTES THAT BELONG TO POINT INSTANCES OR POINT OBJECTS. So every point point object
# can have different values for these attributes. Here is an example
# Using class reference. not working with any point objects, working with the Point class
Point.default_color = 'blue'
point = Point(1, 2)  # One point object with values 1, 2
# 28 is an object , we can use object reference to get access to the default color attribute
print(point.default_color)
# We can also use the point class to get  access to the default color attribute
print(Point.default_color)
# Class attributes are shared to all instances of a class, before printing the default color if I change the default color
# line 27
# Now it's blue line 39
point.draw()
another_point_object = Point(3, 4)  # Another point object with values 3, 4
# if we print another point object color its also changed
print(another_point_object.default_color)
another_point_object.draw()

# Two point object completely independent of each other.
# Each point has it's own attributes, just like John and Marry can have different eye colors
# THESE ARE INSTANCE ATTRIBUTES #


# We can also define CLASS ATTRIBUTES. These are attributes that we define at the class level and they are the same
# across all instances of this class.
# As a metaphor, we can say all humans have two eyes, and two ears. So these are the attributes we'll define at the class level.
# And they are shared by all instances. So back to our Point example, we can define a class level attribute in the body of the class.
