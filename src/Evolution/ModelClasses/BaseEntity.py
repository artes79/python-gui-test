from Evolution.ModelClasses.IBaseEntity import IBaseEntity


class BaseEntity(IBaseEntity):

    _lastGeneratdId: int = 0

    @staticmethod
    def GenerateId() -> str:
        BaseEntity._lastGeneratdId += 1
        return str(BaseEntity._lastGeneratdId)