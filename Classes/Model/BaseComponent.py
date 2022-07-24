from Classes import *
from Dataclasses import *
from Interface import *


class BaseComponent(ISpatial, IExecutableEntity, IDrawableEntity, ICommunity):

    lastIdNumber = 0


    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        self.id: str = BaseComponent.generateId()
        self.positioning = positioning
        self.spatialProperties = spatialProperties
        self.drawnStatus = EntityStatus.NEW

    @staticmethod
    def generateId(type):
        BaseComponent.lastIdNumber += 1
        id = type + str(BaseComponent.lastIdNumber)
        return id
