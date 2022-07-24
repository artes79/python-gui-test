from Classes.Model.Living import *
from Interface import *


class Animal(Living, IBreeding, IMoving, IEat, IAwareness):

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        super().__init__(positioning, spatialProperties)

    def inAreaOfAttention(self, pos):
        return 1.0

    def eating(self, duration):
        pass

    def moving(self, duration, speed: MovingSpeed):
        pass

    def inView(self) -> [BaseComponent]:
        x: BaseComponent = self
        return [x]

    @classmethod
    def breed(cls):
        pass


