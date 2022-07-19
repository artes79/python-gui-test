from Classes.Model.BaseComponent import *
import time


class Living(BaseComponent):

    def __init__(self):
        self.birth = time.time()


    def GetAge(self):
        return time.time() - self.birth
