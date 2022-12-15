import time
from random import random, seed
import numpy as np
from Evolution.DataClasses.Positioning import Positioning
from Evolution.DataClasses.IGroundPositioning import IGroundPositioning
from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.IEntity import IEntity


class GroundPositioning(Positioning, IGroundPositioning):

    walking = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1],
               [2, -1], [2, 0], [2, 1], [2, 2], [1, 2], [0, 2], [-1, 2], [-2, 2], [-2, 1], [-2, 0], [-2, -1], [-2, -2], [-1, -2], [0, -2], [1, -2], [2, -2],
               [3, -2], [3, -1], [3, 0], [3, 1], [3, 2], [3, 3]]

    def SetRandomNabourPosition(self, entity: IEntity) -> None:
        position = self.GetRandomPosition()
        i = 0
        for p in self.walking:
            isOccupaid = BaseEntity.IsGroundSquareOcupide(position[0]+self.walking[i][0], position[1]+self.walking[i][1])
            if isOccupaid:
                break
            i += 1
        i -= 1
        position[0] += self.walking[i][0]
        position[1] += self.walking[i][1]
        self.position = position
        BaseEntity.AddEntityToGround(entity)

    def SetRandomPosition(self, entity: IEntity) -> None:
        position = self.GetRandomPosition()
        self.position = position
        BaseEntity.AddEntityToGround(entity)

    def GetRandomPosition(self) -> np.ndarray:
        x = 0
        y = 0
        counter = 0
        while True:
            x = round(random() * 43) * 15 + 8
            y = round(random() * 31) * 15 + 8
            if BaseEntity.IsGroundSquareOcupide(x, y) is False:
                break
        return np.array([x, y], dtype=float)