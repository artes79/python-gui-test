from ModelClasses.IEntity import IEntity


class IView:

    @staticmethod
    def startGameView() -> None:
        pass

    # <gui.Tk()>.protocol("WM_DELETE_WINDOW", View.onClosing)
    @staticmethod
    def initGUI() -> None:
        pass

    @staticmethod
    def runGUI(entities: list[type[IEntity]]) -> (int, int):
        pass

    @staticmethod
    def arangeLayers() -> None:
        pass

    # Stop View.runGUI() når vinduet lukkes
    @staticmethod
    def onClosing() -> None:
        pass
