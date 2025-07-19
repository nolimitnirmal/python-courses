import random 

# let the user pick the top rang elif
# genrate a random umber 
# make the user guess the number 
# print message 
# guesses 

guesses = 0

while True:
    top_range = input("Pick a number! : ")
    
    if top_range.isdigit():
        top_range = int(top_range)
        
        if top_range <= 0:
            print("Please choose a number above 0")
            continue
        else:
            break 
        
    else:
        print("Please select a number")
        continue
    

random_number = random.randint(1, top_range)

while True:
    guesses += 0
    user_input = input("Make a guess : ")
    
    if user_input.isdigit():
        user_input = int(user_input)
        
        if user_input <= 0:
            print("Please enter a number above 0")
            continue
    
    else:
        print("Please guess a number")
        
    if user_input == random_number:
        print("You got it right!")
        break
    elif user_input > random_number:    
        print("Too high, try again")
        continue
    else:
        print("Too low, try again")
        continue
    
print(f"\t \n \n  You got it in {guesses} tries!!")

