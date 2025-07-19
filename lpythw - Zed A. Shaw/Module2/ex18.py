# Defining Functions and Calling Functions 

# like the previous scripts with argv 

def print_two(*args): # def means "define". we also gave this function a name "print_two"
  arg1, arg2 = args # the colon from the last line makes it intend. everything under it will be attached to print_two 
  # line 5 unpacks the arguments and gives it 2 variables.
  print(f"arg1: {arg1}, arg2: {arg2}") # these variables are then printed out 

# the arg* is actually pointless, we can do this instead 
# this is to show that we can skip the unpacking section of this 

def print_two_again(arg1, arg2): # print_two_again is defined with 2 arguments 
  print(f"arg1: {arg1}, arg2: {arg2}") # printed 

# this just takes one argument 

def print_one(arg1): # print_one is defined using one argument 
  print(f"arg1: {arg1}") # printed 

# this one takes no arguments 

def print_none(): # print_none funtion is defined with no arguments 
  print("I got nothing'.") # printed 


# As shown below, the user defines the argument that goes into each one of the 
# pre defined functions 

# this is also known as "calling" a function. 
# the print in the def() section only outlines what the function does. 
# it can only be printed when it is "called"

# |Function Calls basucally Run the functions that you have set up in the script. 

print_two ("Zed","Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# to run, call or use the function all means the same thing 






