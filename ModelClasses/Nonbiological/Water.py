from PIL.ImageTk import PhotoImage
from numpy import random

from DataClasses.Positioning import Positioning
from ModelClasses.BaseEntity import BaseEntity
from ModelClasses.Nonbiological.IWater import IWater


class Water(BaseEntity, IWater):

    _position: Positioning = Positioning(7, 7, (10, 10))
    _portrait: PhotoImage = None

    @property
    def position(self) -> Positioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/water.png")
        return self._portrait

    def __init__(self, x: int, y: int):
        super().__init__()
        self._position = Positioning(x, y, (10, 10), False)
        self._position.setRandomPosition(15, Water.getAllEntities())

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(Water, self).loadPortrait(path)


    @staticmethod
    def createEntity() -> None:
        for i in range(int(42*32/20)):
            entity = Water(7, 7)
            rand = random.randint(1, 7)
            if len(BaseEntity.getAllEntities()) > 0:
                closestEntity = entity.position.closestTo(BaseEntity.getAllEntities())
                entity.position.placeCloseTo(closestEntity, BaseEntity.getAllEntities())
            Water.addEntity(entity)