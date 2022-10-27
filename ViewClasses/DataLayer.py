import tkinter as gui


class DataLayer:

    @staticmethod
    def initLayer(infoLayer: gui.Canvas):
        infoLayer.create_text(100, 100, text="Canvas text", tags="info-layer")
        infoLayer.create_text(100, 120, text="Level 12", tags="info-layer")

    @staticmethod
    def run():
        pass

    @staticmethod
    def arangeDataItems():
        pass
