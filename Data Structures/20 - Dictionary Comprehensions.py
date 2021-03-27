values = []
for x in range(5):
    values.append(x * 2)

# Whenever you have this pattern in your code,
# You can either use the map function
# Or PREFERABLY a list comprehension.
# [expression for item in items]
values = [x * 2 for x in range(5)]
# That's exactly identical to the previous pattern.

# We can also use comprehensions with sets and dictionaries
# Set comprehension
values = {x * 2 for x in range(5)}

# What is the syntactical difference between set and dictionary?
# For both these data structures we use {} - curly braces.
# In set we just have values {1, 2, 3, 4}
# But in dictionary we have key value pairs,
# that are separeted by : - colon
# {1: 'a', 2: 'b'}
# So we easily can use comprehension expressions to create
# dictionary objects
# We need to change the comprehension expression
# to have a key value pair
# x as the key and x * 2 as the value
values = {x: x * 2 for x in range(5)}

# That's equal to

values = {}
for x in range(5):
    values[x] = x * 2
# This pattern is done by dictionary comprehension

# We use comprehensions with lists, sets, dictionaries
# What about tuples?
values = (x for x in range(5))
print(values)
# We don't get a tuple, we get a generator object
# Next lecture
