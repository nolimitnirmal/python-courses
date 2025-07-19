
from sys import exit # this imports an exit function from the sys module. 
# used to immediately end the program when called. 

def gold_room(): #defines a new function gold_room. 
  print("This room is full of gold.  How much do you take?") #prints message to player 
  choice = int(input(">")) # takes input from player. stores input as variable "choce"
  if "0" in choice or "1" in choice: # if input has a 0 or a 1
    how_much = int(choice) # convert to integer if above is true. stores value in variable how_much
  else: # if 1 or 0 is not in the input. dead function is called. 
    dead("Man, learn to type a number")
  if how_much < 50:
    print("Nice, you're not greedy, you win!")
    exit(0) 
  else: 
    dead("You greedy bastard!")


def bear_room(): # defines bear_room function. represents a room in the game with a bear. 
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")
  print("How are you going to move the bear?")
  bear_moved = False # a boolean variable is initialzed to False 
  
  while True: # while loop is created and a condition is given. will loop as long as condition is true
    choice = input("> ") # stores input as variable 'choice'

    if choice == "take honey": # if player tyoes 'take honey' calls dead function
      dead("The bear looks you and slaps your face off")
    elif choice == "taunt bear" and not bear_moved: #if input is taunt bear and bear has not moved. the bear will move away from the door
      print("The bear has moved from the door")
      print("You can go through it now")
      bear_moved = True # acknoledges and changes variable to bear_moved to be true at the end
    elif choice == "taunt bear" and bear_moved: # if player says taint bear and bear has moved, calls dead function
      dead("The bear gets pissed off and chews your leg off.")
    elif choice == "open door"  and bear_moved: # if bear has moved and player chooses open door. it takes them to the gold_room
      gold_room()
    else: # if player puts something in the input anything other than the previous options. 
      print("I got no idea what that means") # prints message

def cthulhu_room(): # defines cthulu room function. 
  print("Here you see the great evil Cthulhu.")
  print("He, it, whatever stares at you and you go insane.")
  print("Do you flee for your life or eat your head?")

  choice = input("> ") # takes input from user and stores it as choice 

  if "flee" in choice: # if input has 'flee' call the strat function
    start()
  elif "head" in choice: # if 'head' is in input, call dead function
    dead("Well that was tasty!")
  else: # if nothing mentioned above is in input, print message 
    print("I don't understand.")

def dead(why): # this is a custom function. displays a message when the player is dead
  print(why, "Good job!")
  exit(0) # calls exit funtions 

def start(): # defines start function
  print("You are in a dark room.")
  print("There is a door to you right and left")
  print("Which one do you take?")

  choice = input("> ") # gets input from user and stores variable as choice

  if choice == "left": # if input is left, calls bear_room function
    bear_room()  
  elif choice == "right": #if choice is right, calls cthulu_room function
    cthulhu_room()
  else: # if choice is neither left or right, calls dead function. 
    dead("You stumble around the room until you starve.") 


start() # this calls the start function, which starts the game. 


"""
Summary 

The code starts with the start functio, asking the player to go left or right. 

if they choose left, it calls the bear_room function, which takes the player to the bear room. 

BEAR ROOM 
1. prints message
  starts a while loop. Loops with condition, if bear moved is true
2. asks for input 
3. some input calls dead funtioon, 
4. one input calls for the gold_room function
5. else function >> prints a message 

FROM BEAR ROOM TO GOLD ROOM
if the gold_room function is called. 
1. it prints a message and asks user for input and stores it as a variable. 
2. depending on the input
  a. calls end function
  b. prints a message for the user. 

CTHULU ROOM 
1. when called prints some strings and asks for input 
2. stores input as a variable
3. if answer has the word flee
  it will call the start function, this will take them back to the beginning of the game 
4 if input has the word 'head'
  it will call the dead function
5. anything other than this itll call the function for cthulu_room
  this would just loop the player back into the Cthulu Room.

"""