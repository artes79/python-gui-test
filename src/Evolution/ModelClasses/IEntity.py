from Evolution.DataClasses.IPositioning import IPositioning
from PIL.ImageTk import PhotoImage

class IEntity:

    @property
    def id(self) -> str:
        pass

    @property
    def position(self) -> IPositioning:
        pass

    @property
    def portrait(self) -> PhotoImage:
        pass

    @staticmethod
    def GetTypePortrait() -> PhotoImage:
        pass
    
    @staticmethod
    def CreateTypeEntities() -> None:
        pass


class IEntities:

    @staticmethod
    def GenerateId() -> str:
        pass

    @staticmethod
    def LoadPortrait(path: str) -> PhotoImage:
        pass

    @staticmethod
    def GetEntities() -> list[type[IEntity]]:
        pass

    @staticmethod
    def AddEntity(entity: IEntity) -> None:
        pass

    @staticmethod
    def AddEntityToGround(entity: IEntity) -> None:
        pass

    @staticmethod
    def GetEntityFromGroundSquare(x: int, y: int) -> IEntity:
        pass

    @staticmethod
    def IsGroundSquareOcupide(x: int, y: int) -> bool:
        pass
