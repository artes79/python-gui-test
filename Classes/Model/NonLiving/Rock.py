from Classes.Model.NonLiving import *
from Dataclasses import *
from random import randint


class Rock(NonLiving):

    def __init__(self, positioning: Positioning):

        spatial = SpatialProperties
        spatial.radius = 0.6
        spatial.height = 1

        super().__init__(positioning, spatial)

        self.spatialProperties.radius = self.calculateDiameter()
        print("r: " + str(self.spatialProperties.radius))

    def calculateDiameter(self) -> float:
        haveDoneFirstEntity = False
        minDistance = 0
        for id, entity in enumerate(Rock.entitySet):
            if entity.spatialProperties.height > 0.1:
                d = self.calculateDistanceTo(entity)
                print("dist: " + str(d))
                if d <= 0:
                    self.remove()
                    return 0
                if not haveDoneFirstEntity:
                    minDistance = d
                    haveDoneFirstEntity = True
                if minDistance > d:
                    minDistance = d
        m = min(minDistance, 15)
        return randint(500, 100*(m+5)+1) / 100

