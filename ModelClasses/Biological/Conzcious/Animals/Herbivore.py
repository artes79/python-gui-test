from ModelClasses.Biological.Conzcious.Animal import Animal
from ModelClasses.Biological.Conzcious.Animals.IHerbivore import IHerbivore


class Herbivore(Animal, IHerbivore):

    def __init__(self):
        super().__init__()

