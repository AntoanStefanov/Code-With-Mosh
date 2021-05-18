# We also have magic methods for performing arithmetic operations between two objects.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Returns a new Point object with these values, 1st arg and 2nd argument(x, y)
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
another_point = Point(1, 2)


# For example, what if we wanted to add these two points together.
# Error if you run it .

# In order to add two points together, we need to implement add method

# We get this new Point object at this address and don't see the actual values(x, y).
print(point + another_point)
# Because I removed the str magic method
# Store the result of this arithmetic operation in another object
sum_of_two_points = point + another_point
# and print sum_of_two_points.x
print(sum_of_two_points.x) # 11 And we added two points together.
