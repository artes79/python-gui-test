import numpy as np
from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.Biological.Plants.Grasses.IGrassRustle import IGrassRustle
from Evolution.DataClasses.IPositioning import IPositioning
from Evolution.DataClasses.GroundPositioning import GroundPositioning


class GrassRustle(BaseEntity, IGrassRustle):

    _typeProtrait = BaseEntity.LoadPortrait("images/grass.png")

    _id: str
    _position: IPositioning
    _portrait: PhotoImage

    @property
    def id(self) -> str:
        return self._id

    @property
    def position(self) -> IPositioning:
        return self._position

    @property
    def portrait(self) -> PhotoImage:
        if self._portrait == null:
            return GrassRustle._typeProtrait
        return self._portrait

    def __init__(self):
        self._id = GrassRustle.GenerateId()
        self._position = GroundPositioning()
        self._position.physical.extent = np.array([7.5, 7.5], dtype=float)

    @staticmethod
    def GenerateId() -> str:
        return "Rustle" + BaseEntity.GenerateId()