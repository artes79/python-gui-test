from ModelClasses.IEntity import IEntity
from ViewClasses.ICanvasLayer import ICanvasLayer


class IGameBoard(ICanvasLayer):

    @staticmethod
    def run(entities: list[type[IEntity]]) -> None:
        pass

