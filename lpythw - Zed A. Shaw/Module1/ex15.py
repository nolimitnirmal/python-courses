# Reading a File 

from sys import argv # import argv (argument variables) from the sys modules.
# these are variable you enter into the command line when runnnign the script. 
script, filename = argv # unpacks the argv into to variables. 
# script name = "ex15.py" and filename = argv 
txt = open(filename) # open function used to open file entered into the command line 

print(f"Here's you file {filename}:") # prints the message in the bracket and siplays into iterm
print(txt.read()) # used read funtion in python to read entire content in the file. 

print("Type the filename again:") # prints this message and displays to user
file_again = input(">") # shows an input > and waits for user to type in the file name

txt_again = open(file_again) # the file name the user types in is stored as file_again

print(txt_again.read()) #this opens the file that the user just typed in. 
# reads and prints the contexts after.


# in summary:Takes a filename from the command line.
# Opens and shows the file.
# Then asks the user to type the filename again.
# Opens the file again using what the user typed, and shows the contents a second time.

