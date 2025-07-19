
from sys import exit

def start():
  print("""
        You are through on goal in the World Cup with the final CB chasing you down very close. 

        You can shoose to do one skill to get your opponent off you amd get a clear shot on goal 

        Which Skill are you going to do?
        \t a. Step Over
        \t b. Flip Flap 
        \t c. Shot Fake

        """)
  choice = input("> ")
  
  if choice == "a":
    step_over()
  elif choice == "b":
    flip_flip()
  elif choice == "c":
    shot_fake()


  
def dead(why):
  print(why, "Well Done")
  exit(0)
  
def flip_flip():
  print("You have decided to do the worst possible thing when youre through on goal with a defender behind you.")
  print("You just lost the WC Final")
  dead("Poor decision")

def step_over():
  print("The defender has fallen for the step over and commired a tackle.")
  print("You have won a freekick, potentially a chance that could win you the World Cup")

def shot_fake():
  print("You send the defender to the shops")
  print("Then you go ahead and bury the shot bottom right.")
  print("IT'S COMING HOME")

  
start()
