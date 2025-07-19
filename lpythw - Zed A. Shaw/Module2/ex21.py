# the 4 functions below define a math function 
# introduces the return at the end of each function 
# Return sends the value back to when the function was called. 

def add(a, b): # each function is called with 2 arguments 
  print(f"ADDING {a} + {b}") # standard print 
  return a + b # adds a and b and sends it back to where it was called in the script. 
# if you called the function when setting a variable. itll be returned to that variable at that point in the script. 
# when using the variable later on, it will use the returned value. 

def subtract(a, b):
  print(f"SUBTRACTING {a} - {b}")
  return a - b

def multiply(a, b):
  print(f"MULTIPLY {a} * {b}")
  return a * b

def divide(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b

print("Let's do some math with just functions!")

age = add(30, 5) # by using the return it gives the sume back to a + b. 
# so now from the line above, whenever you use the variable "age" it will be the sum of 30 + 5. which is 35 
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes:", what, "Can you do it by hand?")