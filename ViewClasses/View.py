from ViewClasses.IView import IView


class View(IView):

    def p(self):
        pass

    @staticmethod
    def initGUI():
        View.rootGUI = gui.Tk()
        View.rootGUI.protocol("WM_DELETE_WINDOW", View.onClosing)
        View.mainView = gui.Frame(View.rootGUI)
        View.mainView.pack(fill=gui.BOTH, expand=gui.YES)
        View.gameBoardLayer = gui.Canvas(View.mainView, width=640, height=480, bg="#f5deb3", highlightthickness=0)
        View.gameBoardLayer.pack(fill=gui.BOTH, expand=gui.YES)
        View.gameRunning = True

    @staticmethod
    def runGUI():
        while View.gameRunning:
            GameBoard.run()
            DataLayer.run()
            View.arangeLayers()
            View.rootGUI.update()

    @staticmethod
    def arangeLayers():
        pass

    @staticmethod
    def onClosing():
        View.gameRunning = False
