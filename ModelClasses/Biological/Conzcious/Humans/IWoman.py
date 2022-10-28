from ModelClasses.Biological.Conzcious.IHuman import IHuman
from ModelClasses.IBreedable import IBreedable
from ModelClasses.IEntity import IEntity


class IWoman(IHuman, IEntity, IBreedable):
    pass
