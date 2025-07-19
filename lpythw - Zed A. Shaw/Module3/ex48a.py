class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass # you use pass to create an empty block. nothing to define it 

dad = Parent()
son = Child()

dad.implicit()
son.implicit() #Even though you dont have a child method/function defined. it still worked