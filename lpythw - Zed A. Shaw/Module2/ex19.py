
def cheese_and_crackers(cheese_count, boxes_of_crackers): # we define the functionn to take 2 arguments in the bracket
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  print("May that's enough for a party!")
  print("Get the blanket. \n")
# the 4 print lines are intended, which means that they are inside the function
# the \n will add an extra spacing line under the line 6 (it is an escape sequence)

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # calls the functions using numbers directly

print("OR, we can use variables from our script:")
amount_of_cheese = 10 
amount_of_crackers = 50 
# the 2 lines above create variables. 

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# the line above calls the function using these variables. 

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# this line does the math first and then passes it onto the function

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# we can add variables and numbers together to then pass it onto functions as shown above as well. 

"""
This exercise
1. Defines functions 
2. Calls them using numbers, variables and math. Or a mix of both. 
3. Prints the message using the function call. 

"""

