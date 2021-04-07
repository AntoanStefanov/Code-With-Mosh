try:
    age = int(input('Age: '))
except ValueError:
    print("You didn't enter a valid age.")
else:

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
# And what we put in 