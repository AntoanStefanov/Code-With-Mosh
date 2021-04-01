# One operator that comes handy when wokring with these data structures
# is the unpacking operator
numbers = [1, 2, 3]
print(numbers)
# printing the list on the terminal, but what if
# we wanted 1 2 3 individually
# all we have to do is to prefix the variable with the unpacking operator.
print(*numbers)
# Here we unpack the container
# Take out it's individual elements
# and pass them as arbitrary arguments
# to the print function.

# Another useful application of this is when
# creating lists, so let's say a list of numbers
# we want to have list of numbers from 0 to 5
# You know that range(5) function will return a range object.
# so we need to convert it to a list and store result in variable

values = list(range(5))
print(values)

# In this case , instead of calling the list function,
# we can use the unpacking operator

# So we call range(5), this returns an iterable
# The good thing about this unpacking operator is
# we can UNPACK ANY ITERABLE!
# We unpack this iterable which basically means we take individual values
# then we put them in a list and finally store the result
result = [*range(5)]
print(result)
# By the same token, we can unpack a string
result = [*range(5), *'Hello']
print(result)

# Another example . Using this operator, we can combine multiple lists.
first_list = []
