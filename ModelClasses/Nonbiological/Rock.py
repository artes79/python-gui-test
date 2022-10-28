from ModelClasses.BaseEntity import BaseEntity
from ModelClasses.Nonbiological.IRock import IRock


class Rock(BaseEntity, IRock):

    def __init__(self):
        super.__init__()

