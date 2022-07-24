from Classes.Model.Living import *


class Plant(Living):

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        super().__init__(positioning, spatialProperties)
