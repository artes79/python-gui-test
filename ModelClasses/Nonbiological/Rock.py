from PIL.ImageTk import PhotoImage
from DataClasses.Positioning import Positioning
from ModelClasses.BaseEntity import BaseEntity
from ModelClasses.Nonbiological.IRock import IRock


class Rock(BaseEntity, IRock):

    _position: Positioning = Positioning(50, 50, (10, 10))
    _portrait: PhotoImage = None

    @property
    def position(self) -> Positioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/deep-water.png")
        return self._portrait

    def __init__(self):
        super().__init__()
        self._position = Positioning(50, 50, (10, 10), False)
        self._position.setRandomPosition(30)

    def loadPortrait(self, path: str) -> PhotoImage:
        return super(Rock, self).loadPortrait(path)

    @staticmethod
    def createEntity() -> None:
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
        entity = Rock()
        Rock.addEntity(entity)
