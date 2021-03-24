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

# In Python we can only use immutable types for the keys so quite often we use strings and numbers.
# But the value can be of any type.

# We can get the value associated with a key using an index. Our index is the name of a key.
# point of x
print(point['x'])
# Because dicts are collections of key value pairs , we cannot an item using a numerate index as we do with list.

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
