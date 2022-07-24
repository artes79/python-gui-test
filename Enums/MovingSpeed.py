from enum import Enum


class MovingSpeed(float, Enum):
    SLOW = 0.3
    NORMAL = 1
    FAST = 1.3
    RUNNING = 2
