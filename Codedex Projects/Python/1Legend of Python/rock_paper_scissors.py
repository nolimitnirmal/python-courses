import random
print("==================================================")

print("\tRock Paper Scissors Lizard Spock")

print("==================================================")

player = 0
computer = 0
attempts = 0

print("""
    1) ✊
    2) ✋
    3) ✌️  
    4) 🦎
    5) 🖖
      """)

while attempts < 10:
    
    computer_1 = random.randint(1, 5)
    
    player_1 = input("Pick a number : ")
    if player_1.isdigit():
        player_1 = int(player_1)
        
        if player_1 > 5:
            print("Please choose a number between 1 and 3.")
            print("Minus 1 attempt")
            continue
    
    else:
        print("Please enter a valid number")
        print("Minus 1 attempt")
        continue
    
    attempts += 1



    if player_1 == 1 and computer_1 == 3: # rock beats scissors 
        print("""
            You chose: ✊
            CPU chose: ✌️
            You Won!
            """)
        player += 1
    if player_1 == 1 and computer_1 == 4: # rock beats lizard 
        print("""
            You chose: ✊
            CPU chose: 🦎
            You Won!
            """)
        player += 1
    elif player_1 == 2 and computer_1 == 1: # paper beats rock 
        print("""
            You chose: ✋
            CPU chose: ✊
            You Won!
            """)
        player += 1
    elif player_1 == 2 and computer_1 == 5: # paper beats spock 
        print("""
            You chose: ✋
            CPU chose: 🖖
            You Won!
            """)
        player += 1
    elif player_1 == 3 and computer_1 == 2: # scissors beats paper 
        print("""
            You chose: ✌️
            CPU chose: ✋
            You Won!
            """)
        player += 1
    elif player_1 == 3 and computer_1 == 4: # scissors beatslizard 
        print("""
            You chose: ✌️
            CPU chose: 🦎
            You Won!
            """)
        player += 1

    elif player_1 == 4 and computer_1 == 2: # lizard beats paper
        print("""
            You chose: 🦎
            CPU chose: ✋
            You Won!
            """)
        player += 1
    elif player_1 == 4 and computer_1 == 5: # lizard beats spock
        print("""
            You chose: 🦎
            CPU chose: 🖖
            You Won!
            """)
        player += 1
    elif player_1 == 5 and computer_1 == 3: # spock beats scissors
        print("""
            You chose: 🖖
            CPU chose: ✌️
            You Won!
            """)
        player += 1
    elif player_1 == 5 and computer_1 == 1: # spock beats rock
        print("""
            You chose: 🖖
            CPU chose: ✊
            You Won!
            """)
        player += 1
    else: 
        print("You Lost") 
        computer += 1
        
print(f"""
      
      The Computer Scored: {computer}
      The Player Scored : {player}
      
      """)

if computer > player:
    print("==========================")
    print("\tComputer Wins")
    print("==========================")
elif computer == player:
    print("==========================")
    print("\tIts a Tie 🤝")
    print("==========================")
else:
    print("==========================")
    print("\tPlayer Wins")
    print("==========================")
        




