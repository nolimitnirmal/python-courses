from sys import argv
# this says 'bring the tool called argv fri the python sys module. 
# read the WYSS section for how to run this
script, first, second, third = argv
# this line unpacks the values from the argv
# that is, from the command line and puts them into 4 variables. 
# you must assign 3 variables after the scriot name when inputing the promt into the comand line 

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# on iterm run 'python3 ex13.py apple orange dragonfruit"
# this will assign the 3 arguments will get mapped to each argument above

# if you just run 'python3 ex13.py'
# you will get an error message saying. 
# "not enough values to unpack (expected 4, got 1)"
# you need to add values to assign each one to the argument in your scrupt. 
# need exaclty 4 values. the first one being your script name. "exp13.py"
# and in the case of this exercise. the other s=variable being
# "apple orange gragonfruit"

# if you have too many, that will also be an error

