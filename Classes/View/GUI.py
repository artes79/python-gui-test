from tkinter import *
import time
from PIL import Image, ImageTk

class GUI:


    images = []

    def __init__(self, controler):
        self.controler = controler
        self.tkRoot = Tk()
        self.myCanvas = Canvas(self.tkRoot, bg="blue", height=240, width=320)
        self.myCanvas.pack()
        self.windowOpen = True
        self.tkRoot.protocol("WM_DELETE_WINDOW", self.on_closing)

    def draw(self):
        self.positionImage()
        self.myCanvas.create_image(0, 120, image=self.image, tag="image1")
        while self.windowOpen:
            self.controler.executeOneStep()
            self.drawElements()
            #self.myCanvas.delete("all")
            coords = self.myCanvas.coords("image1")
            self.myCanvas.move("image1", 0.1, 0)
            self.tkRoot.update()
            time.sleep(0.01)

    def on_closing(self):
        self.windowOpen = False

    def drawElements(self):
        self.test = "test"

    def positionImage(self):
        pilImage = Image.open("images/rock.png")
        image = ImageTk.PhotoImage(pilImage)
        self.images.append(image)

    def getImage(self, entity):
        name = type(entity).__name__
        i = AllEntitiesType[name].value
        return self.images[i]

    def drawEntities(self):
        for entity in BaseComponent.entitySet:
            if isinstance(entity, IDrawableEntity):
                if entity.drawnStatus is EntityStatus.NEW:
                    self.addEntityToCanvas(entity)
                elif entity.drawnStatus is EntityStatus.DRAWN:
                    self.moveEntityOnCanvas(entity)
                elif entity.drawnStatus is EntityStatus.TO_BE_DELETED:
                    self.removeEntityFromCanvas(entity)
                else:
                    pass

    def removeEntityFromCanvas(self, entity):
        self.myCanvas.delete(entity.id)

    def moveEntityOnCanvas(self, entity):
        self.myCanvas.moveto(entity.id,
                             entity.positioning.getX_asInt(),
                             entity.positioning.getY_asInt())

    def addEntityToCanvas(self, entity):
        self.myCanvas.create_image(entity.positioning.getX_asInt(),
                                   entity.positioning.getY_asInt(),
                                   image=self.getImage(entity),
                                   tag=entity.id)
        entity.drawnStatus = EntityStatus.DRAWN


