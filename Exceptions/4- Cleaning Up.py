# There are times that we need to work with external resources like files,
# network connections, databases and so on. Whenever we use these resources,
# after, after we're done we need to release them.
# For example: when you open a file, we should always close it after we're done,
# otherwise another process or another program may not be able to open that file.


try:
    file = open('name')
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You didnt enter a valid age.')
else:
    print("No exceptions were thorwn.")
finally:  # always executed clause with or without exception
    # and we use it to release external resources
    file.close()
