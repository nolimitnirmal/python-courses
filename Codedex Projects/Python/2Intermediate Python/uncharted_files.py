
sent_message = "Hey there! This is a secret message." # sent message as variable 

with open("sent_message.txt", "w") as file: # open file using with operator in write mode. saved as file 
    file.write(sent_message) # use write method to write the sent message into the file 


with open("sent_message.txt", "r+") as file: # use with operator to open a file in read and write mode with "r+". saved as file 
    original_message = file.read() # read original file and save as variable
    file.seek(0) # seek method used to move cursor to the beginning 
    unsent_message = "This message has been deleted" # save unsent message string as a variable 
    file.truncate(len(unsent_message)) # truncase to the size of the unsent message 
    file.write(unsent_message) # user write method to write the unsent message into the file 

# with operator willl always close the file automatically 


print(f"Original Message:  {original_message}") # prints the original message
print(f"Unsent Message:  {unsent_message}") # prints the unsent message 
