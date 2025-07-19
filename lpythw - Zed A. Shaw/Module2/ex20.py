from sys import argv # this imports argv list from the system module

script, input_file = argv # unpacks the arguments from the command line into variables. 

def print_all(f): # defines the print_all function. file object (f) is a file that is already opened. 
  print(f.read()) # takes all fht ef object and prints the whole content using read.(f)

def rewind(f): # new funtion rewind, takes the file pointe r back to the beginning. 
  f.seek(0) # like rewinding a tape. 

def print_a_line(line_count, f): # define a new function. print_a_line. Take 2 arguments. 
  # line_count and f are 2 arguments defined by the user. 
  print(line_count, f.readline()) # prints line count first. 
  # f.readline() reads the the line first and moves onto the next line automatically. (just how it works)

current_file = open(input_file) # opens input_file and stores it as a variable 

print("First let's print the whole file:\n") # uses escape sequence to start a new line 

print_all(current_file) # Calls print_all funtion to print entire file 

print("\n")

print("Now let's rewind, kind of like a tape.\n") # 

rewind(current_file) # calls rewind function to move pointer back to the beginning of the file 

print("Let's print three lines:\n")

current_line = 1 # sets current_line vsriable to 1 and prints the first line of the file 
print_a_line(current_line, current_file)

current_line = current_line + 1 # increases the count to 2 and prints out the next line in the script. 
print_a_line(current_line, current_file)

rewind(current_file)

current_line = current_line + 1 # increases the count again and prints out the third line. 
print_a_line(current_line, current_file)

'''
1. Takes the file name from the command line 
2. Prints the whole file. 
3. Rewinds the file pointer back to the beginning of the file 
4. Prints the first 3 lines of the file one by one. 
'''