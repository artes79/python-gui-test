from DataClasses.IPositioning import IPositioning, IPositioningUser
from PIL import Image, ImageTk
from tkinter import PhotoImage


class IEntity(IPositioningUser):

    @property
    def position(self) -> IPositioning:
        pass

    @property
    def portrait(self) -> PhotoImage:
        pass

    @staticmethod
    def createEntity() -> None:
        pass


class IEntityShared:

    def loadPortrait(self, path: str) -> PhotoImage:
        pass
