from Evolution.ModelClasses.Biological.Plants.Grasses.IGrassRustle import IGrassRustle
from Evolution.ModelClasses.IEntity import IEntity


def test_inheritance():
    assert issubclass(IGrassRustle, IEntity)
