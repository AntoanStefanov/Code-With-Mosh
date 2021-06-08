# importing functions from sales module.

# AFTER IMPORT PRESS CTRL + SPACE, ENTER , DELETE WHAT TABNINE WROTE YOU AND immediately CTRL AND SPACE AGAIN.
# that way you can see all the objects
# defined in this module
from sales import calc_shipping, calc_tax
# Now we can call the function, just like we have defined in our app module.
# Shortcut to import multiple objects. It's shorter but it's bad practice,
from sales import *
# Because in that module you could have 

calc_shipping()
calc_tax()
