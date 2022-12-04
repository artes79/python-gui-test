import tkinter as gui
from Evolution.ModelClasses.IEntity import IEntity


class IGameBoard:

    @staticmethod
    def InitBoard(playLayer: gui.Canvas) -> None:
        pass

    @staticmethod
    def Run(entities: list[type[IEntity]]) -> None:
        pass

    @staticmethod
    def AddEntity(entity: IEntity) -> None:
        pass

    @staticmethod
    def MoveEntity(entity: IEntity) -> None:
        pass

    @staticmethod
    def RemoveEntity(entity: IEntity) -> None:
        pass
