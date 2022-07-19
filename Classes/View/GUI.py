from tkinter import *
import time
from PIL import Image, ImageTk

class GUI:



    def __init__(self, controler):
        self.controler = controler
        self.tkRoot = Tk()
        self.myCanvas = Canvas(self.tkRoot, bg="blue", height=240, width=320)
        self.myCanvas.pack()
        self.windowOpen = True
        self.tkRoot.protocol("WM_DELETE_WINDOW", self.on_closing)

    def draw(self):
        self.positionImage()
        while self.windowOpen:
            self.controler.executeOneStep()
            self.drawElements()
            self.tkRoot.update()
            time.sleep(0.017)

    def on_closing(self):
        self.windowOpen = False

    def drawElements(self):
        self.test = "test"

    def positionImage(self):
        pilImage = Image.open("icon-192.png")
        self.image = ImageTk.PhotoImage(pilImage)
        self.myCanvas.create_image(160, 120, image=self.image, size=None)
