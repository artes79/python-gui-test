from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.Biological.Plants.Grasses.GrassRustle import GrassRustle
from Evolution.ModelClasses.IBaseEntity import IBaseEntity
from Evolution.ModelClasses.IEntity import IEntity


# ModelClasses / BaseEntity

def test_inheritance():
    assert issubclass(BaseEntity, IBaseEntity)


def test_id():
    a = int(BaseEntity.GenerateId())
    b = int(BaseEntity.GenerateId())
    c = int(BaseEntity.GenerateId())
    assert b == a + 1
    assert c == b + 1


def test_getEntities():
    assert isinstance(BaseEntity.GetEntities(), list)


def test_addEntity():
    rustle1 = GrassRustle()
    rustle2 = GrassRustle()
    BaseEntity.AddEntity(rustle1)
    BaseEntity.AddEntity(rustle2)
    entities = BaseEntity.GetEntities()
    assert entities[len(entities) - 2] == rustle1
    assert entities[len(entities) - 1] == rustle2


def test_getEntitiesContains():
    for entity in BaseEntity.GetEntities():
        assert isinstance(entity, IEntity)
