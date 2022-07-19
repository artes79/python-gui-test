from Classes import *


class BaseComponent(object):

    def __init__(self, name, diameter, images, startPos):
        self.name = name
        self.diameter = diameter
        self.exists = True
        self.images: Images = images
        self.position: Position = startPos
