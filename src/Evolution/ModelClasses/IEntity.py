

class IEntity:

    @property
    def id(self) -> str:
        pass


class IEntities:

    @staticmethod
    def generateId() -> str:
        pass