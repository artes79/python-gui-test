from dataclasses import dataclass


@dataclass
class ISpatialProperties:

    radius: float
    height: float
    birth: float

    def __init__(self, owner):
        pass

    def getLifePhase(self):
        pass
