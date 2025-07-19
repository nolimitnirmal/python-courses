# This exercise shows you how to use arguments and input together. 

from sys import argv #imports argv (tool) from python's sys module
# argv allows the script get the input from the command line 

script, user_name = argv # this line unpacks the command-line arguments. 
# user_name is the first argument 
# script is the name of the file (ex14.py in this case)
prompt = '❌ '
# uses this as a prompt when asking for the input from the user. 
# just gives the input a better style when running the script. 

print(f"Hi {user_name}, I'm the {script} script.") # prints the message using the script name and argument entered in the command line 
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) # asks for an input from the user and waits until entered. with the > prompt from the script. 
# also stores the value that they enter as likes. 

print(f"Where do you live {user_name}?")
lives = input(prompt)
# same as above, stores the value entered as lives. 

print("What kind of computer do you have?")
computer = input(prompt)
# stores the value entered as the variable computer. 

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# summarises the values you entered in this message
# this is how a argument and an input can be used in a script. 
