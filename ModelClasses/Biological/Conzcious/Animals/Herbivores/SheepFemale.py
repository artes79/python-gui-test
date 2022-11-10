from PIL.ImageTk import PhotoImage

from DataClasses.Positioning import Positioning
from ModelClasses.Biological.Conzcious.Animals.Herbivores.ISheepFemale import ISheepFemale
from ModelClasses.Biological.Conzcious.Animals.Herbivores.Sheep import Sheep


class SheepFemale(Sheep, ISheepFemale):

    _position: Positioning = Positioning(600, 400, (10, 10))
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
        _position = Positioning(200, 50, (10, 10))

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(SheepFemale, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = SheepFemale()
        SheepFemale.addEntity(entity)

