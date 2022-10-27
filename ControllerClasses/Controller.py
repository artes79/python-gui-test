from ControllerClasses.IController import IController
from ViewClasses.View import View


class Controller(IController):

    @staticmethod
    def startGame():
        View.startGameView()
