from Evolution.ModelClasses.IEntity import IEntity


class IModel:

    @staticmethod
    def StartGameModel(width: int, height: int) -> None:
        pass

    @staticmethod
    def RunOneStep(duration: float) -> None:
        pass

    @staticmethod
    def GetEntities() -> list[type[IEntity]]:
        pass
