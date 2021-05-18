# tags = {}

# def add_tag(tags, tag):
#     tags[tag] = tags.get(tag, 0) + 1

# add_tag(tags, 'python')


# You learned about the common data structures in Python, sets, lists and so on.

# These data structures or containers types are pretty useful and sufficient for most cases.

# There are times that you want to create your own custom container types(data structures).

# For example, here we have this class TagCloud

# With this class we can keep track of the number of various tags on a blog.

# Example: How many articles do we have that are tagged with Python or JavaScript and so on.


class TagCloud:  # Creating a class
    # Internally we are going to use one or more of the built in data structures(lists, dictionaries and so on).
    # We'll use dictionary, bcs we can get quickly get the number of given tag
    # We first define a constructor
    def __init__(self):
        # In the constructor, we initialize  tags attribute to an empty dict.
        self.tags = {}

    # We can optionally add a method like add, that takes a tag
    def add(self, tag):
        # If the key does not exist we get error so use get method
        # Here we should check if the tag has been added already. If we don't have it we are setting its value to 1,
        # otherwise increment the value with 1.
        # One way to implement this logic.
        tag = tag.lower()
        self.tags[tag] = self.tags.get(tag, 0) + 1  # With get method

    def __getitem__(self, tag):  # It should take self as well as a key
        # return self.tags[key] # If the key does not exist we get error so use get method

        return self.tags.get(tag.lower(), 0)  # So if doesn't exist we return 0

    # MY WAY ##
        ####
    # setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
    # def assign_item(self, tag, value):
    #     setattr(self, tag, value)
        ####

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        # using built in  functions to get iterator object .
        # An interator object is an object that want a container and gets one item at a time.
        # Call iter built in function. We want to iterate through self.tags
        # RETURNS ITERATOR OBJECT  WHICH GIVES US ONE ITEM AT A TIME IN A FOR LOOP
        return iter(self.tags)

        # # Because this class represents a container, it supports various operations around containers
        # cloud = TagCloud()  # creating an object
        # # Because this is a container we get get the number of items in this container,
        # len(cloud)
        # # We can get an item by it's key. For example: getting the number of articles tagged with python
        # cloud['python']
        # cloud['python'] = 10  # We can also set that
        # # And iterating over the container
        # for tag in cloud:
        #     print(tag)
        # # These are the operations that are supported by this custom container type


cloud = TagCloud()
cloud.add('python')
cloud.add('python')
cloud.add('python')
print(cloud.tags)

# Why we created a custom class instead of using a plain old dictionary,
# The reason for this is because I want to make it a little bit smarter than a typical dictionary.
cloud.add('Python')
cloud.add('python')
cloud.add('python')
print(cloud.tags)
# What if we add the python tag with capital P ?
# Technically, this is the same tag as the lowercase python,
# so when we run it it should be one python tag repeated 3 times.
# That's not what we get 2 seperate items , that's typical dict.
# In this class I am going to take care of case-sensitivity.
# Whatever tag we recieve, we will convert it to lowercase.

# So with this class, we're encapsulating the complexity around the case-sensitivity of tags,
# when using this class we no longer have to worry about lowercase or uppercase chars.
# So our code looks cleaner and simpler. All the complexity is encapsulated in the tag cloud class.
# It's not visible to the rest of our program.

# Next Level

# I want to be able to read the count of a tag like this - using square brackets.
print(cloud['python'])
print(cloud['js'])
# For that we need a magic method __getitem__ or we will have an error: TypeError: 'TagCloud' object is not subscriptable.
# Line 38 ^

# As You can see with this implementation we can easily get the number of a given tag, we can't do this with
# typical dictionary. If we don't have the python tag our dictionary would throw an error

# NEXT LEVEL

# With the current implementation, you can only read the number of a given tag, you cannot set it like this
# cloud.assign_item('C#', 10) LINE 43

cloud['C#'] = 10
print(cloud['C#'])
# To do that we need to implement another magic method called __setitem__ (LINE 51)
# With this implementation we can set the number of a given tag 105 line

# Now in order to get the number of items in this tag cloud , we should implement the len magic method LINE 54
print(cloud.__dict__)
print(len(cloud))


# And finally to make this iterable, so to iterate over a for loop.
# We need to implement another magic method that is __iter__ LINE 58

for tag in cloud:
    print(tag)
