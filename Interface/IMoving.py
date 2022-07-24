from Interface.IEnergy import *
from Enums import *


class IMoving(IEnergy):

    def moving(self, duration, speed: MovingSpeed):
        pass
