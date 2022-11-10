from PIL.ImageTk import PhotoImage

from DataClasses.Positioning import Positioning
from ModelClasses.Biological.Conzcious.Animals.Predator import Predator
from ModelClasses.Biological.Conzcious.Animals.Predators.IFox import IFox


class Fox(Predator, IFox):

    _position: Positioning = Positioning(100, 300, (10, 10))
    _portrait: PhotoImage = None

    @property
    def position(self) -> Positioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/fox.png")
        return self._portrait

    def __init__(self):
        super().__init__()
        _position = Positioning(200, 50, (10, 10))

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(Fox, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = Fox()
        Fox.addEntity(entity)

