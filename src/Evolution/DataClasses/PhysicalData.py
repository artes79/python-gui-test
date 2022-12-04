import numpy as np
from Evolution.DataClasses.IPhysicalData import IPhysicalData


class PhysicalData(IPhysicalData):

    _extent: np.ndarray = np.array([1, 1], dtype=float)

    @property
    def extent(self) -> np.ndarray:
        return self._extent

    @extent.setter
    def extent(self, extent: np.ndarray) -> None:
        self._extent = extent