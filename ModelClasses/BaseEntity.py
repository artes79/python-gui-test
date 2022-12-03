import math

from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage

from DataClasses.Positioning import Positioning
from ModelClasses.IBaseEntity import IBaseEntity
from ModelClasses.IEntity import IEntity


class BaseEntity(IBaseEntity):

    _entityCensus: list[type[IEntity]] = []
    _worldRegions = [[[] for i in range(8)] for j in range(6)]

    _lastIdNumber: int = 0
    _id: str

    @property
    def id(self) -> str:
        return self._id

    def __init__(self):
        self._id = BaseEntity.generateId(self)

    def loadPortrait(self, path: str) -> PhotoImage:
        pilImage = Image.open(path)
        return PhotoImage(pilImage)

    @staticmethod
    def generateId(inst) -> str:
        name = type(inst).__name__
        BaseEntity._lastIdNumber += 1
        return name + str(BaseEntity._lastIdNumber)

    @staticmethod
    def getEntities(duration: float) -> list[type[IEntity]]:
        for entity in BaseEntity._entityCensus:
            entity.position.moveInDirection(0, duration, 20, 0)
        return BaseEntity._entityCensus

    @staticmethod
    def getAllEntities() -> list[type[IEntity]]:
        return BaseEntity._entityCensus

    @staticmethod
    def addEntity(entity: IEntity) -> None:
        if BaseEntity._entityCensus is None:
            BaseEntity._entityCensus = [entity]
            return
        BaseEntity.addToRegions(entity)
        BaseEntity._entityCensus.append(entity)
        BaseEntity.printWorldRegion()

    @staticmethod
    def changeWorldSize(width: int, height: int) -> None:
        Positioning.setWorldSize(width, height)
        for entity in BaseEntity._entityCensus:
            entity.position.worldSizeHasChange()

    @staticmethod
    def addToRegions(entity: IEntity):
        rX = math.floor(entity.position.x / 80)
        rY = math.floor(entity.position.y / 80)

        BaseEntity._worldRegions[rY][rX].append(entity)

    @staticmethod
    def changeRegion(entity: IEntity):
        pRX = math.floor(entity.position.previousX / 80)
        pRY = math.floor(entity.position.previousY / 80)

        rX = math.floor(entity.position.x / 80)
        rY = math.floor(entity.position.y / 80)

        if pRX != rX or pRY != rY:
            if entity in BaseEntity._worldRegions[pRY][pRX]:
                BaseEntity._worldRegions[pRY][pRX].pop(BaseEntity._worldRegions[pRY][pRX].index(entity))
            BaseEntity._worldRegions[rY][rX].append(entity)

    

    @staticmethod
    def printWorldRegion():
        print("-----")
        for i in BaseEntity._worldRegions:
            s = ""
            for j in i:
                s += str(len(j)) + " "
            print(s)
