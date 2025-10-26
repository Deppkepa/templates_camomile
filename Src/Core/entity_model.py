from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator


"""
Общий класс для наследования. Содержит стандартное определение: код, наименование
"""
class entity_model(abstract_reference):
    __name:str = ""

    def __init__(self):
        super().__init__()
    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str) -> str:
        validator.validate(value, str)
        self.__name = value.strip()
    
    # Фабричный метод
    @staticmethod
    def create(name:str):
        item = entity_model()
        item.name = name
        return item