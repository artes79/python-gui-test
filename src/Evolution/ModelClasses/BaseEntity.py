from Evolution.ModelClasses.IBaseEntity import IBaseEntity
from PIL import Image
from PIL.ImageTk import PhotoImage

class BaseEntity(IBaseEntity):

    _lastGeneratdId: int = 0

    @staticmethod
    def GenerateId() -> str:
        BaseEntity._lastGeneratdId += 1
        return str(BaseEntity._lastGeneratdId)

    @staticmethod
    def LoadPortrait(path: str) -> PhotoImage:
        pilImage = Image.open(path)
        return PhotoImage(pilImage)