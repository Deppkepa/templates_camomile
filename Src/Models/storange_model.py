from Src.Core.validator import validator
from Src.Core.abstract_reference import abstract_reference

"""
Модель склада
"""
class storage_model(abstract_reference):
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
    
    
    