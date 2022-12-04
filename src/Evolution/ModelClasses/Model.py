import numpy as np
from Evolution.ModelClasses.IModel import IModel
from Evolution.DataClasses.WorldData import WorldData
from Evolution.DataClasses.Positioning import Positioning
from Evolution.ModelClasses.IEntity import IEntity

class Model(IModel):

    @staticmethod
    def StartGameModel(width: int, height: int) -> None:
        worldData = WorldData()
        worldData.size = np.array([width, height], dtype=float)
        Positioning.SetWorld(worldData)

    @staticmethod
    def RunOneStep(duration: float) -> None:
        pass

    @staticmethod
    def GetEntities() -> list[type[IEntity]]:
        pass
