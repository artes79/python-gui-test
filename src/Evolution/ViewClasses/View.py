from Evolution.ViewClasses.IView import IView
from Evolution.ModelClasses.IEntity import IEntity
import tkInter as gui


class View(IView):

    _rootGUI: gui.Tk

    _viewWidth: int
    _viewHeight: int

    @staticmethod
    def StartGameView(width: int, height: int) -> None:
        View._viewWidth = width
        View._viewHeight = height
        View.InitGUI()

    @staticmethod
    def InitGUI() -> None:
        View._rootGUI = gui.Tk()
        View._rootGUI.title("Evolution")
        View._rootGUI.protocol("VM_DELETE_WINDOW", View.OnClosing)
        View._rootGUI.minsize(View._viewWidth, View._viewHeight)

    @staticmethod
    def RunGUI(entities: list[type[IEntity]]):
        pass

    @staticmethod
    def OnClosing() -> None:
        pass
