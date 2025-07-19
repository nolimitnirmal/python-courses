# While loops 

i = 0 #i is set to 0
numbers = [] # this is an empty lost. you are going to add numbers to it 

while i < 6: # this is the while loop. Means, as long as 6 is less than 0, keep looping.
  print(f"At the top is {i}") # this prints out the string and the current value of i before adding it to the list. 
  numbers.append(i) # adds i to the numbers list. 

  i = i + 1 # adds 1 to i
  print("Numbers now: ", numbers) # prints the string and the list
  print(f"At the bottom i is {i}") # prints the updated value of i 

# this code block is repeated until the expression i<6 is false. 
# when it is false, it will move down 

print("The numbers: ") # prints the string

for num in numbers:
  print(num)

# the last code block prints all the numbers that you have added to the list. one by one. 

"""
in summary:
1. you start at 0 and keep adding numbers until you reach 5
2. print strings along the way to show the progress
3. then you print all the numbers at the end 1 by 1 
"""




