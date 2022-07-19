from Classes.Model.Animals import *


class Animal(Living):

    def __init__(self, name, pos, orientation):
        self.name = name
        self.pos = pos
        self.orientation = orientation
