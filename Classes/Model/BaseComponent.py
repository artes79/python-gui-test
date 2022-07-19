from Classes import *


class BaseComponent(object):

    lastIdNumber = 0

    def __init__(self, id: str, diameter, images, startPos):
        self.type = "sau"
        self.id: str = id
        self.diameter = diameter
        self.exists = True
        self.onScreen = False
        self.images: Images = images
        self.position: Position = startPos


    @staticmethod
    def generateId(type):
        BaseComponent.lastIdNumber += 1
        id = type + str(BaseComponent.lastIdNumber)
        return id
