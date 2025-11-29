from Src.Core.abstract_dto import abstract_dto
from Src.Core.filter_type import filter_type
from Src.Core.validator import validator

# Фильтрация
# класс для хранения типов фильтеров

class filter_dto(abstract_dto):
    __field_name:str = "" # Поле, по которому фильтруем
    __value:str = "" # Значение для фильтрации
    __filter_type: filter_type = None


    @property
    def field_name(self) -> str:
        return self.__field_name
    
    @field_name.setter
    def field_name(self, value:str):
        self.__field_name = value

    @property
    def value(self) -> str:
        return self.__value
    
    @value.setter
    def value(self, value:str):
        self.__value = value

    @property
    def filter_type(self) -> str:
        return self.__filter_type
    
    @filter_type.setter
    def filter_type(self, value:str):
        
        self.__filter_type = value

    def create():
        pass