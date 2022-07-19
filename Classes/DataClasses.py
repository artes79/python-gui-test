from dataclasses import dataclass



@dataclass
class Position:
    xCoord: int
    yCoord: int

@dataclass
class Orientation:
    direction: int
    speed: float

@dataclass
class DrawData:
    viewType: int
    orientation: Orientation

#@dataclass
#class ViewType:

@dataclass
class Images:
    allDirections: int

