class Person(object): #defines a person class. defines what data and functions your person will have when you create it


    def __init__(self, name, age, eyes): # new funtion to configure any person you create with the data that it needs
        self.name = name
        self.age = age
        self.eyes = eyes
    # here we have assigned each name, age and eyes to self. 
    
    def talk(self, words): # new talk function. takes self, and words arguments 
        print(f"I am {self.name} and {words}")

becky = Person("Becky", 39, "green") # we have created an >>>>object named becky using the person >>>>constructor. 
# this turns the class "person" to a constructor function 
becky.talk("I am talking here!") # calling the becky function 

print(becky.__dict__) 
print(becky.__class__) # the class that becky comes from
print(becky.__class__.__dict__) # contents of the class
print(dir(becky)) # a list of strings for everything 

# these 2 lines below do the same thing 
print(becky.talk) 
print(getattr(becky, 'talk'))

# class version of talk
print(becky.__class__.__dict__['talk']) 







