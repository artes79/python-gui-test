from PIL.ImageTk import PhotoImage
from DataClasses.Positioning import Positioning
from ModelClasses.Biological.Conzcious.Animals.Herbivore import Herbivore
from ModelClasses.Biological.Conzcious.Animals.Herbivores.ISheep import ISheep


class Sheep(Herbivore, ISheep):

    _position: Positioning = Positioning(99, 450, (10, 10))
    _portrait: PhotoImage = None

    @property
    def position(self) -> Positioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/sheap4.png")
        return self._portrait

    def __init__(self):
        super().__init__()
        _position = Positioning(99, 400, (10, 10))

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(Sheep, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = Sheep()
        Sheep.addEntity(entity)
