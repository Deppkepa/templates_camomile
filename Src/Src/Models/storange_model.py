from Src.Core.validator import validator
from Src.Core.abstract_reference import abstract_reference
from Src.Core.entity_model import entity_model

"""
Модель склада
"""
class storage_model(entity_model):
    __address:str = ""

    """
    Адрес
    """
    @property
    def address(self) -> str:
        return self.__address.strip()
    
    @address.setter
    def address(self, value:str):
        validator.validate(value, str)
        self.__address = value.strip()
    
    
    