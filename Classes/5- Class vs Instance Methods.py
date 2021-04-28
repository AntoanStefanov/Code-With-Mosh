# Last lecture, I learned about class vs instance attributes. We have the same concept around the methods that we define
# in a class. So we have instance methods as well as class methods, in this example, both these methods that
# we have defined in the point class are instance methods, so we can call them using an instance of the point class,
# using an object.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define method call it zero, call its first parameter cls which is short for class, like self
    # decorator, it's a way to extend the behavior of a method or function, later we will see how it works.
    @classmethod
    def zero(cls):  # Thats all decorator and method with cls reference need to create a class method
        # with the reference cls we can create a point object with inital values
        return cls(0, 0)  # call cls and give it the initial values.
        # That's exactly like calling  Point(0, 0). The difference is that if you use cls
        # AT RUNTIME , WHEN WE CALL THE ZERO METHOD, PYTHON INTERPRETER WILL AUTOMATICALLY PASS A REFERENCE
        # TO THE POINT CLASS TO THE ZERO METHOD. So we create a point object  and return it
    # this is purely convention, you can call this anything, but by convention whenever we  define a class method
    # we call it's parameter cls. This is reference to the class itself, so here, we are not working with a point object
    # or a point instance.
    # Now to make this method a class method, we need to decorate it with somth like this

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
point.draw()

# Generally speaking, you use these instance methods whenever we need an object reference, for example, when drawing
# a point, you really need to work with a specific point object.
# That's why this draw method is defined as an instance method.
# But there are times that you don't really need an existing object and that's when we use a class method.

# For example, let's say in our program, there are a lot of cases where we want to create a point with these initial values.

# This is one way to create a point object and that's perfectly fine but we can come up with a
point = Point(0, 0)
# different way to create a point object with these values. Like this:
# Point.zero()  # Note that I'm using a class reference. In this case zero is a class method that is defined at the class
# level and when we call it , it will return a point object initialized with 0, 0 values.
# So we can get this point object and assign it to this point variable
# In this exmaple , we refer to this zero method as factory method, because it's like a factory,
point = Point.zero()
point.draw()
# It creates a new object. This example is pretty basic, creating a zero point with these initial values is not a big deal.
# But there are times where initializing na object can be pretty complex. So every time you want to create an object
# of a given type, you might have to pass some magical values hereand you might have to repeat this in several places
# in your program, in that case instead of passing all the magical values to create an object, we can define a factory
# method that will return an object with these values and this way you can move this complexity of creating this object
# into a factory method.

# Let's see how to define a method at the class level.
