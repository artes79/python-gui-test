

class IEntity:

    @property
    def id(self) -> str:
        pass


class IEntities:

    @staticmethod
    def generateId(inst) -> str:
        pass