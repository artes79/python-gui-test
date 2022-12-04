from Evolution.DataClasses.IPositioning import IPositioning


class IEntity:

    @property
    def id(self) -> str:
        pass

    @property
    def position(self) -> IPositioning:
        pass


class IEntities:

    @staticmethod
    def generateId() -> str:
        pass