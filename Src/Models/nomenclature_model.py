from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator
from Src.Models.groupNomenclature_model import groupNomenclature_model
from Src.Models.unit_model import unit_model

class nomenclature_model(abstract_reference):
    __full_name: str = ""
    __group_nomenclature: groupNomenclature_model = None
    __unit: unit_model = None

    @property
    def full_name(self) -> str:
        return self.__full_name
    
    @full_name.setter
    def full_name(self, value: str):
        validator.validate(value, str, 256, "le")
        self.__full_name = value


    @property
    def group_nomenclature(self) -> groupNomenclature_model:
        return self.__group_nomenclature
    
    @group_nomenclature.setter
    def group_nomenclature(self, value: str):
        validator.validate(value, groupNomenclature_model)
        self.__group_nomenclature = value


    @property
    def unit(self) -> unit_model:
        return self.__unit
    
    @unit.setter
    def unit(self, value: str):
        validator.validate(value, unit_model)
        self.__unit = value