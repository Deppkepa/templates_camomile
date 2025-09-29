from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator

class unit_model(abstract_reference):
    __name_unit:str = "" # название единицы измерения 
    __coeff_recalculation: int = None #  единица пересчета
    __base_unit: 'unit_model' = None # базовая единица изрения

    def __init__(self, name_unit, coeff_recalculation, base_unit=None):
        self.__name_unit = name_unit
        self.__coeff_recalculation = coeff_recalculation
        self.__base_unit = base_unit
        
        

    @property
    def name_unit(self) -> str:
        return self.__name_unit
    
    @name_unit.setter
    def name_unit(self, value: str):
        validator.validate(value, str)
        self.__name_unit = value


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


    