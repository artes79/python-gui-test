from ModelClasses.IBaseEntity import IBaseEntity


class BaseEntity(IBaseEntity):

    _lastIdNumber: int = 0
    _id: str

    @property
    def id(self) -> str:
        return self._id

    def __init__(self):
        self._id = BaseEntity.generateId(self)

    @staticmethod
    def generateId(inst) -> str:
        name = type(inst).__name__
        BaseEntity.lastIdNumber += 1
        return name + str(BaseEntity.lastIdNumber)
