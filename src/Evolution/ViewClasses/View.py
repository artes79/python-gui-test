from Evolution.ViewClasses.IView import IView
from Evolution.ModelClasses.IEntity import IEntity
import tkinter as gui


class View(IView):

    _rootGUI: gui.Tk
    _guiRunning: bool

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
        View._rootGUI.protocol("WM_DELETE_WINDOW", lambda: View.onClosing())
        View._rootGUI.minsize(View._viewWidth, View._viewHeight)
        View._guiRunning = True

    @staticmethod
    def RunGUI(entities: list[type[IEntity]]):
        View._rootGUI.update()

    @staticmethod
    def IsRunning() -> bool:
        return View._guiRunning

    @staticmethod
    def onClosing() -> None:
        View._guiRunning = False
