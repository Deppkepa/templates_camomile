
###############################################
# Модель организации
class company_model:
    __name:str = ""
    __inn:int = None # 12 чисел
    __acc:int = None # 11 чисел
    __correspondent_acc:int = None # 11 чисел
    __bic:int = None # 5 чисел
    __ownership:str = ""

    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str):
        if value.strip() != "":
            self.__name = value.strip()
        else:
            raise ValueError("Не правильное имя")

    @property
    def inn(self) -> int:
        return self.__inn
    
    @inn.setter
    def inn(self, value:int):
        if value != None and len(str(value)) == 12:
            self.__inn = value
        else:
            raise ValueError("'inn' должен состоять из 12 символов")
    
    @property
    def acc(self) -> int:
        return self.__acc
    
    @acc.setter
    def acc(self, value:int):
        if value != None and len(str(value)) == 11:
            self.__acc = value
        else:
            raise ValueError("'acc' должен состоять из 11 символов")

    @property
    def correspondent_acc(self) -> int:
        return self.__correspondent_acc
    
    @correspondent_acc.setter
    def correspondent_acc(self, value:int):
        if value != None and len(str(value)) == 11:
            self.__correspondent_acc = value
        else:
            raise ValueError("'correspondent_acc' должен состоять из 11 символов")

    @property
    def bic(self) -> int:
        return self.__bic
    
    @bic.setter
    def bic(self, value:int):
        if value != None and len(str(value)) == 9:
            self.__bic = value
        else:
            raise ValueError("'bic' должен состоять из 9 символов")

    @property
    def ownership(self) -> str:
        return self.__ownership
    
    @ownership.setter
    def ownership(self, value:str):
        if value.strip() != "" and len(value) == 5:
            self.__ownership = value.strip()
        else:
            raise ValueError("'ownership' должен состоять из 5 символов")


