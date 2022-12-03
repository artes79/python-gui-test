from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.Biological.Plants.Grasses.IGrassRustle import IGrassRustle


class GrassRustle(BaseEntity, IGrassRustle):

    _id: str

    @property
    def id(self) -> str:
        return self._id

    def __init__(self):
        self._id = GrassRustle.GenerateId()

    @staticmethod
    def GenerateId() -> str:
        return "Rustel" + BaseEntity.GenerateId()