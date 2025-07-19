# assign 10 to types_of_people
type_of_people = 10
# assign the f-string to x (insert types_of_people in the string)
x = f"There are {type_of_people} types of people"
# assign binary to binary and do_not to don't
binary = "binary"
do_not = "don't"
# assign the f string to y (insert binary and do_not into the string)
y = f"Those who know {binary} and those who {do_not}."
# used to check and debut whether the line is broken after assigning the variable.
# the >>>> along with the comment helps you know where you are in the code once printed.
print(">>>> after assign y", y)

# prints variable x and y 
# no need to add format as it is pre defined already in the variable
print(x)
print(y)

# prints new string with x injected into it using the brace
# need to add format because you used the brace {} in the new string to add a variable
# when you format a string it iscalled an f-string 
print(f"I said: {x}")
print(f"I also said: '{y}'")


hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# using a .format() syntax 
# just another type of formatting

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)


