
#search starting from current working directory and all location in the 
#python PATH

#from package import module : Note: mypackage folder should be in the current project or in python path
from mypackage import mymodule

#from displaymodule of mypackage import the functionality of display_greeting
from mypackage.displaymodule import display_greeting

ans = mymodule.square(10)

display_greeting("Harshit","Good Afternoon")

print(ans)
