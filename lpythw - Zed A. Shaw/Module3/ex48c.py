# Alter before or after 

class Parent(object): #defines a parent class
 
   def altered(self): # defines a method called altered. just prints a message 
        print("PARENT altered()")


class Child(Parent): # creates a Child Class inherent to Parent Class

    def altered(self): # new method called altered, overrides the parent method 
        print("Child, BEFORE PARENT altered()") # prints one string 
        super(Child, self).altered() # says 'go to the Parent class and then run the altered method
        print("CHILD, AFTER PARENT altered()") # prints another string 

dad = Parent() # dad instance of parent class 
son = Child()

dad.altered()
son.altered()

# the child class overrides the altered method from the parent class 
# we can still use the super() function to run the parent altered() METHOD

