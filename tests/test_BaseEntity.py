from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.IBaseEntity import IBaseEntity


# ModelClasses / BaseEntity

def test_inheritance():
    assert issubclass(BaseEntity, IBaseEntity)
