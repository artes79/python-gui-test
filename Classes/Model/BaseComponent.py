from Classes import *
from Dataclasses import *
from Interface import *


class BaseComponent(ISpatial, IExecutableEntity, IDrawableEntity, ICommunity):

    entitySet = set()
    lastIdNumber: int = 0


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

    def removeEntity(self):
        self.drawnStatus = EntityStatus.TO_BE_DELETED

