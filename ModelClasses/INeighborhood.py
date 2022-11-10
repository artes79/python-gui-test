from DataClasses.IPositioning import IPositioningUser


class INeighborhood:

    @staticmethod
    def hasMoved(entities: IPositioningUser) -> list[type[IPositioningUser]]:
        pass


