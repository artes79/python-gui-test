import numpy as np


class IWorldData:

    @property
    def size(self) -> np.ndarray:
        pass

    @size.setter
    def size(self, size: np.ndarray) -> None:
        pass

    @property
    def width(self) -> int:
        pass

    @property
    def height(self) -> int:
        pass