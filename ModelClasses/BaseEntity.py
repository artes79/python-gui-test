from ModelClasses.IEntity import IEntity


class BaseEntity(IEntity):

    lastIdNumber: int = 0

    def __init__(self):
        self.id = BaseEntity.generateId(self)

    @staticmethod
    def generateId(inst):
        name = type(inst).__name__
        BaseEntity.lastIdNumber += 1
        return name + str(BaseEntity.lastIdNumber)
