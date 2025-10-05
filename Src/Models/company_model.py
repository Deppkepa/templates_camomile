from Src.Core.validator import validator
from Src.Core.abstract_reference import abstract_reference

###############################################
# Модель организации
class company_model(abstract_reference):
    __name:str = ""
    __inn:int = None # ИНН : 12 симв
    __acc:int = None # Счет 11 симв
    __correspondent_acc:int = None # 1Корреспондентский счет 11 симв
    __bic:int = None # Вид собственности 5 симв
    __ownership:str = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str):
        validator.validate(value, str)
        self.__name = value


    @property
    def inn(self) -> int:
        return self.__inn
    
    @inn.setter
    def inn(self, value:int):
        validator.validate(value, int, 12)
        self.__inn = value
    

    @property
    def acc(self) -> int:
        return self.__acc
    
    @acc.setter
    def acc(self, value:int):
        validator.validate(value, int, 11)
        self.__acc = value


    @property
    def correspondent_acc(self) -> int:
        return self.__correspondent_acc
    
    @correspondent_acc.setter
    def correspondent_acc(self, value:int):
        validator.validate(value, int, 11)
        self.__correspondent_acc = value
        

    @property
    def bic(self) -> int:
        return self.__bic
    
    @bic.setter
    def bic(self, value:int):
        validator.validate(value, int, 9)
        self.__bic = value
        

    @property
    def ownership(self) -> str:
        return self.__ownership
    
    @ownership.setter
    def ownership(self, value:str):
        validator.validate(value, str, 5)
        self.__ownership = value
        
