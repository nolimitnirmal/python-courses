class Parent(object): #Class

    def override(self): #METHOD
        print("PARENT override()")

    def implicit(self): #METHOD
        print ("PARENT implicit()")

    def altered(self): #METHOD
        print("PARENT altered")

class Child(Parent): #Class

    def override(self): #METHOD
        print("CHILD override()")
 
    def altered(self): #METHOD
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() # runs altered method from the parent class 
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()



