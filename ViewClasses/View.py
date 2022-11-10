from ViewClasses.DataLayer import DataLayer
from ViewClasses.GameBoard import GameBoard
from ViewClasses.IView import IView
import tkinter as gui


class View(IView):

    rootGUI: gui.Tk
    mainView: gui.Frame
    gameBoardLayer: gui.Canvas
    dataLayersLayer: gui.Frame
    guiRunning: bool

    _viewWidth: int
    _viewHeight: int

    @staticmethod
    def startGameView(width: int, height: int):
        View._viewWidth = width
        View._viewHeight = height
        View.initGUI()
        GameBoard.initBoard(View.gameBoardLayer)
        DataLayer.initLayer(View.gameBoardLayer)


    @staticmethod
    def initGUI() -> None:
        View.rootGUI = gui.Tk()
        View.rootGUI.title("Evolution")
        View.rootGUI.protocol("WM_DELETE_WINDOW", View.onClosing)
        View.rootGUI.minsize(View._viewWidth, View._viewHeight)
        View.rootGUI.bind("<Configure>", View.onResize)
        View.mainView = gui.Frame(View.rootGUI)
        View.mainView.pack(fill=gui.BOTH, expand=gui.YES)
        View.gameBoardLayer = gui.Canvas(View.mainView, width=View._viewWidth, height=View._viewHeight, bg="#f5deb3", highlightthickness=0)
        View.gameBoardLayer.pack(fill=gui.BOTH, expand=gui.YES)
        View.guiRunning = True


    @staticmethod
    def runGUI(entities) -> (int, int):
        GameBoard.run(entities)
        DataLayer.run()
        View.arangeLayers()
        View.rootGUI.update()
        return View._viewWidth, View._viewHeight

    @staticmethod
    def arangeLayers():
        View.gameBoardLayer.tag_lower("GameBoard")
        View.gameBoardLayer.tag_raise("DataLayer")

    @staticmethod
    def onClosing():
        View.guiRunning = False

    @staticmethod
    def onResize(event):
        View._viewWidth = event.width
        View._viewHeight = event.height
