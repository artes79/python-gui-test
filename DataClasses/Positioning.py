import math
import random
from dataclasses import dataclass
import numpy as np
from DataClasses.IPositioning import IPositioning
from ModelClasses.IEntity import IEntity


#@dataclass
class Positioning(IPositioning):

    _coord: np.ndarray
    _orientation: float = 0

    _movable: bool

    _boundingBoxWidth: int
    _boundingBoxHeight: int

    _worldWidth: int = 0
    _worldHeight: int = 0
    _lastWidthDiff: int = 0
    _lastHeightDiff: int = 0

    @property
    def coord(self) -> np.ndarray:
        return self._coord

    @property
    def x(self) -> float:
        return self._coord[0]

    @property
    def centerX(self) -> float:
        return self._coord[0]

    @property
    def xAsInt(self) -> int:
        return np.round(self._coord[0])

    @property
    def y(self) -> float:
        return self._coord[1]

    @property
    def centerY(self) -> float:
        return self._coord[1]

    @property
    def yAsInt(self) -> float:
        return np.round(self._coord[1])

    @property
    def orientation(self) -> float:
        return self._orientation

    @staticmethod
    def setWorldSize(width: int, height: int):
        Positioning._lastWidthDiff = width - Positioning._worldWidth
        Positioning._lastHeightDiff = height - Positioning._worldHeight

        Positioning._worldWidth = width
        Positioning._worldHeight = height
