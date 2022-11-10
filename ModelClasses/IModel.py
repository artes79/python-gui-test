from ModelClasses.IEntity import IEntity


class IModel:

    @staticmethod
    def startGameModel():
        pass

    @staticmethod
    def getEntities() -> list[type[IEntity]]:
        pass