from __future__ import annotations
from Classes import *
from DataStorageClasses import *
from Interface import *
from Enums import *
import math


class BaseComponent(ISpatial, IExecutableEntity, IDrawableEntity, ICommunity):

    entitySet = set()
    lastIdNumber: int = 0

    gameBoard = {
        "width": 640,
        "height": 480,
    }

    id: str
    drawnStatus: EntityStatus
    positioning: Positioning
    spatialProperties: SpatialProperties

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        self.id: str = BaseComponent.generateId()
        self.positioning = positioning
        self.spatialProperties = spatialProperties
        self.drawnStatus = EntityStatus.NEW

    @staticmethod
    def generateId():
        BaseComponent.lastIdNumber += 1
        return str(BaseComponent.lastIdNumber)

    @staticmethod
    def addToEntitySet(entity):
        BaseComponent.entitySet.add(entity)

    @staticmethod
    def calculateNextStep():
        for entity in BaseComponent.entitySet:
            if isinstance(entity, IExecutableEntity):
                entity.executeStep()

    def executeStep(self):
        pass

    def calculateDistanceTo(self, entity: BaseComponent):
        d = BaseComponent.distance(
            self.positioning.x,
            self.positioning.y,
            entity.positioning.x,
            entity.positioning.y
        )
        return d - (
                self.spatialProperties.radius +
                entity.spatialProperties.radius
        )

    @staticmethod
    def distance(x1: float, y1: float, x2: float, y2: float):
        q1 = pow(abs(y2-y1), 2)
        q2 = pow(abs(x2-x1), 2)
        return math.sqrt(q1+q2)

    def removeEntity(self):
        self.drawnStatus = EntityStatus.TO_BE_DELETED

    def toString(self):
        pass
