import numpy as np
from Evolution.DataClasses.IPhysicalData import IPhysicalData
from Evolution.DataClasses.PhysicalData import PhysicalData

instances = [PhysicalData(), PhysicalData(), PhysicalData()]


def test_inheritance():
    assert issubclass(PhysicalData, IPhysicalData)


def test_extent():
    for inst in instances:
        e1 = inst.extent
        assert isinstance(e1, np.ndarray)
        assert np.all([np.equal(e1, inst.extent), [True, True]])
        assert e1[0] > 0
        assert e1[1] > 0
        e2 = np.array([7.5, 7.5], dtype=float)
        inst.extent = e2
        assert np.all([np.equal(e2, inst.extent), [True, True]])
