from Classes.Model.Living import *
from Interface import *


class Animal(Living, IBreeding, IMoving, IEat):

    def __init__(self, name, pos, orientation):
        self.name = name
        self.pos = pos
        self.orientation = orientation

    def inAreaOfAttention(self, pos):
        return 1.0

    def eating(self, duration):
        pass

    def moving(self, duration, speed: MovingSpeed):
        pass

    @classmethod
    def breed(cls):
        pass


