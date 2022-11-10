from tkinter import PhotoImage

from DataClasses.Positioning import Positioning
from ModelClasses.Biological.Conzcious.Human import Human
from ModelClasses.Biological.Conzcious.Humans.IMan import IMan


class Man(Human, IMan):

    _position: Positioning = Positioning(320, 150, (10, 10))
    _portrait: PhotoImage = None

    @property
    def position(self) -> Positioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/man.png")
        return self._portrait

    def __init__(self):
        super().__init__()
        _position = Positioning(100, 50, (10, 10))

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(Man, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = Man()
        Man.addEntity(entity)

