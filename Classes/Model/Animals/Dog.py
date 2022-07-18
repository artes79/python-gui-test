from Classes.Model.Animals import *

class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)

    def printD(self):
        print self.name
