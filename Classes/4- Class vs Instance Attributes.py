# In the last lecture, we defined two attributes for our point objects in the constructor in the point class.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y}, {self.z})')


# Now whenever we create a Point object, this Point object will have these attributes by default.
# We can also define an attribute after we create a point object, so here we can set - point.z = 10
point = Point(1, 2)
point.z = 10  # beacuse objects in Python are dynamic. Similar to JavaScript, so we don't have to define all the attributes
# in the constructor, we can define them later, whenever we need them.


# IMPORTANT TO UNDERSTAND: ALL THESE ATTRIBUTES WE HAVE DEFINED SO FAR, x, y and z. THESE ARE INSTANCES ATTRIBUTES.
# IN OTHER WORDS, THESE ARE ATTRIBUTES THAT BELONG TO POINT INSTANCES OR POINT OBJECTS. So every point point object
# can have different values for these attributes. Here is an example

point = Point(1, 2)  # One point object with values 1, 2
point.draw()
another_point_object = Point(3, 4)  # Another point object with values 3, 4
another_point_object.draw()

# Two point object completely independent of each other.
# Each point has it's own attributes, just like John and Marry can have different eye colors
# THESE ARE INSTANCE ATTRIBUTES #


# We can also define CLASS ATTRIBUTES. These are attributes that we define at the class level and they are the same
# across all instances of this class.
# As a metaphor, we can say all humans have two eyes, and two ears. So these are the attributes we'll define at the class level.

