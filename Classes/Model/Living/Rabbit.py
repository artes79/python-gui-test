from Classes import *
from random import random


class Rabbit(Herbivore, IBreedable):

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        super().__init__(positioning, spatialProperties)

    @classmethod
    def breed(cls):
        sex = "she"
        if random() < 0.35:
            sex = "he"
        return cls("Test", [12, 13], "west")