from Evolution.DataClasses.IWorldData import IWorldData


class IPositioning:

    @property
    def x(self) -> float:
        pass

    @property
    def xRound(self) -> int:
        pass

    @property
    def y(self) -> float:
        pass

    @property
    def yRound(self) -> float:
        pass

    @staticmethod
    def SetWorld(world: IWorldData) -> None:
        pass

    @staticmethod
    def GetWorld() -> IWorldData:
        pass
