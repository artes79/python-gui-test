from Evolution.DataClasses.IPositioning import IPositioning
from PIL.ImageTk import PhotoImage

class IEntity:

    @property
    def id(self) -> str:
        pass

    @property
    def position(self) -> IPositioning:
        pass

    @property
    def portrait(self) -> PhotoImage:
        pass


class IEntities:

    @staticmethod
    def generateId() -> str:
        pass

    @staticmethod
    def LoadPortrait(path: str) -> PhotoImage:
        pass