
# UNPYTHONIC #

# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

# prod = Product(10)

# Pythonic means that the code is not using Python's best practices.
# It's not using Python's language features to the best potential.

# Better way

# Using property

# Property is an object that sits in front of an attribute and allows you to get or set the value of that attribute.


class Product:
    def __init__(self, price):
        self.price = price # Using the price property like a regular attribute

    @property  # decorator for creating a property instead of line 54 and rename with an ideal name - price instead of get_price
    def price(self):
        return self.__price
    # When Python sees this code , it will automatically create a property object called price

    @price.setter # starts with the name of the property
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # Defining a property -> In the class after defining get and set price methods.
    # We define a class attribute with an ideal name, in that case, call it price.

    # Here we call the built in property function.
    # That function takes four parameters and all are optional.
    # first parameter is a function for getting the value of an attribute.
    # third parameter is a function for deleting the attribute.
    # forth parameter is for documentation.

    # In this case we need to supply two arguments,
    # First will be get_price and second will be set_price.
    # YOU DON'T CALL the functions, just PASSING A REFERENCE to them.
    # price = property(get_price, set_price) # instead of EXPLICITLY CALLING THE PROPERTY FUNCTION to create a property object,
    # We can apply the property decorator to the method line 32

    # So when we call the built in property function with these arguments.
    # This function will return a property object. That property object will use this function(get_price)
    # for reading the value of the price attribute.
    # Adding line 51, we can go back to our product and set the initial price to 10.
product = Product(10)

# When we use . notation product.
# product.  we can see we have the price property and we can use it like a regular field

print(product.price)

# So the property looks like a regular attribute from the outside, but internally has two methods that we call a getter and a setter.

# Now, while these price property solved our problem, the two methods that we wrote are still accessible
# If we type product.  we can see we have get price and set price methods.

# THESE METHODS ARE POLLUTING THE INTERFACE OF OUR OBJECT.
# We want our objects or our classes to have minimal number of functions or methods exposed to the outside.
# So, to hide these we can use decorators LINE #32 and 35

# WHEN DEFINING PROPERTIES < WE DONT ALWAYS HAVE TO DEFINE A GETTER AND A SETTER, IN THIS CASE  IF WE COMMENT OUT THE SETTER
# WE WILL HAVE A READ-ONLY PROPERTY , SO WE CAN ONLY READ THE VALUE, ONCE WE SET IT WE CANNOT CHANGE IT