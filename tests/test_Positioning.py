from Evolution.DataClasses.IPositioning import IPositioning
from Evolution.DataClasses.Positioning import Positioning


instants = [Positioning(), Positioning(), Positioning()]


def test_inheritance():
    assert issubclass(Positioning, IPositioning)


def test_returnX():
    for inst in instants:
        assert isinstance(inst.x, float)
        v = inst.x
        assert v == inst.x


def test_returnXRound():
    for inst in instants:
        assert isinstance(inst.xRound, float)
        v = inst.x
        vRound = inst.xRound
        assert (v - 0.5) <= vRound <= (v + 0.5)
        assert vRound == int(vRound)


def test_returnY():
    for inst in instants:
        assert isinstance(inst.y, float)
        v = inst.y
        assert v == inst.y


def test_returnYRound():
    for inst in instants:
        assert isinstance(inst.yRound, float)
        v = inst.y
        vRound = inst.yRound
        assert (v - 0.5) <= vRound <= (v + 0.5)
        assert vRound == int(v)