# In the last lecture , we use the finally clause to release external resources.
# We have a shorter and cleaner way to achieve the same thing without the
# finally clause, but it doesn't always work for certain kind of objects.

# instead of getting the return value of the open function
# you prefix this with the with statement
# Then we'll get access to the return value of this function.
# by typing as file, so this is the file object that,
# the open function return
# In the block of code, we can work with this file object
# example: read smth from this file, write and so on.
# let's just print - file opened
# Whenever we open a file, using the with statement
# Python will AUTOMATICALLY CALL file.close,
# whether we have finally clause or not
# In other words, the with statement is used to automatically release
# external resources.
# How this work under the hood
# look at this file object file. # these are the members of the file object.
# We have methods that starts with __ and we refer to them as magic methods.
# Here we have 2 magic methods that u need to know . enter and exit.
# When an object has these two methods we say that objects supports
# context management protocol, if objects supports it (means has enter and exit),
# you can use that object with the with statement.
# Python will automatically call the exit method,
# and there will release external resourses.
# That's the reason we dont need a finally clause here.
# Next level: There are times that you might be working with multiple external resourses.
# let's say you want to read some data from one file and write it to another.
# How ?
# before the column , we can add a comma and open another external resourse like a file.
# With this python will automatically release both these external resourses
try:
    with open('4- Cleaning Up.py') as file, open('3- Handling Different Exceptions.py') as target:  # target is a variable name
        print('File Opened.')
        # file.__exit__() and file.__enter__()
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You didnt enter a valid age.')
else:
    print("No exceptions were thorwn.")
