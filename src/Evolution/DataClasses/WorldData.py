from Evolution.DataClasses.IWorldData import IWorldData
import numpy as np


class WorldData(IWorldData):

    _size: np.ndarray = np.array([200, 200], dtype=float)

    @property
    def size(self) -> np.ndarray:
        return self._size

    @size.setter
    def size(self, size: np.ndarray) -> None:
        self._size = size

    @property
    def width(self) -> int:
        return int(self._size[0])

    @property
    def height(self) -> int:
        return int(self._size[1])