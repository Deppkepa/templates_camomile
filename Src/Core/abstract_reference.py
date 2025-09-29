from abc import ABC
import uuid
from Src.Core.validator import validator

class abstract_reference(ABC):
    __usual_name:str
    __unique_code:str

    def __init__(self) -> None:
        super().__init__()
        self.__unique_code = uuid.uuid4().hex

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
    def usual_name(self) -> str:
        return self.__usual_name
    
    @usual_name.setter
    def usual_name(self, value: str):
        validator.validate(value, str, 50, "le")
        self.__usual_name = value
    

    """
    Перегрузка штатного варианта сравнения
    """
    def __eq__(self, value: str) -> bool:
        return self.__unique_code == value

    def __str__(self):
        return super().__str__()
    
    def __ne__(self, value):
        return self.__unique_code != value