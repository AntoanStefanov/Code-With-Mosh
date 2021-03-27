values = []
for x in range(5):
    values.append(x * 2)

# Whenever you have this pattern in your code,
# You can either use the map function
# Or PREFERABLY a list comprehension.
# [expression for item in items]
values = [x * 2 for x in range(5)]
# That's exactly identical to the previous pattern.

# We can also use comprehensions with sets and dictionaries
# Set comprehension
values = {x * 2 for x in range(5)}
