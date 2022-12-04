from Evolution.ViewClasses.IView import IView
from Evolution.ModelClasses.IEntity import IEntity
from Evolution.ViewClasses.GameBoard import GameBoard
from Evolution.ModelClasses.BaseEntity import BaseEntity
import tkinter as gui


class View(IView):

    _rootGUI: gui.Tk
    _guiRunning: bool
    _mainView: gui.Frame
    _gameBoardCanvas: gui.Canvas

    _viewWidth: int
    _viewHeight: int

    @staticmethod
    def StartGameView(width: int, height: int) -> None:
        View._viewWidth = width
        View._viewHeight = height
        View.InitGUI()
        GameBoard.InitBoard(View._gameBoardCanvas)

    @staticmethod
    def InitGUI() -> None:
        View._rootGUI = gui.Tk()
        View._rootGUI.title("Evolution")
        View._rootGUI.protocol("WM_DELETE_WINDOW", lambda: View.onClosing())
        View._rootGUI.minsize(View._viewWidth, View._viewHeight)
        View._guiRunning = True
        View._mainView = gui.Frame(View._rootGUI)
        View._mainView.pack(fill=gui.BOTH, expand=gui.YES)
        View._gameBoardCanvas = gui.Canvas(View._mainView, width=View._viewWidth, height=View._viewHeight, bg="#f5deb3", highlightthickness=0)
        View._gameBoardCanvas.pack(fill=gui.BOTH, expand=gui.YES)
        View._gameBoardCanvas.create_image(120, 120, image=BaseEntity.LoadPortrait("images/water.png"))

    @staticmethod
    def RunGUI(entities: list[type[IEntity]]):
        GameBoard.Run(entities)
        View._rootGUI.update()

    @staticmethod
    def IsRunning() -> bool:
        return View._guiRunning

    @staticmethod
    def onClosing() -> None:
        View._guiRunning = False
