from Classes import *
import time


class Controler(object):

    def __init__(self, name):

        self.timeLastUpdate = time.time()

        self.name = name
        self.model = Model()

        self.gui = GUI(self)
        self.gui.draw()

    def executeOneStep(self):
        newTime = time.time()
        diffTime = newTime - self.timeLastUpdate
        #print(diffTime)
        self.timeLastUpdate = newTime
        self.model.run(diffTime)

    def getEntityImages(self):
        pass

