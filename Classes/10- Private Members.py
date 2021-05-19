# The class from last lecture has a tiny problem.
class TagCloud:
    def __init__(self):
        # to make it private or inaccessible from the outside , prefix it with __ (2 underlines)
        self.__tags = {}

    def add(self, tag):
        tag = tag.lower()
        self.__tags[tag] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()  # TagCloud object
cloud.add('python')  # Calling add method passing python
cloud.add('python')  # Calling add method passing python
cloud.add('Python')  # Calling add method passing Python
# If we print cloud['PYTHON']
print(cloud['PYTHON'])  # We get 3. The program is working
# HOWEVER, If I access the underlying dictionary in this class our program will CRASH
# KeyError: 'PYTHON' That's exception. Because we dont have this key in our dictionary,
print(cloud.tags['PYTHON'])
# everything in our dictionary is stored in lowercase.

# So the problem with this class is that it gives us access to the underlying dictionary(self.tags)
# that is used to keep track of the count tags.

# To fix this problem we need to hide this attribute from the outside, so we cannot access it

# print(cloud.tags['PYTHON']) -> AttributeError: 'TagCloud' object has no attribute 'tags'

# If we use the dot operator