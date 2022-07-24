from Classes import *
from Classes.Model.Living import *
from Classes.Model import *
from random import randint


class Model(object):

    entityTypes = {
        "Rock": Rock
    }

    def __init__(self):
        self.propagateEntities()

    def propagateEntities(self):
        for _ in range(10):
            for typeStr in self.entityTypes:
                t = self.entityTypes[typeStr]
                p = Positioning()
                p.x = float(randint(1,639))
                p.y = float(randint(1,479))
                p.orientation = -45
                inst = t(p)
                inst.toString()
                t.addToEntitySet(inst)



    def run(self, timeSpan):
        self.test = "test"
