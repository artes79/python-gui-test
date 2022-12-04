import numpy as np
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage
from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.Biological.Plants.Grasses.IGrassRustle import IGrassRustle
from Evolution.DataClasses.IPositioning import IPositioning
from Evolution.DataClasses.GroundPositioning import GroundPositioning


class GrassRustle(BaseEntity, IGrassRustle):

    _typeProtrait: PhotoImage = None

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
        if self._portrait == None:
            self._portrait = GrassRustle.GetTypePortrait()
        return self._portrait

    def __init__(self):
        self._id = GrassRustle.GenerateId()
        self._position = GroundPositioning()
        self._position.physical.extent = np.array([7.5, 7.5], dtype=float)
        self._portrait = None

    @staticmethod
    def GenerateId() -> str:
        return "Rustle" + BaseEntity.GenerateId()

    @staticmethod
    def GetTypePortrait() -> PhotoImage:
        if GrassRustle._typeProtrait == None:
            GrassRustle._typeProtrait = BaseEntity.LoadPortrait("images/grass.png")
        return GrassRustle._typeProtrait

    @staticmethod
    def CreateTypeEntities() -> None:
        for _ in range(int(42*32/2)):
            inst = GrassRustle()
            inst.position.SetRandomPosition()
            BaseEntity.AddEntity(inst)
