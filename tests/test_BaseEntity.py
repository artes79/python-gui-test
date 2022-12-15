from Evolution.ModelClasses.BaseEntity import BaseEntity
from Evolution.ModelClasses.Biological.Plants.Grasses.GrassRustle import GrassRustle
from Evolution.ModelClasses.IBaseEntity import IBaseEntity
from Evolution.ModelClasses.IEntity import IEntity
import numpy as np

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


def test_addEntityToGroundTabel():
    rustle = GrassRustle()
    rustle.position.position = np.array([300, 300], dtype=float)
    BaseEntity.AddEntityToGround(rustle)
    assert BaseEntity.GetEntityFromGroundSquare(300, 300) == rustle


def test_isSquareOcupide():
    rustle = GrassRustle()
    rustle.position.position = np.array([300, 300], dtype=float)
    BaseEntity.AddEntityToGround(rustle)
    assert BaseEntity.IsGroundSquareOcupide(300, 300) is True
    assert BaseEntity.IsGroundSquareOcupide(290, 300) is False
    assert BaseEntity.IsGroundSquareOcupide(290, 290) is False
    assert BaseEntity.IsGroundSquareOcupide(300, 290) is False
    assert BaseEntity.IsGroundSquareOcupide(310, 290) is False
    assert BaseEntity.IsGroundSquareOcupide(310, 300) is False
    assert BaseEntity.IsGroundSquareOcupide(310, 310) is False
    assert BaseEntity.IsGroundSquareOcupide(300, 310) is False
    assert BaseEntity.IsGroundSquareOcupide(290, 310) is False
    rustle2 = GrassRustle()
    rustle2.position.position = np.array([654, 474], dtype=float)
    BaseEntity.AddEntityToGround(rustle2)
    assert BaseEntity.IsGroundSquareOcupide(654, 474) is True
    rustle3 = GrassRustle()
    rustle3.position.position = np.array([10, 10], dtype=float)
    BaseEntity.AddEntityToGround(rustle3)
    assert BaseEntity.IsGroundSquareOcupide(10, 10) is True