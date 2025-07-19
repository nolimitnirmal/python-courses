class Person: # new class 
    def __init__(self, name, hp, damage): # runs when you create a new class
        self.name  = name # instace variables or attributes 
        self.hp = hp # instace variables or attributes 
        self.damage = damage # instace variables or attributes 

# __init__ is a special method 

    def hit(self, who): # method called hit. self doing the hitting like the boxer. who is the object being hit  
        who.hp -= self.damage # take objects damage and subtract from other persons health 
        # above line is the same as: 
            # who.hp = who.hp - self.damage
            # who is the person getting hit 
            # self it doing the hitting 


    def alive(self): # alive method 
        return self.hp > 0 # health of the object is more than zero
    
    
