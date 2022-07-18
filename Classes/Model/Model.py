from Classes import *
from Classes.Model.Animals import *


class Model(object):

    def __init__(self, name):
        self.name = name

        dog = Dog("Terje")
        dog.printD()