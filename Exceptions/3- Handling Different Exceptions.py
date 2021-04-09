try:
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You didnt enter a valid age.')
except ZeroDivisionError:
    print('You didnt enter a valid age.')
else:
    print("No exceptions were thorwn.")

# Let's make a magic formula
# Entering 0 as age - program crashes again.
# We got different kind of exception that is a zero division error.
# because in programming we can't a number divide by 0
# The statement on line 3 threw an exception!
# But we don't have a matching except clause with that kind of exception.
# In other words. In this code you're only handling value error exceptions.
# That's why our program crashed.

# To solve this problem, you can add a second except clause,
# And specify a different kind of exception , in this case, ZeroDivisionError
# And print message like age cannot be zero
# Now the program didnt crash with input 0 .

# Next level:
# Imagine the user enters 0 for the age, you want to print the exact same
# error message 'You didnt enter a valid age.'
# So copy and paste at the two exceptions
# Now the code is repetitive and that means
# If in the future we want to change this message, we have to change it in two places.

# Better way:
# In front of the except clause , we can specify multiple types of exceptions,
# So, if the exception that is thrown matches any of those exceptions,
# Then the code in except block will be executed.
# To specify multiple types of exceptions use () seperated by ,
# With the two exceptions we get only 1 MESSAGE ?
# In other words, the code we have in the second except block was not executed, otherwise
# we would see this message twice.

# When python executes the code that we have in the try block,
# if any of these statements throws an exception that matches one of the except clauses,
# that except clause is executed and the other except clauses are ignored

# DELETE line 6 and 7 (Unnecessary)
