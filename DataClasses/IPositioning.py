from __future__ import annotations
import numpy as np
from ModelClasses.IEntity import IEntity
from ModelClasses.INeighborhood import INeighborhoodUser


class IPositioning(INeighborhoodUser):

    @property
    def x(self) -> float:
        pass

    @property
    def xAsInt(self) -> float:
        pass

    @property
    def y(self) -> float:
        pass

    @property
    def yAsInt(self) -> float:
        pass

    @property
    def orientation(self) -> float:
        pass

    def moveInDirection(self, direction: np.ndarray, duration: float, speed: float, maxDistance: float) -> None:
        pass

    def distanceTo(self, entity: IPositioning) -> float:
        pass

    def closeBy(self, entities: list[type[IEntity]], distance: float) -> list[type[IEntity]]:
        pass



