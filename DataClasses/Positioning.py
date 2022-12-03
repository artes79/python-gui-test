import math
import random
from dataclasses import dataclass
import numpy as np
from DataClasses.IPositioning import IPositioning
from ModelClasses.IEntity import IEntity


#@dataclass
class Positioning(IPositioning):

    _curentCoord: np.ndarray
    _previousCoord: np.ndarray
    _orientation: float = 0

    _movable: bool

    _boundingBoxHalfWidth: int
    _boundingBoxHalfHeight: int

    _worldWidth: int = 0
    _worldHeight: int = 0
    _lastWidthDiff: int = 0
    _lastHeightDiff: int = 0

    @property
    def coord(self) -> np.ndarray:
        return self._curentCoord

    @property
    def x(self) -> float:
        return self._curentCoord[0]

    @property
    def centerX(self) -> float:
        return self._curentCoord[0]

    @property
    def xAsInt(self) -> int:
        return np.round(self._curentCoord[0])

    @property
    def previousX(self) -> float:
        return self._previousCoord[0]

    @property
    def y(self) -> float:
        return self._curentCoord[1]

    @property
    def centerY(self) -> float:
        return self._curentCoord[1]

    @property
    def yAsInt(self) -> float:
        return np.round(self._curentCoord[1])

    @property
    def previousY(self) -> float:
        return self._previousCoord[1]

    @property
    def orientation(self) -> float:
        return self._orientation

    @property
    def halfBoundingBox(self) -> (int, int):
        return self._boundingBoxHalfWidth, self._boundingBoxHalfHeight

    @staticmethod
    def setWorldSize(width: int, height: int):
        Positioning._lastWidthDiff = width - Positioning._worldWidth
        Positioning._lastHeightDiff = height - Positioning._worldHeight

        Positioning._worldWidth = width
        Positioning._worldHeight = height

    def __init__(self, x: int, y: int,
                 boundingBox: (int, int),
                 movable: bool = True):
        self._curentCoord = np.array([x, y], dtype=float)
        self._boundingBoxHalfWidth = boundingBox[0] / 2
        self._boundingBoxHalfHeight = boundingBox[1] / 2
        self._movable = movable
        self._orientation = random.randint(0, 359)

    def moveInDirection(self, direction: float, duration: float, speed: float, maxDistance: float) -> None:
        if self._movable:

            distanceBorder, direction = self.closestBorderDistance();

            direction = (direction / np.abs(direction)) / 10

            self._orientation = (self._orientation + direction) % 360

            speed = min(abs(distanceBorder/3), speed)
            distance = duration * speed;
            distanceX = distance * np.cos(self._orientation);
            distanceY = distance * np.sin(self._orientation);
            if distance >= distanceBorder:
                distance = distanceBorder * 0.9
            self._curentCoord[0] += distanceX
            self._curentCoord[1] += distanceY

    def closestBorderDistance(self) -> (float, float):
        distanceTopBorder = self._curentCoord[1] - self._boundingBoxHalfHeight
        distanceBottomBorder = self._worldHeight - self._curentCoord[1] - self._boundingBoxHalfHeight
        distanceLeftBorder = self._curentCoord[0] - self._boundingBoxHalfWidth
        distanceRightBorder = self._worldWidth - self._curentCoord[0] - self._boundingBoxHalfWidth

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

        return distance, direction

    def distanceTo(self, entityPos: IPositioning) -> float:

        posA = self.boundingBoxIntersect(self, entityPos)
        posB = self.boundingBoxIntersect(entityPos, self)
        return np.linalg.norm(posA - posB)

    def boundingBoxIntersect(self, entityPosA: IPositioning, entityPosB: IPositioning) -> np.ndarray:
        denominator = (entityPosA.coord[0] - entityPosB.x)
        if denominator < 0.001:
            denominator = 0.001
        sloap = (entityPosA.coord[1] - entityPosB.y) / denominator
        halfWidth, halfHeight = entityPosB.halfBoundingBox

        x = 0
        y = 0

        hitYAxis = sloap * halfWidth
        if -halfHeight <= hitYAxis and hitYAxis <= halfHeight:
            y = entityPosB.y + hitYAxis
            if entityPosA.coord[0] > entityPosB.x:
                x = entityPosB.x + halfWidth
            else:
                x = entityPosB.x - halfWidth
        else:
            x = entityPosB.x + halfHeight / sloap
            if entityPosA.coord[1] > entityPosB.y:
                y = entityPosB.y - halfHeight
            else:
                y = entityPosB.y + halfHeight

        return np.array([x, y], dtype=float)

    def distanceBetween(self, coord: np.ndarray, entityPos: IPositioning) -> float:
        return np.linalg.norm(coord - entityPos.coord)

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
        self._curentCoord[0] += Positioning._lastWidthDiff / 2
        self._curentCoord[1] += Positioning._lastHeightDiff / 2

    def setRandomPosition(self, step: int, entities: list[type[IEntity]] = []) -> None:
        findCoords = True
        while findCoords:
            self._curentCoord[0] = float(random.randrange(0, Positioning._worldWidth - step, step) + step / 2)
            self._curentCoord[1] = float(random.randrange(0, Positioning._worldHeight - step, step) + step / 2)
            overlap = self.closeBy(entities, 7)
            if len(overlap) == 0:
                findCoords = False

    def getOverlaps(self, entities: list[type[IEntity]]) -> None:
        for entity in entities:
            if entity != self:
                distance = self.distanceBetweenBBoxes(entity)
                print(distance)

    def distanceBetweenBBoxes(self, entity: IEntity):
        intersectsB = self.boundingBoxIntersect(self, entity.position)
        intersectsA = self.boundingBoxIntersect(entity.position, self)

        distanceAB = np.linalg.norm(self.coord - entity.position.coord)

        internalDistanceB = np.linalg.norm(intersectsB - entity.position.coord)
        internalDistanceA = np.linalg.norm(intersectsA - self.coord)

        print(distanceAB)

        return distanceAB - internalDistanceA - internalDistanceB


    def setRandomPosition2(self, step: int, entities: list[type[IEntity]]):
        pass

    def coordIsOccupaid(self, coord: np.array, entities: list[type[IEntity]], radius: float) -> bool:
        for entity in entities:
            distance = self.distanceBetween(coord, entity.position)
            if distance < radius:
                return True
        return False

    def placeCloseTo(self, entity: IEntity, entieties: list[type[IEntity]]) -> None:
        freeCoord = []
        numNabours = []

        for x, y in [(15, 0), (15, 15), (0, 15), (-15, 15), (-15, 0), (-15, -15), (0, -15), (15, -15)]:
            coord = np.array([entity.position.x + x, entity.position.y + y])
            if not self.coordIsOccupaid(coord, entieties, 5):
                numN = 0
                for x1, y1 in [(15, 0), (15, 15), (0, 15), (-15, 15), (-15, 0), (-15, -15), (0, -15), (15, -15)]:
                    coord1 = np.array([entity.position.x + x1, entity.position.y + y1])
                    if self.coordIsOccupaid(coord1, entieties, 5):
                        numN += 1
                freeCoord.append(coord)
                numNabours.append(numN)

        mostNIndex = numNabours.index(max(numNabours))
        if len(freeCoord) > 0:
            #pos = random.randint(0, len(freeCoord)-1)
            newCoord = freeCoord[mostNIndex];
            self._curentCoord[0] = newCoord[0]
            self._curentCoord[1] = newCoord[1]



