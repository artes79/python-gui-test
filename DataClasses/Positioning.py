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

    def __init__(self, x: int, y: int,
                 boundingBox: (int, int),
                 movable: bool = True):
        self._coord = np.array([x, y], dtype=float)
        self._boundingBoxWidth = boundingBox[0]
        self._boundingBoxHeight = boundingBox[1]
        self._movable = movable
        self._orientation = random.randint(0, 359)


    def closestBorderDistance(self) -> (float, float):
        distanceTopBorder = self._coord[1] - self._boundingBoxHeight / 2
        distanceBottomBorder = self._worldHeight - self._coord[1] - self._boundingBoxHeight / 2
        distanceLeftBorder = self._coord[0] - self._boundingBoxWidth / 2
        distanceRightBorder = self._worldWidth - self._coord[0] - self._boundingBoxWidth / 2

        direction = (0 - self._orientation) % 360
        distance = distanceTopBorder

        if distanceRightBorder < distance:
            direction = (90 - self._orientation) % 360
            distance = distanceRightBorder
        if distanceBottomBorder < distance:
            direction = (180 - self._orientation) % 360
            distance = distanceBottomBorder
        if distanceLeftBorder < distance:
            direction = (270 - self._orientation) % 360
            distance = distanceLeftBorder

        if direction > 180:
            direction -= 360

        return (distance, direction)

    def closestTo(self, entities: list[type[IEntity]]) -> IEntity:
        closestEntity: IEntity = entities[0]
        closestDistance: float = self._worldWidth + self._worldHeight
        for entity in entities:
            distance = self.distanceTo(entity.position)
            if closestDistance > distance:
                closestDistance = distance
                closestEntity = entity
        return closestEntity

    def closeBy(self, entities: list[type[IEntity]], radius: float) -> list[type[IEntity]]:
        closeBy = []
        for entity in entities:
            distance = self.distanceTo(entity.position)
            if distance < radius:
                closeBy.append(entity)
        return closeBy

    def worldSizeHasChange(self) -> None:
        self._coord[0] += Positioning._lastWidthDiff / 2
        self._coord[1] += Positioning._lastHeightDiff / 2

    def setRandomPosition(self, step: int, entities: list[type[IEntity]] = []) -> None:
        findCoords = True
        while findCoords:
            self._coord[0] = float(random.randrange(0, Positioning._worldWidth, step))
            self._coord[1] = float(random.randrange(0, Positioning._worldHeight, step))
            overlap = self.closeBy(entities, 7)
            if len(overlap) == 0:
                findCoords = False
