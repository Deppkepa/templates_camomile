from src.Models.company_model import company_model

class Settings:
    __company: company_model = None

    @property 
    def company(self) -> company_model:
        return self.__company

    def __init__(self):
        self.__company = company_model()        