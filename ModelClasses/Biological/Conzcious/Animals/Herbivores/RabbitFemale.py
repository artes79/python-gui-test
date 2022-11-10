from PIL.ImageTk import PhotoImage
from DataClasses.Positioning import Positioning
from ModelClasses.Biological.Conzcious.Animals.Herbivores.IRabbitFemale import IRabbitFemale
from ModelClasses.Biological.Conzcious.Animals.Herbivores.Rabbit import Rabbit


class RabbitFemale(Rabbit, IRabbitFemale):

    _position: Positioning = Positioning(280, 350, (10, 10))
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
        return super(RabbitFemale, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = RabbitFemale()
        RabbitFemale.addEntity(entity)

