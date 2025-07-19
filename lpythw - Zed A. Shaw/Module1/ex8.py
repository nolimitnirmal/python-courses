formatter = "{} {} {} {}"

# you are using the .format to tell it to format using the terms that you are dfining


print(formatter.format(1,2,3,4)) #this is a number. numbers and strings dont need to be in quotes 
print(formatter.format("one", "two", "three", "four")) # this is a string, telling python that it is a text 
print(formatter.format(True, False, True, False)) # this is a concept python understands as true of false. it you want to print as text add quotes. 
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I",
    "am",
    "the",
    "Goat"
))

# 