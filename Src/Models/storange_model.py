import uuid
from Src.Core.validator import validator
from Src.Core.abstract_reference import abstract_reference

class storage_model(abstract_reference):
    __name:str = ""

    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str):
        validator.validate(value, str)
        self.__name = value.strip()
    
    
    