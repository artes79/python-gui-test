from PIL.ImageTk import PhotoImage

from DataClasses.IPositioning import IPositioning
from DataClasses.Positioning import Positioning
from ModelClasses.Nonbiological.Water import Water
from ModelClasses.Nonbiological.Waters.IDeepWater import IDeepWater


class DeepWater(Water, IDeepWater):

    _position: IPositioning
    _portrait: PhotoImage

    @property
    def position(self) -> IPositioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait is None:
            self._portrait = self.loadPortrait("images/deep-water.png")
        return self._portrait

    def __init__(self, x: int, y: int):
        super().__init__()
        self._position = Positioning(x, y, (90, 60), False)
        self._position.setRandomPosition(15, DeepWater.getAllEntities())
        self._position.getOverlaps(DeepWater.getAllEntities())

    @staticmethod
    def createEntity() -> None:
        for i in range(2):
            entity = DeepWater(1, 1)
            DeepWater.addEntity(entity)