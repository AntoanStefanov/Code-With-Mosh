from sys import getsizeof
# Here we're creating a list using a list comprehension expression,
# then we iterate over all the numbers in this list and print them

values = [x * 2 for x in range(10)]
for x in values:
    print(x)

# This is perfectly fine, but there are situations where you might be working
# with a really large data set or perhaps an infinite stream of data,
# in those situations we shouldn't store all of those values in the memory,
# because that's very memory inefficient for example, what if instead of 10 here,
# we had a range of a billion, you don't want to store a billion objects in memory,
# that takes too much memory, in situations like this it's more efficient to use
# a generator object.

# Generator objects are iterable, so just like lists we can iterate over them,
# and in each iteration, we generate or spit out a new value.
# So , unlike lists, they don't store all the values and memory,
# they generate a new value in each iteration.
# Replacing [] with ()
values = (x * 2 for x in range(10))
# values is a generator object
print(type(values), values)
for x in values:
    print(x)

# Generator objects are iterable, we can iterate over them, and in each iteration
# they spit out a new value.

# The interesting thing is the generator objects size.
# Let me show you how we can get the size of an object
# from sys import getsizeof

values = (x * 2 for x in range(1000))
print('generator', getsizeof(values))
# Our generator object takes 56 bytes of memory~

# Let's try with 100 000

values = (x * 2 for x in range(100_000))
print('generator', getsizeof(values))

# Again it's 56 bytes of memory. The size of the generator object remains consistent.

# If we use list comprehension, we will end up with a list of 100 000 items

values = [x * 2 for x in range(100_000)]
print('list', getsizeof(values)) 

# the size of the list comprehension is 412228 bytes

# In situations where I am dealing with a really large data set,
# or potentially an infinite stream of data, use a generator expression ()
# to create a generator object, so when we use parenthesis around a comprehension
# expression.

# Just be aware that because generator objects don't store all items in memory
# you won't be able to get the total number of items you're working with.

values = (x * 2 for x in range(100_000))
print(len(values)) # Error

# WE CAN ONLY ACCESS THESE ITEMS WHEN WE ITERATE OVER A GENERATOR OBJECT.

# So, we won't know ahead of time, how many objects or how many items this generator
# is going to produce.
