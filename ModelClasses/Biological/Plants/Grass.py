from ModelClasses.Biological.Plant import Plant
from ModelClasses.Biological.Plants.IGrass import IGrass


class Grass(Plant, IGrass):

    def __init__(self):
        super.__init__()

