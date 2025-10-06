from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.unit_model import unit_model

"""
Модель номенклатуры
"""

class nomenclature_model(abstract_reference):
    __group_nomenclature: group_nomenclature_model = None
    __unit: unit_model = None

    @property
    def group_nomenclature(self) -> group_nomenclature_model:
        return self.__group_nomenclature
    
    @group_nomenclature.setter
    def group_nomenclature(self, value: str):
        validator.validate(value, group_nomenclature_model)
        self.__group_nomenclature = value


    @property
    def unit(self) -> unit_model:
        return self.__unit
    
    @unit.setter
    def unit(self, value: str):
        validator.validate(value, unit_model)
        self.__unit = value

    
    '''
    Фабричный метод для создания номеклатур
    '''
    @staticmethod
    def create(name:str, group_nomenclature:group_nomenclature_model, unit:unit_model):
        validator.validate(name, str)
        validator.validate(group_nomenclature, group_nomenclature_model)
        validator.validate(unit, unit_model)
        item = nomenclature_model()
        item.name = name
        item.group_nomenclature = group_nomenclature
        item.unit = unit
        return item