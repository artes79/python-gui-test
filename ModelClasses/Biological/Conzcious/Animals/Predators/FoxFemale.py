from ModelClasses.Biological.Conzcious.Animals.Predators.Fox import Fox
from ModelClasses.Biological.Conzcious.Animals.Predators.IFoxFemale import IFoxFemale


class FoxFemale(Fox, IFoxFemale):

    def __init__(self):
        super.__init__()
