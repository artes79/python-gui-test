from Classes.Model.BaseComponent import *


class Living(BaseComponent, IMortal, IComputeAndEvolvEntity):

    lifeCycle: ITypeLifeCycleStages = ITypeLifeCycleStages(10, 20)

    def __init__(self, type, diameter, images, startPos):
        BaseComponent.__init__(type, diameter, images, startPos)



