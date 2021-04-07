try:
    age = int(input('Age: '))
except ValueError as ex: # ex as exception
    print("You didn't enter a valid age.")
    print(ex) # The actual error message that is included in exception
    print(type(ex))
else:
    print('No exceptions were thrown.')
print('Execution continues')

# Continue with the code from last lecture to handle
# the value error exception here, we need to put the statement
# in try block

# What is the type of the exception clause that we get
# if the user enters a non numeric value.
# That's valueError exception. You saw in the last lecture
# So we add the except clause and then we'll print a friendly error message

# When Python sees a try block it will execute every statement in this block,
# if any of these  statements throws an exception
# the code in the except clause will be executed
# If you don't have any exceptions, this code will not be executed
# input - a, and the app didn't crash! this is the important thing about
# handling exceptions.
# If you don't handle exceptions properly your program will crash.
# In other words if we add another statement after the block
# Let's print Execution continues
# IN this example, because we are handling this exception properly,
# The last statement will be executed
# In contrast in our last lecture where we didn't have the try block,
# if we put this print statement after getting user;s age this print will not be executed.

# We also have an optional else clause here
# And what we put inside this block will be executed if no exception
# is thrown in the code that we add to the try block.
# so, what we have in else clause will only be executed if we don't have any exceptions
# very similar to for else loops.
# I told you that the else statement is executed,
# If we don't break out of the for loop.
# In other words, if the for loop completes then the else clause is executed.

# So, here's a basic structure for handling exceptions.
# One more thing before we finish.
# When handling exceptions, we can optionally define a variable that will
# include the details about the exception.
# Mostly, the error message and sometimes additional arguments
# So , here we add 'as' and then define a variable, like 'error' or 'ex' for exception.
# after this error message let's just print the variable, also the type of variable(ex):

# invalid literal for int() with base 
# 10: 'a'
# <class 'ValueError'>

# This is very technical to show to an end user, so we're not going to print it on the terminal
# It's just for demonstration purposes
# And below that you can see the type of this exception
# It's an object of type ValueError
