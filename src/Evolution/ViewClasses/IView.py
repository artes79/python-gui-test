from Evolution.ModelClasses.IEntity import IEntity


class IView:

    @staticmethod
    def StartGameView(width: int, height: int) -> None:
        pass

    @staticmethod
    def InitGUI() -> None:
        pass

    @staticmethod
    def RunGUI(entities: list[type[IEntity]]):
        pass

    @staticmethod
    def OnClosing() -> None:
        pass
