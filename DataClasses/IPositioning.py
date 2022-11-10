from __future__ import annotations
from dataclasses import dataclass
import numpy as np


class INeighborhoodUser:

    @property
    def neighborhoodSquar(self) -> (int, int):
        pass

    @neighborhoodSquar.setter
    def neighborhoodSquar(self, value: (int, int)) -> None:
        pass

@dataclass
class IPositioning(INeighborhoodUser):

    @property
    def x(self) -> float:
        pass

    @property
    def xAsInt(self) -> int:
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

    def moveInDirection(self, direction: float, duration: float, speed: float, maxDistance: float) -> None:
        pass

    def distanceTo(self, entity: IPositioning) -> float:
        pass

    def closeBy(self, entities: list[type[IPositioningUser]], distance: float) -> list[type[IPositioningUser]]:  #list[type[IEntity]]
        pass

    def changeWorldBorder(self, width: int, height: int) -> None:
        pass


class IPositioningUser:

    @property
    def position(self) -> IPositioning:
        pass





