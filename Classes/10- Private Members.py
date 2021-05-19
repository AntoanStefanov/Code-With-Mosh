# The class from last lecture has a tiny problem.
class TagCloud:
    def __init__(self):
        # to make it private or inaccessible from the outside , prefix it with __ (2 underlines)
        self.__tags = {}

    def add(self, tag):
        tag = tag.lower()
        self.__tags[tag] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()  # TagCloud object
cloud.add('python')  # Calling add method passing python
cloud.add('python')  # Calling add method passing python
cloud.add('Python')  # Calling add method passing Python
# If we print cloud['PYTHON']
print(cloud['PYTHON'])  # We get 3. The program is working
# HOWEVER, If I access the underlying dictionary in this class our program will CRASH
# KeyError: 'PYTHON' That's exception. Because we dont have this key in our dictionary,
# print(cloud.tags['PYTHON'])
# everything in our dictionary is stored in lowercase.

# So the problem with this class is that it gives us access to the underlying dictionary(self.tags)
# that is used to keep track of the count tags.

# To fix this problem we need to hide this attribute from the outside, so we cannot access it

# print(cloud.tags['PYTHON']) -> EXCEPTION  of type -- > AttributeError: 'TagCloud' object has no attribute 'tags'

# If we use the dot operator
# cloud. # We no longer have tags here, also dont have __tags

# That's how we make certain attributes or methods private with __.

# Technically, these members are still accessible from the outside, it's just harder to access them.

# The point of this practice is not security, it's more of a warning or alert to someone who is using this class.

# It's telling the consumer of this class, hey, don't touch this, it's private.

# You can access them this way:
# Every class or every class/object has this property __dict__
print(cloud.__dict__)  # dictionary THAT HOLD ALL THE ATTRIBUTES IN THIS CLASS.

# THIS CLASS HAVE THIS ATTRIBUTE : _TagCloud__tags

# When Python interpreter  runs this code, it automatically rename this atribute and prefix it with _name of the class

# We can still access it with this attribute

print(cloud._TagCloud__tags)

# In Python, unlike Java, C#, we don't really have the concept of private members, they are still accessible

# Using double underscore is more of a convention to prevent accidental access of these private members.
