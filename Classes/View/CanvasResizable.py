# Kode is from:
# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width
# posted by ebarr https://stackoverflow.com/users/821672/ebarr

from Classes.Controler import *
from tkinter import *


class CanvasResizable(Canvas):

    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        self.width = event.width
        self.height = event.height
        self.config(width=self.width, height=self.height)
        Controler.setGameBoardSize(self.width, self.height)


