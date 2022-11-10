
from PIL.ImageTk import PhotoImage
from numpy import random

from DataClasses.Positioning import Positioning
from ModelClasses.BaseEntity import BaseEntity
from ModelClasses.Biological.Plant import Plant
from ModelClasses.Biological.Plants.IGrass import IGrass


class Grass(Plant, IGrass):

    _position: Positioning = Positioning(7, 7, (10, 10))
    _portrait: PhotoImage = None

    @property
    def position(self) -> Positioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/grass.png")
        return self._portrait

    def __init__(self, x: int, y: int):
        super().__init__()
        self._position = Positioning(x, y, (10, 10), False)
        self._position.setRandomPosition(15, Grass.getAllEntities())

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(Grass, self).loadPortrait(path)


    @staticmethod
    def createEntity() -> None:
        for i in range(int(42*32/2)):
            entity = Grass(7, 7)
            rand = random.randint(1, 7)
            if len(BaseEntity.getAllEntities()) > 2:
                closestEntity = entity.position.closestTo(BaseEntity.getAllEntities())
                entity.position.placeCloseTo(closestEntity, BaseEntity.getAllEntities())
            Grass.addEntity(entity)


