
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
        pass

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # Defining a property -> In the class after defining get and set price methods.
    # We define a class attribute with an ideal name, in that case, call it price.

    # Here we call the built in property function
    price = property()  
