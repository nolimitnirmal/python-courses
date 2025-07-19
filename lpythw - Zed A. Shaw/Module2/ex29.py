import code
from dis import dis

people = 20 
cats = 30
dogs = 15

if people < cats:
  print("Too mamnu cats! The World is doomed!")

if people > cats:
  print("Not many cats! The world is saved!")

if people < dogs:
  print("The world is droole on!")

if people > dogs:
  print("The world is dry")

dogs += 5 # dogs = dogs + 5

if people <= dogs:
  print("People are greater than or equal to dogs.")

if people <= dogs:
  print("People are less than or equal to dogs.")

if people == dogs:
  print("People are dogs.")

compiled = compile(code, '<string>', 'exec')
dis.dis(compiled)

