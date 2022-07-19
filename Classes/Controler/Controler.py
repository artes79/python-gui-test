from Classes import *


class Controler(object):

    def __init__(self, name):
        self.name = name
        self.model = Model("model")

        self.gui = GUI(self)
        self.gui.draw()
