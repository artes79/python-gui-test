from Classes.Model.Living import *


class Animal(Living, IBreeding):

    def __init__(self, name, pos, orientation):
        self.name = name
        self.pos = pos
        self.orientation = orientation

    def calculateDistance(self,  animalArray ):
        for animal in animalArray:
            pos = animal.pos

    def inAreaOfAttention(self, pos):
        return 1.0

    def toString(self):
        return self.name

    @classmethod
    def breed(cls):
        pass


