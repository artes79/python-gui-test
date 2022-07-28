from tkinter import *
import time
from PIL import Image, ImageTk
from Classes import *
from Classes.Model import *
from Interface import *
from Enums import *
import copy


class GUI:

    images = []

    def __init__(self, controler, imageData: dict):
        self.controler = controler
        self.createGUI()
        self.loadImages(imageData)
        self.windowOpen = True

    def createGUI(self):
        self.tkRoot = Tk()
        self.myCanvas = Canvas(self.tkRoot, bg="green", height=480, width=640)
        self.myCanvas.pack()
        self.tkRoot.protocol("WM_DELETE_WINDOW", self.on_closing)

    def draw(self):
        while self.windowOpen:
            self.controler.executeOneStep()
            self.drawEntities()
            self.tkRoot.update()
            time.sleep(0.01)

    def on_closing(self):
        self.windowOpen = False

    def loadImages(self, imageData: dict):
        for key, value  in imageData.items():
            pilImage = Image.open(value["normal"]["image_path"])
            image = ImageTk.PhotoImage(pilImage)
            value["normal"]["image"] = image
            #self.images.append(image)
            print(imageData[key])
        self.imageData = imageData

    def positionImage(self):
        pilImage = Image.open("images/rock.png")
        image = ImageTk.PhotoImage(pilImage)
        self.images.append(image)

    def getImage(self, entity):
        name = type(entity).__name__
        #i = AllEntitiesType[name].value
        print("getImage " + name)
        return self.imageData[name]["normal"]["image"]

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
        entity.drawnStatus = EntityStatus.REMOVED_FROM_CANVAS

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


