import numpy as np
from Evolution.DataClasses.WorldData import WorldData

instances = [WorldData(), WorldData(), WorldData()]


def test_size():
    for inst in instances:
        assert isinstance(inst.size, np.ndarray)
        w = inst.size[0]
        assert w == inst.width
        h = inst.size[1]
        assert h == inst.height
        newSize = np.array([480, 640], dtype=float)
        inst.size = newSize
        assert np.all([inst.size, newSize])
        assert inst.width == newSize[0]
        assert inst.height == newSize[1]


def test_width():
    for inst in instances:
        assert isinstance(inst.width, int)
        w = inst.width
        assert w == inst.width
        assert w >= 200



def test_height():
    for inst in instances:
        assert isinstance(inst.height, int)
        h = inst.height
        assert h == inst.height
        assert h >= 200
