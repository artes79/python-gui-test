from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.IBaseEntity import IBaseEntity


# ModelClasses / BaseEntity

def test_inheritance():
    assert issubclass(BaseEntity, IBaseEntity)

def test_id():
    a = int(BaseEntity.generateId())
    b = int(BaseEntity.generateId())
    c = int(BaseEntity.generateId())
    assert b == a + 1
    assert c == b + 1
