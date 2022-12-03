from Evolution.ModelClasses.IBaseEntity import IBaseEntity
from Evolution.ModelClasses.IEntity import IEntities


# ModelClasses / IBaseEntity

def test_inheritance():
    assert issubclass(IBaseEntity, IEntities)
