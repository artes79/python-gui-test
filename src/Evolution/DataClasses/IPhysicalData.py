import numpy as np


class IPhysicalData:

    @property
    def extent(self) -> np.ndarray:
        pass

    @extent.setter
    def extent(self, extent: np.ndarray) -> None:
        pass