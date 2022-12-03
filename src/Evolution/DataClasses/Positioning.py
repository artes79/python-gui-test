from Evolution.DataClasses.IPositioning import IPositioning
from Evolution.DataClasses.WorldData import WorldData
from dataclasses import dataclass
import numpy as np


@dataclass
class Positioning(IPositioning):

    _world: WorldData = WorldData()
    _curentPosition: np.ndarray = np.array([0, 0], dtype=float)

    @property
    def x(self) -> float:
        return self._curentPosition[0]

    @property
    def xRound(self) -> float:
        return np.round(self._curentPosition[0])

    @property
    def y(self) -> float:
        return self._curentPosition[1]

    @property
    def yRound(self) -> float:
        return np.round(self._curentPosition[1])

    @staticmethod
    def SetWorld(world: WorldData) -> None:
        Positioning._world = world

    @staticmethod
    def GetWorld() -> WorldData:
        return Positioning._world