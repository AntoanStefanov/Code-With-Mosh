# As I explained in the last lecture, when writing your own functions,
# prefer not to raise exceptions, because those exceptions come with a price.
# That's gonna show you in this lecture.

# From the timeit module import function called timeit
# with this function we can calculate the execution time of some code.

# This is how it works. Imagine you want to calculate the execution time of
# this code.

# We define a variable code1 and set it to string
# This string should include our code so using triple quotes code
# for multiple lines. One piece of code inside string with triple quotes
from timeit import timeit
code1 = '''
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return age / 10


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
'''
