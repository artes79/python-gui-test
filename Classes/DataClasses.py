from dataclasses import dataclass


@dataclass
class Orientation:
    xCoord: int
    yCoord: int
    direction: int
    speed: float

@dataclass
class DrawData:
    viewType: int
    orientation: Orientation

#@dataclass
#class ViewType:

