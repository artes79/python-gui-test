import tkinter as gui
from Evolution.ViewClasses.IGameBoard import IGameBoard
from Evolution.ModelClasses.IEntity import IEntity


class GameBoard(IGameBoard):

    _playLayer: gui.Canvas = None
    _running = True

    @staticmethod
    def InitBoard(playLayer: gui.Canvas) -> None:
        GameBoard._playLayer = playLayer

    @staticmethod
    def Run(entities: list[type[IEntity]]) -> None:
        if GameBoard._running:
            for entity in entities:
                GameBoard.AddEntity(entity)
            GameBoard._running = False

    @staticmethod
    def AddEntity(entity: IEntity) -> None:
        GameBoard._playLayer.create_image(entity.position.xRound,
                                          entity.position.yRound,
                                          image=entity.portrait,
                                          anchor=gui.CENTER,
                                          tag=entity.id)

    @staticmethod
    def MoveEntity(entity: IEntity) -> None:
        pass

    @staticmethod
    def RemoveEntity(entity: IEntity) -> None:
        pass