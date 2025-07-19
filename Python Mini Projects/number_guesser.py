import random

guesses = 0

# user selects a range for the number 
while True:
    user_selects_range = input("Choose a number : ")
    
    if user_selects_range.isdigit():
        top_range = int(user_selects_range)
        
        if top_range <= 0:
            print("Please select a number above 0")
            continue
        else:
            break 
        
    else:
        print("Please select a number")

# generate random number 

random_number = random.randint(1, top_range)

# user selects a number 
# what happens whan the number is equal to egenrated number 

while True:
    guesses += 1
    user_input = input("Make a guess : ")
    
    if user_input.isdigit():
        user_input = int(user_input)
            
        if user_input <= 0:
            print("Please enter a number above 0")
            continue
    
    else:
        print("Please select a number")
        
    if user_input == random_number:
        print("Congrats, you got it right")
        break
    elif user_input < random_number:
        print("Too low, try again")
        continue
    else:
        print("Too high, try again")
        continue

print(f"Your got it in {guesses} guesses!")
