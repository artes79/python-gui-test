from Evolution.ModelClasses.IBaseEntity import IBaseEntity
from PIL import Image
from PIL.ImageTk import PhotoImage

from Evolution.ModelClasses.IEntity import IEntity

class BaseEntity(IBaseEntity):

    _entitiesCensus: list[type[IEntity]] = []
    _lastGeneratdId: int = 0

    @staticmethod
    def GenerateId() -> str:
        BaseEntity._lastGeneratdId += 1
        return str(BaseEntity._lastGeneratdId)

    @staticmethod
    def LoadPortrait(path: str) -> PhotoImage:
        pilImage = Image.open(path)
        return PhotoImage(pilImage)

    @staticmethod
    def GetEntities() -> list[type[IEntity]]:
        return BaseEntity._entitiesCensus

    @staticmethod
    def AddEntity(entity: IEntity) -> None:
        BaseEntity._entitiesCensus.append(entity)