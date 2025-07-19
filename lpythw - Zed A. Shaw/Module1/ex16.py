# Writing to a File. 

from sys import argv # omports argv fronm sys module

script, filename = argv # unpacks the 2 argv enetered in the command line into variables 

print(f"We're going to erase {filename}.") # prints this with the filename enetred in the command line 
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?") # waits for user to press enter 

print("Opening the file...")
target = open(filename, 'w') # telling python to open the file "filename"
# you need to type "w" when you intent to write to the file 
# w = write mode


print("Truncating the file. Goodbye!")
target.truncate() # moving the location to the beginning of the file and just erasing all the data. 

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # always close your files.



