from Evolution.DataClasses.IPositioning import IPositioning
from Evolution.DataClasses.WorldData import WorldData
from Evolution.DataClasses.PhysicalData import PhysicalData
from dataclasses import dataclass
from random import random
import numpy as np


@dataclass
class Positioning(IPositioning):

    _world: WorldData = WorldData()
    _physical: PhysicalData = PhysicalData()
    _curentPosition: np.ndarray = np.array([0, 0], dtype=float)
    _previusPosition: np.ndarray = np.array([0, 0], dtype=float)

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

    @property
    def physical(self) -> PhysicalData:
        return self._physical

    @property
    def position(self) -> np.ndarray:
        return self._curentPosition

    @position.setter
    def position(self, position: np.ndarray) -> None:
        self._previusPosition = self._curentPosition
        self._curentPosition = position

    @property
    def previousPosition(self) -> np.ndarray:
        return self._previusPosition

    def SetRandomPosition(self) -> None:
        x = random() * Positioning._world.width
        y = random() * Positioning._world.height
        self.position = np.array([x, y], dtype=float)