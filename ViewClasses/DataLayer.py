import tkinter as gui


class DataLayer:

    @staticmethod
    def initLayer(infoLayer: gui.Canvas):
        infoLayer.create_text(100, 100, text="Canvas text", tags="Datalayer")
        infoLayer.create_text(100, 120, text="Level 12", tags="Datalayer")

    @staticmethod
    def run():
        pass

    @staticmethod
    def arangeDataItems():
        pass
