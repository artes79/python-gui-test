import math
import tkinter as gui

from ModelClasses.Biological.IConscious import IConscious
from ModelClasses.IEntity import IEntity
from ViewClasses.IGameBoard import IGameBoard


class GameBoard(IGameBoard):

    _playLayer: gui.Canvas

    _running = True

    @staticmethod
    def initBoard(playLayer: gui.Canvas):
        GameBoard._playLayer = playLayer

    @staticmethod
    def run(entities: list[type[IEntity]]) -> None:
        if GameBoard._running:
            for entity in entities:
                GameBoard.addEntity(entity)
            GameBoard._running = False
        else:
            for entity in entities:
                GameBoard.moveEntity(entity)

    @staticmethod
    def addEntity(entity: IEntity) -> None:
        GameBoard._playLayer.create_image(entity.position.xAsInt,
                                          entity.position.yAsInt,
                                          anchor=gui.CENTER,
                                          image=entity.portrait,
                                          tag=(entity.id, "GameBoard"))

    @staticmethod
    def moveEntity(entity: IEntity) -> None:
        boundingBox = GameBoard._playLayer.bbox(entity.id)
        posX = entity.position.xAsInt - math.floor((boundingBox[2] - boundingBox[0]) / 2)
        posY = entity.position.yAsInt - math.floor((boundingBox[3] - boundingBox[1]) / 2)
        GameBoard._playLayer.moveto(entity.id, posX, posY)

    # tags: all: game-item, grups: ground, on-ground, above-ground
    @staticmethod
    def arangeGameItems():
        pass