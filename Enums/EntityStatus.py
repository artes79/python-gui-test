from enum import Enum


class EntityStatus(Enum):
    NEW = 0
    DRAWN = 1
    TO_BE_DELETED = 2
    REMOVED_FROM_CANVAS = 3