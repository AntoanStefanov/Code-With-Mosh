# Powerful data structure - Dictionary
# Collection of key: value pairs
# We use it to map a key to a value
# Real life example : phone book - we map person's name to their contact details.

# key: value
# Define a dictionary
point = {'x': 1, 'y': 2}
# We can also use the dict function
# With this func we pass one or more keyword arguments
point = dict(x=1, y=2)  # Cleaner and shorter

# In Python we can only use immutable types for the keys so quite often we use strings and numbers, (tuples).
# But the value can be of any type.

# We can get the value associated with a key using an index. Our index is the name of a key.
# point of x
print(point['x'])
# Because dicts are collections of key value pairs,
# we cannot access an item using a numeric index as we do with list. point[0]

# We can change the value of x to a new value
point['x'] = 10

# We can add a new key
point['z'] = 20

print(point)

# When reading a value, if we use an invalid key we get an error
# Look up the value of the item with the key 'a'.
# print(point['a'])
# KeyError
# Two workarounds here:
# First : check for the existence of a key

if 'a' in point:
    print(point['a'])

# Second: use get method
# Instead of using
# point['a']
# We call the get method
print(point.get('a'))
# If the key doesn't exist , by default returns None
# Or we can pass a default value as a second argument
print(point.get('a', 0))

# To delete an item we use the del or delete statement
del point['x']
print(point)


# Loop over dictionary
# In each iteration our loop variable, will hold the key of an item , so rename it to key
# We can print the value associated with the key
for key in point:
    print(key, point[key])

# Another way for iteration over dict

for x in point.items():
    print(x)

# In each iteration we get a tuple of key and value, so we can unpack it.

for key, value in point.items():
    print(key, value)
