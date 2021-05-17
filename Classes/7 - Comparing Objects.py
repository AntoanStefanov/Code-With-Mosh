class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defining eq(equality) requires two parameters self and other
    def __eq__(self, other):
        # We need to return True if the two objects are equal, othwerwise False
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


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
# THEY ARE NOT EQUAL.

# To solve this problem, we need a magic method. That magic method is called when we compare two objects. line 7


# Now what if we wanted to compare these two point objects like this:
print(point > other)  # If point is greater than other
# We get a type error , because the greatter than operator is not supported between instances of Point class.

# To solve this problem, we need to define another magic method. line 11

# let's modify the values

point = Point(2, 3)
other = Point(1, 2)

print(point > other)

# What if we change to less than ?

print(point < other)

# We get False.
# As you can see we don't have to explicitly implement each of these operators.
# When you implement the greater than magic method, Python will automatically figure out what to do if you use the less than
# operator.