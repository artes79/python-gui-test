from random import random
import numpy as np
from Evolution.DataClasses.Positioning import Positioning
from Evolution.DataClasses.IGroundPositioning import IGroundPositioning


class GroundPositioning(Positioning, IGroundPositioning):

    def SetRandomPosition(self) -> None:
        x = np.round(random() * ((Positioning._world.width - self._physical.extent[0] * 2) / (self._physical.extent[0] * 2))) * (self._physical.extent[0] * 2) + self._physical.extent[0]
        y = np.round(random() * ((Positioning._world.height - self._physical.extent[1] * 2) / (self._physical.extent[1] * 2))) * (self._physical.extent[1] * 2) + self._physical.extent[1]
        self.position = np.array([x, y], dtype=float)