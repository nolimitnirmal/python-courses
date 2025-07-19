from sys import exit # imports exit funcction from the system module 
from random import randint # imports randint function from the random module 
from ex47_dialogue import DIALOGUE # imports DIALOGUE DICT FROM ex47_dialogue 

class Scene(object): # create scene class (is-a object)

    def enter(self):  # self is the current instance of the class 
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")


class Engine(object): # creating a class called engine, this will run the whole game 
    def __init__(self, scene_map): #function runs when the engine is created 
        self.scene_map = scene_map # stores the map of scenes so it can be used later 

    def play(self): # the main function that starts and controles the game 
        current_scene = self.scene_map.opening_scene() # asks what is the first scene, and stores it as a variable 
        last_scene = self.scene_map.next_scene('finished') # # asks what is the scene called 'finished' and stores it as a last scene 

        while current_scene != last_scene: # "while current scene is not last scene" this is a loop that keeps going while at the last scene 
            next_scene_name = current_scene.enter() # enter function runs on the current scene. returns the name of the next scene  
            current_scene = self.scene_map.next_scene(next_scene_name) # "Get the next scene from the scene map using its name, and make it the new current scene."


        current_scene.enter()


class Death(Scene): # creates a death class inherits from scene 

    quips = [ # lists funny lines for the game 
        "You died.  You kinda suck at this.",
         "Your Mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this.",
         "You're worse than your Dad's jokes."

    ]

    def enter(self): # new method 
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

# randint(0, len(self.quips)-1) gives a random index.
# Death.quips[...] picks a random death message from the list.
# print(...) displays it.

# class Finished(Scene): # new scene in the game, inherits the base class 'scene '
    
# class EscapePod(Scene): # new scene in the game, inherits the base class 'scene '

# class TheBridge(Scene): # new scene in the game, inherits the base class 'scene '

# class LaserWeaponArmory(Scene): # new scene in the game, inherits the base class 'scene '

class CentralCorridor(Scene): # new scene in the game, inherits the base class 'scene '

    def enter(self): # method runs when the player enters the scene.
        print(DIALOGUE["CentralCorridor_enter"]) # prints dialogue from the exported file 

        action = input("> ") # game pauses and waits for players input 

        if action == "shoot!": # if input is death 
            print(DIALOGUE["CentralCorridor_shoot"]) # prints this dialogue 
            return 'death' # returns 'death' whoch will load the death scene 

        elif action == "dodge!": 
            print(DIALOGUE["CentralCorridor_dodge"])
            return 'death'

        elif action == "tell a joke":
            print(DIALOGUE["CentralCorridor_joke"])
            return 'laser_weapon_armory' # advances to laser_weapon_armory scene 

        else: # anything else 
            print("DOES NOT COMPUTE!") # prints this 
            return 'central_corridor'
        
class Map(object): # this class knows all the scenes. starts the game at the correct place. tells the engine what scene comes next 

# first is a dictionary with all the scenes. 
    scenes = { 
        'central_corridor': CentralCorridor(),
        # 'laser_weapon_armory': LaserWeaponArmory(),
        # 'the_bridge': TheBridge(),
        # 'escape_pod': EscapePod(),
        # 'death': Death(),
        # 'finished': Finished(),
    }

    def __init__(self, start_scene): # when you make the map you create a start scene so it knows where to start 
        self.start_scene = start_scene 

    def next_scene(self, scene_name): # this methos gets the next scene. by passing the names of the scene you can pull it up
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self): # opens start scene 
        return self.next_scene(self.start_scene)
    
# This class knows all the scenes in your game.
# It can give you any scene by name.
# It remembers where the game should start.

a_map = Map('central_corridor') # creates mao for the game, tells the map to start the game at central_corridor 
a_game = Engine(a_map) # creates a game angine and gives it a map
a_game.play() # this is what starts the game