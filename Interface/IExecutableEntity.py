from __future__ import annotations
from Classes.Model.BaseComponent import *


class IExecutableEntity:

    @staticmethod
    def calculateNextStep():
        pass

    def executeStep(self):
        pass

    def calculateDistanceTo(self, entity: BaseComponent):
        pass

    @staticmethod
    def distance(x1: float, y1: float, x2: float, y2: float):
        pass
