from Evolution.ModelClasses.IModel import IModel
from Evolution.ModelClasses.Model import Model


# ModelClasses / Model.py

def test_inheritance():
    assert issubclass(Model, IModel)


def test_construction():
    m = Model()
    assert isinstance(m, Model)
