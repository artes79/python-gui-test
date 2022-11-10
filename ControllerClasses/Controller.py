import time
from ControllerClasses.IController import IController
from ModelClasses.IEntity import IEntity
from ModelClasses.Model import Model
from ViewClasses.View import View


class Controller(IController):

    _timestampLastFrame: float

    _viewWidth: int = 640
    _viewHeight: int = 480
    _hasReSized: bool = False

    @staticmethod
    def startGame():
        Model.startGameModel(640, 480)
        View.startGameView(640, 480)
        Controller.runGame()

    @staticmethod
    def runGame():
        Controller._timestampLastFrame = time.time()
        while View.guiRunning:
            runTime = 0.05 - (time.time() - Controller._timestampLastFrame)
            duration = max(runTime, (time.time() - Controller._timestampLastFrame))
            if runTime > 0:
                time.sleep(runTime)
            Controller._timestampLastFrame = time.time()
            if Controller._hasReSized:
                entities = Model.getEntitiesWithScale(Controller._viewWidth, Controller._viewHeight)
                print(str(Controller._viewWidth), str(Controller._viewHeight))
                Controller._hasReSized = False
            else:
                entities = Model.getEntities(duration)
            (viewWidth, viewHeight) = View.runGUI(entities)
            if viewWidth != Controller._viewWidth or viewHeight != Controller._viewHeight:
                Controller._hasReSized = True
                Controller._viewWidth = viewWidth
                Controller._viewHeight = viewHeight