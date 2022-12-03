from Evolution.ModelClasses.IBaseEntity import IBaseEntity


class BaseEntity(IBaseEntity):

    lastGeneratdId: int = 0

    @staticmethod
    def generateId() -> str:
        BaseEntity.lastGeneratdId += 1
        return BaseEntity.lastGeneratdId