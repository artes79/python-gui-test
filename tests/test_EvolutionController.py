from Evolution.EvolutionController import EvolutionController
from Evolution.IEvolutionController import IEvolutionController


# Evolution Controller

def test_inheritance():
    assert issubclass(EvolutionController, IEvolutionController)


def test_construction():
    e = EvolutionController()
    assert isinstance(e, EvolutionController)
    assert isinstance(e, IEvolutionController)
