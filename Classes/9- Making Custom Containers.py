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
        # Here we should check if the tag has been added already. If we don't have it we are setting its value to 1,
        # otherwise increment the value with 1.
        # One way to implement this logic.
        tag = tag.lower()
        self.tags[tag] = self.tags.get(tag, 0) + 1  # With get method


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