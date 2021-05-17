class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# There are times that we need to compare two objects, for example, here we have
# this point object, if I define another point object with the exact same values.
point = Point(1, 2)
other = Point(1, 2)
# Then compare them
print(point == other)
# We get False , what's going on ?
# The reason we get False is that by default this equality operators compares the references or addresses of these two
# objects in memory. 

# In this case these two variables(point, other) are referencing two different objects in memory and that's why 
# THEY ARE NOT EQUAL