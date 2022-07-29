from Interface import *
from DataStorageClasses.TypeLifeCycleStages import *
from dataclasses import dataclass
from Enums import *
import time


@dataclass
class SpatialProperties(ISpatialProperties):

    radius: float
    height: float
    birth: float
    #lifeCycle: TypeLifeCycleStages

    def __init__(self):
        self.radius = 0.0
        self.height = 0.0
        self.birth = 0.0
        #self.lifeCycle = TypeLifeCycleStages(0.0, 0.0)

    def setLifeCycle(self, owner):
        if isinstance(owner, IMortal):
            t = type(owner)
            #self.lifeCycle = t.lifeCycle

    def getLifePhase(self):
        if isinstance(self, IImmortal):
            return LifeCycleForm.IMMORTAL
        if isinstance(self, IMortal):
            t = time.time()
            if self.lifeCycle.getEndOfLifeCycle() > t:
                return LifeCycleForm.NOT_ALIVE
            if self.lifeCycle.isAdultAt > t:
                return LifeCycleForm.INFANT
            if self.lifeCycle.isElderlyAt > t:
                return LifeCycleForm.ADULT
            return LifeCycleForm.ELDERLY


