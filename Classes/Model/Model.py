from Classes import *
from Classes.Model.Living import *
from Classes.Model import *
from random import randint


class Model(object):

    entityTypes = {
        "Rock": Rock,
        "Gress": Gress
    }

    def __init__(self, typeData: dict):
        self.propagateEntities(typeData)

    def propagateEntities(self, typeData: dict):
        for tKey, tData in typeData.items():
            #tData = typeData[tIndex]
            print(tData)
            t = eval(tKey)
            for _ in range(tData["init_count"]):
                argList: list = ["test"]
                for property, value in tData["propertys"].items():
                    pt = eval(property)
                    print(pt)
                    p = pt()
                    print(getattr(p, "x"))
                    for attrIndex in tData["propertys"][property]:
                        setattr(p,
                                tData["propertys"][property][attrIndex],
                                float(randint(1,400)))
                    argList.append(p)
                print(argList)
                inst = t(argList)

        for _ in range(100):
            for typeStr in self.entityTypes:
                t = self.entityTypes[typeStr]
                p = Positioning()
                p.x = float(randint(1,639))
                p.y = float(randint(1,479))
                p.orientation = -45
                print(setattr(p, "x", 200))
                print(p.x)
                #inst = t(p)
                #inst.toString()
                #t.addToEntitySet(inst)




    def run(self, timeSpan):
        self.test = "test"
