from tkinter import PhotoImage

from DataClasses.Positioning import Positioning
from ModelClasses.Biological.Conzcious.Animals.Herbivore import Herbivore
from ModelClasses.Biological.Conzcious.Animals.Herbivores.IRabbit import IRabbit


class Rabbit(Herbivore, IRabbit):

    _position: Positioning = Positioning(280, 300, (10, 10))
    _portrait: PhotoImage = None

    @property
    def position(self) -> Positioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/rabbit.png")
        return self._portrait

    def __init__(self):
        super().__init__()
        _position = Positioning(200, 50, (10, 10))

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(Rabbit, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = Rabbit()
        Rabbit.addEntity(entity)

