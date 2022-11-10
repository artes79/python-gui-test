from ModelClasses.Biological.Conscious import Conscious
from ModelClasses.Biological.Conzcious.IHuman import IHuman


class Human(Conscious, IHuman):

    def __init__(self):
        super().__init__()

