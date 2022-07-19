from tkinter import *

class GUI:


    def __init__(self, controler):
        self.controler = controler
        self.tkRoot = Tk()
        self.myCanvas = Canvas(self.tkRoot, bg="blue", height=240, width=320)
        self.myCanvas.pack()
        self.windowOpen = True
        self.tkRoot.protocol("WM_DELETE_WINDOW", self.on_closing)

    def draw(self):
        self.tkRoot.mainloop()