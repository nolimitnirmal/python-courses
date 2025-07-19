from ex50 import Person # imports Person class from ex50

def test_combat(): # test created 2 characters 
    boxer = Person("Boxer", 100, 10) 
    zombie = Person("Zed", 1000, 1000)

    assert boxer.hp == 100, "Boxer has wrong hp." # checking if health is correct
    assert zombie.hp == 1000, "Zombie has wrong hp."

    boxer.hit(zombie) # boxer hits zombie, will run the method in ex50. 
    assert zombie.alive(), "Zombie should be alive." # zonbie health goes down by ten. 
    # hp goes from 1000>990 after getting hit 
    # 990 > 0 so it is true 

    zombie.hit(boxer) # boxer hits zombie. 
    assert not boxer.alive(), "Boxer should be dead." # boxer health goes from 100 > -900
    # -900 < 0 so true. Boxer is not alive 


    

