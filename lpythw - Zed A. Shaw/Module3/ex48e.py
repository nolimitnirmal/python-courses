# Composition is when you use another class inside a class instead of inheritance

class Other(object): #define a new class Other 

    def override(self): #METHOD
        print("OTHER override()")

    def implicit(self): #method
        print("OTHER implicit()")

    def altered(self): #method 
        print("OTHER altered()")

class Child(object):

    def __init__(self): #METHOD 
        self.other = Other() # Other object is stored in self.other 

    def implicit(self): #METHOD
        self.other.implicit() # calls implicit method on the other object 

    def override(self): #METHOD
        print("CHILD override") #Prints string     

    def altered(self): #METHOD
        print("CHILD, BEFORE OTHER altered()") 
        self.other.altered() # Calls altered method from the other object
        print("CHILD, AFTER OTHER altered()")

son = Child() # instance or object for Child class 

# Other object was created earlier 

son.implicit() # calls implicit method on son instance 
son.override() # 
son.altered()

# the object for the Other Class was created inside the Child class