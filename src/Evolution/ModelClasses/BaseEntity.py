from PIL import Image
from PIL.ImageTk import PhotoImage
import numpy as np

from Evolution.ModelClasses.IBaseEntity import IBaseEntity
from Evolution.ModelClasses.IEntity import IEntity

class BaseEntity(IBaseEntity):

    _entitiesCensus: list[type[IEntity]] = []
    _lastGeneratdId: int = 0
    _groundTable: list = [[None] * 32 for i in range(44)]

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

    @staticmethod
    def AddEntityToGround(entity: IEntity) -> None:
        x = int(round(entity.position.position[0] / 15)) - 1
        y = int(round(entity.position.position[1] / 15)) - 1
        BaseEntity._groundTable[x][y] = entity

    @staticmethod
    def GetEntityFromGroundSquare(px: int, py: int) -> IEntity:
        x = int(round(px / 15)) - 1
        y = int(round(py / 15)) - 1
        return BaseEntity._groundTable[x][y]

    @staticmethod
    def IsGroundSquareOcupide(x: int, y: int) -> bool:
        return BaseEntity.GetEntityFromGroundSquare(x, y) != None