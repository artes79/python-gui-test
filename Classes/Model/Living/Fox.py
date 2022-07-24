from Classes import *


class Fox(Predator, IBreedable):

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        super().__init__(positioning, spatialProperties)
