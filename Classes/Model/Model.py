#from Classes import *
from Classes.Model.Living import *
from Classes.Model import *
from DataStorageClasses import *
from random import randint


class Model(object):

    gameBoard = {
        "width": 640,
        "height": 480,
    }


    def __init__(self, typeData: dict):
        self.propagateEntities(typeData)

    def propagateEntities(self, typeData: dict):
        for tKey, tData in typeData.items():
            #tData = typeData[tIndex]
            print(tData)
            t = eval(tKey)
            print(t)
            for _ in range(tData["init_count"]):
                argList: list = []
                for property, value in tData["propertys"].items():
                    pt = eval(property)
                    print(pt)
                    p = pt()
                    for key, value in tData["propertys"][property].items():
                        setattr(p,
                                key,
                                self.convertValue(value))
                        print(key + " " + value)
                    argList.append(p)
                print(argList)
                inst = t(argList)
                t.addToEntitySet(inst)
        #
        # for _ in range(100):
        #     for typeStr in self.entityTypes:
        #         t = self.entityTypes[typeStr]
        #         p = Positioning()
        #         p.x = float(randint(1,639))
        #         p.y = float(randint(1,479))
        #         p.orientation = -45
        #         print(setattr(p, "x", 200))
        #         print(p.x)
        #         #inst = t(p)
        #         #inst.toString()
        #         #t.addToEntitySet(inst)

    def convertValue(self, value: str):

        if value is "randScreen":
            return 60
        return 50

    def run(self, timeSpan):
        pass


    @staticmethod
    def setGameBoardSize(width: int, height: int):
        pass
