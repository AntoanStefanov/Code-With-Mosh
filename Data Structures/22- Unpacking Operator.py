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
first_list = [1, 2]
second_list = [3, 4]
# To combine the lists , we unpack the first one and then the second one

values = [*first_list, *second_list]
print(values)
# We can also put something in the middle
values = [*first_list, 'hi', *second_list]
print(values)
# Or unpack a string at the end
values = [*first_list, 'hi', *second_list, *'Hello']
print(values)

# We can also unpack dictionaries but we need too use 2 asterisks(**)
# If you use 1 * only the keys will combine, they are unordered.
# ** takes out all key value pairs in a dictionary
first_dictionary = {'x': 1}
second_dictionary = {'x': 10, 'y': 2}

combined_dictionary = {**first_dictionary, **second_dictionary}
print(combined_dictionary)
# NOTE that the value of x is 10, if you have multiple items with same key
# the last value will be used.

# we can add additionally another key value pair

combined_dictionary = {**first_dictionary, **second_dictionary, 'z': 3}
print(combined_dictionary)

# RECAP: WE CAN USE UNPACKING OPERATOR
# TO TAKE OUT INDIVIDUAL VALUES IN ANY INTERABLE.