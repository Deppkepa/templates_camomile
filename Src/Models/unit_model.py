from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator
from Src.Core.entity_model import entity_model

"""
Модель единицы измерения
"""

class unit_model(entity_model):
    __coeff_recalculation: int = None #  единица пересчета
    __base_unit: 'unit_model' = None # базовая единица изрения

    def __init__(self, name_unit, coeff_recalculation, base_unit=None):
        super().__init__()
        self.name = name_unit
        self.__coeff_recalculation = coeff_recalculation
        self.__base_unit = base_unit

    @property
    def base_unit(self) -> int:
        return self.__base_unit
    
    @base_unit.setter
    def base_unit(self, value: int):
        validator.validate(value, int)
        self.__base_unit = value


    @property
    def coeff_recalculation(self) -> 'unit_model':
        return self.__coeff_recalculation
    
    @coeff_recalculation.setter
    def coeff_recalculation(self, value: 'unit_model'):
        validator.validate(value, unit_model)
        self.__coeff_recalculation = value

    """
    Киллограмм
    """
    @staticmethod
    def create_kill():
        inner_gramm = unit_model.create_gramm()
        return unit_model.create("киллограмм", inner_gramm)

    """
    Грамм
    """
    @staticmethod
    def create_gramm():
        return unit_model.create("грамм")
    
     
    """
    Универсальный метод - фабричный
    """
    @staticmethod
    def create(name:str, base=None):
        validator.validate(name, str)
        if not base is None:
            validator.validate(base, unit_model)
        item = unit_model(name, base)
        return item


    