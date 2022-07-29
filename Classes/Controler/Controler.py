#from Classes import *
from Classes.Model.Model import *
import Classes.View.GUI as gui
import json
import time


class Controler(object):

    def __init__(self, name):

        gameDataStr = open('gameData.json')
        self.gameData = json.load(gameDataStr)

        self.timeLastUpdate = time.time()

        self.name = name
        self.model = Model(self.gameData)

        self.gui = gui.GUI(self.gameData)
        self.gui.draw()

    def executeOneStep(self):
        newTime = time.time()
        diffTime = newTime - self.timeLastUpdate
        #print(diffTime)
        self.timeLastUpdate = newTime
        self.model.run(diffTime)

    def getEntityImages(self):
        pass

