from Evolution.DataClasses.IPositioning import IPositioning
from dataclasses import dataclass
import numpy as np


@dataclass
class Positioning(IPositioning):

    _curentCoord: np.ndarray = np.array([0, 0], dtype=float)

    @property
    def x(self) -> float:
        return self._curentCoord[0]

    @property
    def xRound(self) -> float:
        return np.round(self._curentCoord[0])

    @property
    def y(self) -> float:
        return self._curentCoord[1]

    @property
    def yRound(self) -> float:
        return np.round(self._curentCoord[1])