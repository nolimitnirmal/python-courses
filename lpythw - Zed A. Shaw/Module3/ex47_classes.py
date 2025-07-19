class Scene(object): 

    def enter(self):
        pass


class Engine(object): # you are creating a new class called engine 
# has 2 parts 
    def __init__(self, scene_map): # this is a constructor, will run when yo create the engine. scene_map is passed into the engine. 
        pass

    def play(self):
        pass

class Death(Scene): # created a new death class, which inherits from the scenee class. Scene is the blueprint foe the whole game, death is one of them. 

    def enter(self): # defining a function called enter. this is where you show what happened by displaying a message.
        pass # use pass to do nothing for now, fill up code later 

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()