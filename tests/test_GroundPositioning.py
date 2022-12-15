import numpy as np
from Evolution.DataClasses.GroundPositioning import GroundPositioning
from Evolution.DataClasses.PhysicalData import PhysicalData
from Evolution.DataClasses.WorldData import WorldData
from Evolution.ModelClasses.Biological.Plants.Grasses.GrassRustle import GrassRustle

instances = [GroundPositioning(), GroundPositioning(), GroundPositioning()]
entity = GrassRustle()

def test_set_random_position():
    for inst in instances:
        inst.physical.extent = np.array([7.5, 7.5], dtype=float)
        inst.SetRandomPosition(entity)
        p1 = inst.position
        inst.SetRandomPosition(entity)
        p2 = inst.position
        assert not np.all([np.equal(p1, p2), [True, True]])
        insideWorld(p1, inst.physical, inst.GetWorld())
        insideWorld(p2, inst.physical, inst.GetWorld())


def insideWorld(p: np.ndarray, physical: PhysicalData, world: WorldData):
    assert p[0] >= physical.extent[0]
    assert p[1] >= physical.extent[1]
    assert p[0] < world.width - physical.extent[0]
    assert p[1] < world.height - physical.extent[1]
    #assert p[0] == np.round((p[0] - physical.extent[0]) / (physical.extent[0] * 2)) * (physical.extent[0] * 2) + physical.extent[0]
    #assert p[1] == np.round((p[1] - physical.extent[1]) / (physical.extent[1] * 2)) * (physical.extent[1] * 2) + physical.extent[1]