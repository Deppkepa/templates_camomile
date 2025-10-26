from abc import ABC
import uuid
from Src.Core.validator import validator


'''
Абстрактный класс для наследования моделей
Содержит в себе только генерацию уникального кода
'''
class abstract_reference(ABC):
    __name:str = ""
    __unique_code:str = ""

    def __init__(self) -> None:
        super().__init__()
        self.unique_code = uuid.uuid4().hex

    """
    Уникальный код
    """
    @property
    def unique_code(self) -> str:
        return self.__unique_code
    
    @unique_code.setter
    def unique_code(self, value: str):
        validator.validate(value, str)
        self.__unique_code = value.strip()
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        validator.validate(value, str, 50, "le")
        self.__name = value
    

    """
    Перегрузка штатного варианта сравнения
    """
    def __eq__(self, value: str) -> bool:
        return self.__unique_code == value

    def __str__(self):
        return super().__str__()
    
    def __ne__(self, value):
        return self.__unique_code != value
    
    