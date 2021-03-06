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
# Now we call timeit
#  - first arg = python code , second arg(keyword arg) = number of exectutions
print('first code=', timeit(code1, number=10000))
# This function returns the exectution time of the code after 10 000 repetitions.


# DIfferent approach ### 4 times faster
code2 = '''
def calculate_xfactor(age):
    if age <= 0:
        None
    return age / 10


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
'''

print('second code=', timeit(code2, number=10000))


# that's so because we execute the code 10 000 times
# 1 time execution no difference
# If you are building a simple application for a few users raising exceptions
# in your functions is not going to have a bad impact on the performance of your app.

# But if you are building application where performance and scaleability is important,
# then it's better to raise exceptions when you really have to .

# if you can handle the situation with a simple if statement, think twice for exceptions.

# Raise exceptions if YOU REALLY HAVE TO !