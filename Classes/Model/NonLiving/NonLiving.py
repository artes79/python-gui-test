from Classes.Model.BaseComponent import *


class NonLiving(BaseComponent, IImmortal):

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        super().__init__(positioning, spatialProperties)

