from dataclasses import dataclass


@dataclass
class ITypeLifeCycleStages:

    isAdultAt: float
    isElderlyAt: float

    def __init__(self, isAdultAt: float, isElderlyAt: float):
        pass

    @staticmethod
    def getEndOfLifeCycle() -> float:
        pass
