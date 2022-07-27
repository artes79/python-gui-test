from Classes.Model.BaseComponent import *
from Dataclasses import *
from Interface import *


class Living(BaseComponent, IMortal, IComputeAndEvolvEntity):

    lifeCycle: TypeLifeCycleStages = TypeLifeCycleStages()

    def __init__(self, positioning: Positioning,
                 spatialProperties: SpatialProperties):
        super().__init__(positioning, spatialProperties)



