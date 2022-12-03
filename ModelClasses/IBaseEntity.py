from ModelClasses.IEntity import IEntity, IEntityShared
from ModelClasses.INeighborhood import INeighborhood


class IBaseEntity(INeighborhood, IEntityShared):

    @property
    def id(self) -> str:
        pass

    @staticmethod
    def generateId(inst) -> str:
        pass

    @staticmethod
    def getEntities() -> list[type[IEntity]]:
        pass

    @staticmethod
    def addEntity(entity: IEntity) -> None:
        pass

    @staticmethod
    def changeRegion(entity: IEntity) -> None:
        pass

