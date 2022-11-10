from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage

from DataClasses.Positioning import Positioning
from ModelClasses.IBaseEntity import IBaseEntity
from ModelClasses.IEntity import IEntity


class BaseEntity(IBaseEntity):

    _entityCensus: list[type[IEntity]] = []

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
        BaseEntity._entityCensus.append(entity)

    @staticmethod
    def changeWorldSize(width: int, height: int) -> None:
        Positioning.setWorldSize(width, height)
        for entity in BaseEntity._entityCensus:
            entity.position.worldSizeHasChange()