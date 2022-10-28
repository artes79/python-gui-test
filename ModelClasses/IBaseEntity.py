from ModelClasses.INeighborhood import INeighborhood


class IBaseEntity(INeighborhood):

    @property
    def id(self) -> str:
        pass

    @staticmethod
    def generateId(inst) -> str:
        pass
