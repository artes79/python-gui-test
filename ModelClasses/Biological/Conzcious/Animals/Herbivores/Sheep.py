from ModelClasses.Biological.Conzcious.Animals.Herbivore import Herbivore
from ModelClasses.Biological.Conzcious.Animals.Herbivores.ISheep import ISheep


class Sheep(Herbivore, ISheep):

    def __init__(self):
        super.__init__()
