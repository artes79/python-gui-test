import numpy as np
from Evolution.DataClasses.IPositioning import IPositioning
from Evolution.DataClasses.PhysicalData import PhysicalData
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


def test_physical():
    for inst in instants:
        p = inst.physical
        assert isinstance(p, PhysicalData)
        assert p == inst.physical
        e = np.array([2.7, 4.5], dtype=float)
        inst.physical.extent = e
        assert np.all([np.equal(e, inst.physical.extent), [True, True]])


def test_position():
    for inst in instants:
        p = np.array([360, 240], dtype=float)
        inst.position = p
        assert p[0] == inst.x
        assert p[1] == inst.y
        assert np.all([np.equal(p, inst.position), [True, True]])


def test_previousPosition():
    for inst in instants:
        p1 = np.array([256,512], dtype=float)
        p2 = np.array([125,420], dtype=float)
        inst.position = p1
        inst.position = p2
        assert np.all([np.equal(inst.previousPosition, p1), [True, True]])


def test_randomPosition():
    for inst in instants:
        inst.SetRandomPosition()
        p1 = inst.position
        inst.SetRandomPosition()
        p2 = inst.position
        assert not np.all([np.equal(p1, p2), [True, True]])
        insideWorld(p1, inst.GetWorld())
        insideWorld(p2, inst.GetWorld())


def insideWorld(p: np.ndarray, world: WorldData):
    assert p[0] >= 0
    assert p[1] >= 0
    assert p[0] < world.width
    assert p[1] < world.height
