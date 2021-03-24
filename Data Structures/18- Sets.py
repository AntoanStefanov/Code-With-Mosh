# Another useful data structure called Set.
# Which is basically a collection with NO duplicates

numbers = [1, 1, 2, 3, 4]

# If you want to remove the duplicates, you can convert it to a set.
# Define variable , call the set function and pass the list
uniques = set(numbers)
print(uniques)
# We only have uniques items , so 1 is not repeated
# NOTE We use curly braces to define sets - {}

# We can define a second set using curly braces
second_set = {1, 4}
# Similar to lists we can add new items to a set or remove an existing one
# We can call add method, we can append new number, we can use remove and
# len function (returns the number of items in a set)
second_set.add(5)
second_set.remove(4)
len(second_set)
# These are the basics.

###################################################################################

# Sets shine are in the powerful mathematical operations that are supported by them.
# We have two sets now.
first = set(numbers)
second = {1, 5}

print(second)
# 1. We can get a union of two sets, using the vertical bar.
print(first | second)
# This expression will return
# a new set that includes all the items that are either in the first set or in the second set.

# 2. We can also get the intersection of two sets
print(first & second)
# This expression will return
# a new set that includes all the items that are IN both first and second sets
# The only number that is IN both first set and second set is 1.

# 3. We can also get the difference between two sets
print(first - second)
# This expression will return {2, 3, 4}
# So the first set has these additional items that we don't have in the second set

# 4. We can also get the semantic difference ^ - carrot
print(first ^ second)
# This expression will return
# the items that are either in the first or second sets but not both


# One thing you need to know about sets is that unlike lists:
# ! They are an unordered collection:
# Which means the items that we have in a set are not in sequence.
# So we cannot access them, using an index.

# IF we try to print
# print(first[0])
# We get TypeError: 'set' object is not subscriptable

# If you need to access items by index, you need to use a list.
# In sets quite often we use one of these operations here
# Or We can check for the existance of an item in a set.

if 1 in first:
    print('Yes')


# RECAP:
    # Set is an unordered collection of unique items.
    # We cannot have a duplicate
    # This object is unordered, it is not in sequence,
    # so we cannot access it using an index.
