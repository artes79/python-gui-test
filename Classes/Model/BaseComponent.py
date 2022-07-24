from Classes import *
from Dataclasses import *
from Interface import *
from Enums import *


class BaseComponent(ISpatial, IExecutableEntity, IDrawableEntity, ICommunity):

    entitySet = set()
    lastIdNumber: int = 0

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

    def removeEntity(self):
        self.drawnStatus = EntityStatus.TO_BE_DELETED

