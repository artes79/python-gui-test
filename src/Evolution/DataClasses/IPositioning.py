import numpy as np
from Evolution.DataClasses.IWorldData import IWorldData


class IPositioning:

    @property
    def x(self) -> float:
        pass

    @property
    def xRound(self) -> int:
        pass

    @property
    def y(self) -> float:
        pass

    @property
    def yRound(self) -> float:
        pass

    @staticmethod
    def SetWorld(world: IWorldData) -> None:
        pass

    @staticmethod
    def GetWorld() -> IWorldData:
        pass

    @property
    def position(self) -> np.ndarray:
        pass

    @position.setter
    def position(self, position: np.ndarray) -> None:
        pass

    @property
    def previousPosition(self) -> np.ndarray:
        pass

    def SetRandomPosition(self) -> None:
        pass
