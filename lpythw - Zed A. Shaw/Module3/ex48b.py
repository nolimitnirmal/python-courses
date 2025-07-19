# OVERRIDE EXPLICITLY 

class Parent(object): #CLASS

    def override(self):
        print("PARENT override()")

class Child(Parent): # CLASS 

    def override(self):
        print("CHILD override()")

dad = Parent() # INSTANCE OR OBJECT
son = Child() # INSTANCE OR OBJECT

dad.override() # calls the override method on the dad object
son.override() # calls the override method on the Child object 

# you can override the same function used in child class even though they are defined diferently 
# useful if you want to use the same function but you want it to behave differently in the child class. 
