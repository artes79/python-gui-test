import time

from Evolution.IEvolutionController import IEvolutionController
from Evolution.ModelClasses.Model import Model
from Evolution.ViewClasses.View import View


class EvolutionController(IEvolutionController):

    _gameboardWidth: int = 640
    _gameboardHeight: int = 480

    _timestampLastFrame: float

    @staticmethod
    def StartGame() -> None:
        Model.StartGameModel(EvolutionController._gameboardWidth, EvolutionController._gameboardHeight)
        View.StartGameView(EvolutionController._gameboardWidth, EvolutionController._gameboardHeight)
        EvolutionController.RunGame()

    @staticmethod
    def RunGame() -> None:
        EvolutionController._timestampLastFrame = time.time()
        while View.IsRunning():
            duration = EvolutionController.DurationToNextFrame()
            EvolutionController.WaitToNextFrame(duration)
            Model.RunOneStep(duration)
            entities = Model.GetEntities()
            View.RunGUI(entities)

    @staticmethod
    def DurationToNextFrame() -> float:
        newTimestamp = time.time()
        duration = 0.05 - (newTimestamp - EvolutionController._timestampLastFrame)
        if duration < 0:
            duration = 0
        EvolutionController._timestampLastFrame = newTimestamp
        return duration

    @staticmethod
    def WaitToNextFrame(duration: float) -> None:
        time.sleep(duration)

