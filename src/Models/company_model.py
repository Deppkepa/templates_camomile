
###############################################
# Модель организации
class company_model:
    __name:str = ""
    __inn:str = ""
    __acc:str = ""
    __correspondent_acc:str = ""
    __bic:str = ""
    __ownership:str = ""

    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str):
        if value.strip() != "":
            self.__name = value.strip()

    @property
    def inn(self) -> str:
        return self.__inn
    
    @inn.setter
    def inn(self, value:str):
        if value.strip() != "" and len(value) == 12:
            self.__inn = value.strip()
        else:
            raise ValueError("'inn' должен состоять из 12 символов")
    
    @property
    def acc(self) -> str:
        return self.__acc
    
    @acc.setter
    def acc(self, value:str):
        if value.strip() != "" and len(value) == 11:
            self.__acc = value.strip()
        else:
            raise ValueError("'acc' должен состоять из 11 символов")

    @property
    def correspondent_acc(self) -> str:
        return self.__correspondent_acc
    
    @correspondent_acc.setter
    def correspondent_acc(self, value:str):
        if value.strip() != "" and len(value) == 11:
            self.__correspondent_acc = value.strip()
        else:
            raise ValueError("'correspondent_acc' должен состоять из 11 символов")

    @property
    def bic(self) -> str:
        return self.__bic
    
    @bic.setter
    def bic(self, value:str):
        if value.strip() != "" and len(value) == 9:
            self.__bic = value.strip()
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


