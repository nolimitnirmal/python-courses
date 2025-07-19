import random

guesses = 0

while True:
    top_range = input("Choose a number! : ")

    if top_range.isdigit():
        top_range = int(top_range)
    
        if top_range <= 0:
            print("Pick a number above 0!")
            continue
        else:
            break
        
    else:
        print("Enter a number")
        continue
    
random_number = random.randint(1, top_range)


while True:
    guesses += 1
    user_number = input("Make a guess! : ")
    if user_number.isdigit():
        user_number = int(user_number)
        
        if user_number <= 0:
            print("Choose a number above 0")
            continue

    else:
        print("Choose a number ")
        
    if user_number == random_number:
        print("You got it right!")
        break
    elif user_number > random_number:
        print("Too high, try a lower number")
        continue
    else:
        print("Too low, try a bigger number")
        continue
         
    
print(f"You got it in {guesses} attempts!")
        

    
