from __future__ import annotations
from dataclasses import dataclass
from Interface import *
import math


@dataclass()
class Positioning(IPositioning):

    x: float
    y: float
    orientation: float

    def __init__(self):
        pass

    def getX_asInt(self):
        return round(self.x)

    def getY_asInt(self):
        return round(self.y)

    def rePositioning_relatively(self, shift: Positioning):
        self.x += shift.x
        self.y += shift.y
        self.orientation = (self.orientasion + shift.orientation) % 360



