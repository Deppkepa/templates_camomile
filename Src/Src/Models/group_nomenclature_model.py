from Src.Core.entity_model import entity_model
from Src.Core.validator import validator

"""
Модель группы номенклатуры
"""

class group_nomenclature_model(entity_model):

    def __init__(self, name:str= None):
        super().__init__()
        validator.validate(name, str)
        self.name = name