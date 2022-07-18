from Classes import *


class Controler(object):

    def __init__(self, name):
        self.name = name
        self.model = Model("model")

    def makeView(self):
        self.gui = GUI()
        self.gui.draw()