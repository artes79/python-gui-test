from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.Biological.Plants.Grasses.GrassRustle import GrassRustle
from Evolution.ModelClasses.Biological.Plants.Grasses.IGrassRustle import IGrassRustle
from Evolution.ModelClasses.IEntity import IEntity


instants = [GrassRustle(), GrassRustle(), GrassRustle()]


def test_inheritance():
    assert issubclass(GrassRustle, IGrassRustle)
    assert issubclass(GrassRustle, IEntity)
    assert issubclass(GrassRustle, BaseEntity)


def test_getId():
    for instA in instants:
        for instB in instants:
            if instA == instB:
                assert instA.id == instB.id
            else:
                assert instA.id != instB.id

def test_generateId():
    idA = GrassRustle.GenerateId()
    idB = GrassRustle.GenerateId()
    assert idA != idB
    assert idA.startswith("Rustle")
    assert idB.startswith("Rustle")
