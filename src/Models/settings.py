class Settings:
    __company_name: str = ""
    __inn:str = ""
    __acc:str = ""
    __correspondent_acc:str = ""
    __bic:str = ""
    __ownership:str = ""

    def __init__(self, value:dict):
        if "name" in value:
            self.__company_name = value["name"]
        if "inn" in value:
            self.__inn = value["inn"]
        if "acc" in value:
            self.__acc = value["acc"]
        if "correspondent_acc" in value:
            self.__correspondent_acc = value["correspondent_acc"]
        if "bic" in value:
            self.__bic = value["bic"]
        if "ownership" in value:
            self.__ownership = value["ownership"]

    @property
    def company_name(self) -> str:
        return self.__company_name
    
    @company_name.setter
    def company_name(self, value:str):
        if value.strip() != "":
            self.__company_name = value.strip()

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