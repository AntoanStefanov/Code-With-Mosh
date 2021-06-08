# importing functions from sales module.

# AFTER IMPORT PRESS CTRL + SPACE, ENTER , DELETE WHAT TABNINE WROTE YOU AND immediately CTRL AND SPACE AGAIN.
# that way you can see all the objects
# defined in this module
from sales import calc_shipping, calc_tax
# Now we can call the function, just like we have defined in our app module.
# Shortcut to import multiple objects. It's shorter but it's bad practice,
from sales import *
# Because in that module you could have several different functions or variables,
# and if you blindly import them into the current module, some of those objects may overwrite
# the objects with the same name in the current module. SO DONT IMPORT ALL OBJECTS LIKE THIS.

# IMPORT ONLY THE STUFF YOU NEED !

# Another way
# import sales # Now in this module we have an object called sales and you can use the dot operator to access it's members.
# So now calculater shipping fucntion is now a method  in this object sales.calc_shipping()
calc_shipping()
calc_tax()


# YOU CAN IMPORT THE ENTIRE MODULE AS AN OBJECT, or you can import specific objects from that module.
# your choice.
