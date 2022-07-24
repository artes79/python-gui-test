from Interface.ISpatialProperties import *


class ISpatial:

    lastIdNumber: int
    id: str
    spatialProperties: ISpatialProperties

    @staticmethod
    def generateId(self) -> str:
        pass
