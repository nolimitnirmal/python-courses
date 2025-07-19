# More Files 

# Copies everything from test.txt to copy.txt (this file doesnt exist until this script is ran)

from sys import argv # imports argv from system module 
from os.path import exists # imports exist() function from python. to check is a file already exists. 

script, from_file, to_file = argv # unpacks the argv into 3 variables. 3 values were entered into the command line. 
# script = python file name 
# from_file = file youre copying from 
# to_file = the file youre copying to 

print(f"Copying fom {from_file} to {to_file}") # standard print with the variables identified above

# we could do these two on one line, how?
in_file = open(from_file) # opens the source file. File copying from. and gives it a new variable
indata = in_file.read() # reads the full file from the source file. gives it a new variable "in_file"

print(f"The input file is {len(indata)} bytes long") # Remember what a len function does? gives you back the size of the file in numbers. (no. of characters) 

print(f"Does the output file exist? {exists(to_file)}") # Checks if the file that youre coying to exists or not. 
# exist() gives us back a true of false velue if the file exists or not 
print("Ready, hit RETURN to continue, CTRL-C to abort.") # regular print 
input() # waits for user input 

out_file = open(to_file, 'w') # opens the d estination file in write mode. 
# if file doesn't exist, it will be created. if it does exist it will be overwritten. 
out_file.write(indata) # writes contents from the source file to destination file  

print("Alright, all done.") # print

out_file.close() 
in_file.close()
# closes both files. 

