from Classes.Model.Living import *
from DataStorageClasses import *


class Gress(Plant):

    #def __init__(self, positioning: Positioning,
    #             spatialProperties: SpatialProperties):
    def __init__(self, args: list):
        super().__init__(args[0], args[1])

