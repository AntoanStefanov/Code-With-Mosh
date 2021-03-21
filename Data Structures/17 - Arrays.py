# If you have performance issues, replace lists with arrays. 90% List Usage
# Faster performance than lists
# Less memory usage than lists
from array import array  # from module 'array' import class called 'array' same name

# first parameter 'typecode' which is a string that determines the type of objects in your array. 'typecode' in google => See all type codes in python.
# It's a string of one char that the determines the type of objects  in your list signed int = 'i'
# Second arg we pass a list of integers
# Now we get array, call it numbers
numbers = array('i', [1, 2, 3])
# We have methods in this object for add new object or removing
# or insert for specific index , pop , remove . exactly like lists. We can access items by their index.
numbers.append(4)
# HOWEVER, unlike lists, the objects in this array are TYPED. So here every object should get INTEGER.
# If we ry to put a floating point number here or any other kind of objects, we will get an error.
# Changing first item to 1.0
numbers[0] = 1.0
# Run
# We get type error: integer argument expected, got float
# Every object of this array should be the same type , which is determined at the time of creating the array using typecode.
# RECAP:
# Use arrays only if you are dealing with large sequence of numbers and you encounter performance issues.
# For other cases use lists and tuples by default.
