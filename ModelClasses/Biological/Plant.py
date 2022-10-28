from ModelClasses.BaseEntity import BaseEntity
from ModelClasses.Biological.IPlant import IPlant


class Plant(BaseEntity, IPlant):

    def __init__(self):
        super.__init__()

