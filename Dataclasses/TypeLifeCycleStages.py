from dataclasses import dataclass
from Interface import *


@dataclass
class TypeLifeCycleStages(ITypeLifeCycleStages):

    isAdultAt: float
    isElderlyAt: float

    def __init__(self, isAdultAt: float, isElderlyAt: float):
        self.isAdultAt = isAdultAt
        self.isElderlyAt = isElderlyAt

    @staticmethod
    def getEndOfLifeCycle() -> float:
        return 12
