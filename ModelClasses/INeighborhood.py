from ModelClasses.IEntity import IEntity


class INeighborhood:

    @staticmethod
    def hasMoved(entities: IEntity) -> list[type[IEntity]]:
        pass


class INeighborhoodUser:

    @property
    def neighborhoodSquar(self) -> (int, int):
        pass

    @neighborhoodSquar.setter
    def neighborhoodSquar(self, value: (int, int)) -> None:
        pass
