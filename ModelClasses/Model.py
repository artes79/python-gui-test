from DataClasses.Positioning import Positioning
from ModelClasses.BaseEntity import BaseEntity
from ModelClasses.Biological.Conzcious.Animals.Herbivores.Rabbit import Rabbit
from ModelClasses.Biological.Conzcious.Animals.Herbivores.RabbitFemale import RabbitFemale
from ModelClasses.Biological.Conzcious.Animals.Herbivores.Sheep import Sheep
from ModelClasses.Biological.Conzcious.Animals.Herbivores.SheepFemale import SheepFemale
from ModelClasses.Biological.Conzcious.Animals.Predators.Fox import Fox
from ModelClasses.Biological.Conzcious.Animals.Predators.FoxFemale import FoxFemale
from ModelClasses.Biological.Conzcious.Humans.Man import Man
from ModelClasses.Biological.Conzcious.Humans.Woman import Woman
from ModelClasses.Biological.Plants.Grass import Grass
from ModelClasses.IEntity import IEntity
from ModelClasses.IModel import IModel
from ModelClasses.Nonbiological.Rock import Rock
from ModelClasses.Nonbiological.Water import Water


class Model(IModel):

    @staticmethod
    def startGameModel(width: int, height: int):
        Positioning.setWorldSize(width, height)

        Water.createEntity()
        Grass.createEntity()
        Rock.createEntity()
        Man.createEntity()
        Woman.createEntity()
        Rabbit.createEntity()
        RabbitFemale.createEntity()
        Sheep.createEntity()
        SheepFemale.createEntity()
        Fox.createEntity()
        FoxFemale.createEntity()



    @staticmethod
    def getEntities(duration: float) -> list[type[IEntity]]:
        return BaseEntity.getEntities(duration)

    @staticmethod
    def getEntitiesWithScale(width: int, height: int) -> list[type[IEntity]]:
        BaseEntity.changeWorldSize(width, height)
        return Model.getEntities(0)
