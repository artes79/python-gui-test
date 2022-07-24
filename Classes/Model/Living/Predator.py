from Classes.Model.Living import *


class Predator(Animal):

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        super().__init__(positioning, spatialProperties)

