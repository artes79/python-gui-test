import numpy as np
from Evolution.DataClasses.IPositioning import IPositioning
from Evolution.DataClasses.Positioning import Positioning
from Evolution.DataClasses.WorldData import WorldData

instants = [Positioning(), Positioning(), Positioning()]


def test_inheritance():
    assert issubclass(Positioning, IPositioning)


def test_returnX():
    for inst in instants:
        assert isinstance(inst.x, float)
        v = inst.x
        assert v == inst.x
        assert v >= 0
        assert v < Positioning.GetWorld().width


def test_returnXRound():
    for inst in instants:
        assert isinstance(inst.xRound, float)
        v = inst.x
        vRound = inst.xRound
        assert (v - 0.5) <= vRound <= (v + 0.5)
        assert vRound == int(vRound)
        assert vRound >= 0



def test_returnY():
    for inst in instants:
        assert isinstance(inst.y, float)
        v = inst.y
        assert v == inst.y
        assert v >= 0
        assert v < Positioning.GetWorld().height


def test_returnYRound():
    for inst in instants:
        assert isinstance(inst.yRound, float)
        v = inst.y
        vRound = inst.yRound
        assert (v - 0.5) <= vRound <= (v + 0.5)
        assert vRound == int(v)
        assert vRound >= 0


def test_world():
    w = WorldData()
    size = np.array([360, 480], dtype=float)
    w.size = size
    Positioning.SetWorld(w)
    assert Positioning.GetWorld() == w
    assert Positioning.GetWorld().width == w.width
    assert Positioning.GetWorld().height == w.height

