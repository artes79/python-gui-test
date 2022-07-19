from dataclasses import dataclass


@dataclass
class Orientation:
    xCoord: int
    yCoord: int
    direction: int
    speed: float

