print("Welcome to the quiz game!")

playing = input("Would you like to continue? : ")

correct = 0

attempts_q1 = 0
attempts_q2 = 0
attempts_q3 = 0

if playing != "yes":
    print("ok nvm")
    quit()

while True:
    attempts_q1 += 1 
    question1 = input("Who is the striker for arsenal?").lower().strip()
    if question1 == "gyokores":
        print("Well done, we are winnning the treble!")
        correct += 1
        break
    else: 
        print("Try again")
        continue
    
    
while True:
    attempts_q2 += 1 
    question1 = input("Who is the LW for arsenal?").lower().strip()
    if question1 == "rodrygo":
        print("Well done, we are winnning the treble!")
        correct += 1
        break
    else: 
        print("Try again")
        continue
    
    
while True:
    attempts_q3 += 1 
    question1 = input("Who is the RW for arsenal?").lower().strip()
    if question1 == "saka":
        print("Well done, we are winnning the treble!")
        correct += 1
        break
    else: 
        print("Try again")
        continue
    
    
print(f"You got {correct} questions correct")
print(f" That is {((correct/3)*100)}%")

def attempts(n):
    return "attempt" if n == 1 else "attempts"

print(f"It took you {attempts_q1} {attempts(attempts_q1)} to solve question 1 ")

print(f"It took you {attempts_q2} {attempts(attempts_q2)} to solve question 1 ")

print(f"It took you {attempts_q3} {attempts(attempts_q3)} to solve question 1 ")



