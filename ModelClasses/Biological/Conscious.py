from ModelClasses.BaseEntity import BaseEntity
from ModelClasses.Biological.IConscious import IConscious


class Conscious(BaseEntity, IConscious):

    def __init__(self):
        super.__init__()

