print("Welcome to the computer quiz!")

playing = input("Do you want to play? > ")
if playing.lower() != "yes":
    quit()

print("Let's Play") 

score = 0
q1_attempts = 0
q2_attempts = 0
q3_attempts = 0
q4_attempts = 0

while True:
    q1_attempts += 1 
    answer = input("What does CPU stand for?").strip()
    if answer.lower() == "central processing unit": 
        print("Correct!")
        score += 1
        break 
    else: 
        print("Incorrect, Try again")
        continue
        

while True:
    q2_attempts += 1
    answer = input("What does GPU stand for?").strip()
    if answer.lower() == "graphics processing unit": 
        print("Correct!")
        score += 1
        break 
    else: 
        print("Incorrect, Try again")
        continue



while True:
    q3_attempts += 1
    answer = input("What does RAM stand for?").lower().strip()
    if answer == "random access memory": 
        print("Correct!")
        score += 1
        break 
    else: 
        print("Incorrect, Try again")
        continue


while True:
    q4_attempts += 1
    answer = input("What does PSU stand for?").lower().strip()
    if answer == "power supply": 
        print("Correct!")
        score += 1
        break
    else: 
        print("Incorrect, Try again")
        continue
    
    
print("\t")
print(f"You got {score} questions correct!\t") 
print("\t")
print(f"You got {(score/4)*100}%!")
print("\t")

def attempt_word(n):
    return "attemp" if n == 1 else "attempts"
    
print(f"It took you {q1_attempts} {attempt_word(q1_attempts)} to solve question 1 ")
print(f"It took you {q2_attempts} {attempt_word(q1_attempts)} to solve question 2 ")
print(f"It took you {q3_attempts} {attempt_word(q1_attempts)} to solve question 3 ")
print(f"It took you {q4_attempts} {attempt_word(q1_attempts)} to solve question 4 ")








