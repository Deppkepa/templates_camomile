from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator
from Src.Models.groupNomenclature_model import groupNomenclature_model
from Src.Models.unit_model import unit_model

class nomenclature_model(abstract_reference):
    __group_nomenclature: groupNomenclature_model = None
    __unit: unit_model = None

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

    def create_spaghetti():
        unit = unit_model("грамм", 200)
        group = groupNomenclature_model("Макаронные изделия")
        return nomenclature_model().create("спагетти", group, unit)
    
    def create_garlic():
        unit = unit_model("грамм", 12)
        group = groupNomenclature_model("Овощи")
        return nomenclature_model().create("Чеснок", group, unit)
    
    def create_olive_oil():
        unit = unit_model("мл", 45)
        group = groupNomenclature_model("Масло")
        return nomenclature_model().create("Оливковое масло", group, unit)
    
    def create_salt():
        unit = unit_model("грамм", 15)
        group = groupNomenclature_model("Специи")
        return nomenclature_model().create("Соль", group, unit)
    
    def create_pepper():
        unit = unit_model("грамм", 15)
        group = groupNomenclature_model("Специи")
        return nomenclature_model().create("Перец", group, unit)

    @staticmethod
    def create(name:str, group_nomenclature:groupNomenclature_model, unit:unit_model):
        validator.validate(name, str)
        validator.validate(group_nomenclature, groupNomenclature_model)
        validator.validate(unit, unit_model)
        item = nomenclature_model()
        item.name = name
        item.group_nomenclature = group_nomenclature
        item.unit = unit
        return item