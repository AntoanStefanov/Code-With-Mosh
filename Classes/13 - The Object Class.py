# The Animal we defined inherits from another class called object
# Even though we didn'y add Animal(object), object class is the base class for all classes in Python.


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eating')


class Mammal(Animal):
    def walk(self):
        print('walking')


class Fish(Animal):
    def swim(self):
        print('swimming')


m = Mammal()

# Couple useful built in functions:
# isinstance Return whether an object is an instance of a class or of a subclass thereof.
print(isinstance(m, object))

# Also we have built-in function for creating an empty object
empty_object = object()
# let's inspect the object, you can see all these magic methods, every object has these magic methods,
# inherited from the base object class
# empty_object.

# another built-in function that is useful:

# Return whether 'cls' is a derived from another class or is the same class.
print(issubclass(Mammal, object))
