from __future__ import annotations
from dataclasses import dataclass


@dataclass
class IPositioning:
    x: float
    y: float
    orientation: float

    def getX_asInt(self) -> int:
        pass

    def getY_asInt(self) -> int:
        pass

    def rePositioning_relatively(self, shift: IPositioning):
        pass