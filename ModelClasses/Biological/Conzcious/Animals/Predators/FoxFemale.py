from PIL.ImageTk import PhotoImage

from DataClasses.Positioning import Positioning
from ModelClasses.Biological.Conzcious.Animals.Predators.Fox import Fox
from ModelClasses.Biological.Conzcious.Animals.Predators.IFoxFemale import IFoxFemale


class FoxFemale(Fox, IFoxFemale):

    _position: Positioning = Positioning(50, 420, (10, 10))
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
        return super(FoxFemale, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
        entity = FoxFemale()
        FoxFemale.addEntity(entity)
