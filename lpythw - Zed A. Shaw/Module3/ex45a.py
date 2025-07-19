# class person(object): # defining a class name 
#     def __init__(self, name, age, eyes): # METHOD
#         self.name = name
#         self.age = age
#         self.eyes = eyes

#     def talk(self, words): # talk function using self and words as args 
#         print(f"I am {self.name} and {words}") # words is the string passed


# people = [] # create and empty list that you store 1000 people in 

# for i in range(1000): # run 1000 times with 1 from 0-999
#     name = f"person_{i}" #. makes a unique name person_1, person_2 etc 
#     age = i % 100 # 
#     eyes = "blue" if i % 2 == 0 else "brown"
#     Person = person(name, age, eyes) # stores person name 
#     people.append(person) # adds to list 

class Person(object):
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes

    def talk(self, words):
        print(f"I am {self.name} and {words}")

# Create 1000 Person objects and store them in a list
people = []

for i in range(1000):
    name = f"Person_{i}"
    age = i % 100  # cycle through ages 0–99
    eyes = "blue" if i % 2 == 0 else "brown"  # alternate eye color
    person = Person(name, age, eyes)
    people.append(person)

# Optional: Have the first 5 people talk
for person in people[:5]:
    person.talk("I'm one of the thousand!")




print(people)


