from dataclasses import dataclass
from Interface import *


@dataclass
class TypeLifeCycleStages(ITypeLifeCycleStages):

    isAdultAt: float
    isElderlyAt: float

    def __init__(self):
        self.isAdultAt = 0
        self.isElderlyAt = 0

    @staticmethod
    def getEndOfLifeCycle() -> float:
        return 12
