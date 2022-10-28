from ModelClasses.Biological.Conzcious.Animal import Animal
from ModelClasses.Biological.Conzcious.Animals.IPredator import IPredator


class Predator(Animal, IPredator):

    def __init__(self):
        super.__init__()

