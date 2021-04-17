# So far you have learned how to handle exceptions,
# but you can also raise or throw exceptions in your own code.

# Example:
# age cannot be 0 or less
# if that is the input we raise an exception
# using raise statement and specify the type of our exception, add error message.
# We have this function that raises or throws an exception
# if we give it an invalid argument.

# Somewhere in our program you're going to use this function,
# with -1 the program crashed with a value error exception and message shown.
# That happened bcs we didn't handle exceptions properly,
# so we didn't have a try block. To fix this issue , let's add
# a try block then exception clause

# In Python have various kinds of exceptions.
# Search in google: python 3 built-in exceptions.
# There is a hierarchy. They are sufficient for most cases.
# You can also define your own exception types, it's not something you do that often.
# But you can do for sure. You need classes


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')

    return 10 / age


try:  # Try block
    calculate_xfactor(-1)
# Except clause of type value error.
# Giving this exception object a name like error
except ValueError as error:
    print(error)  # Here we can simply print this error

##### This way the program didnt crash and the message is shown

# This way you raise exceptions, but THIS IS NOT SOMETHING that I advise you to do.
# Explained it here, because you will see it in other ppl's code.

# Raising exceptions is costly, in this example, instead of raising an exception,
# and then handling it, you could take a different approach that owuld result
# in better performance, that's for the next lecture.
