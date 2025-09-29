from Src.Models.company_model import company_model
from Src.Core.abstract_reference import abstract_reference

######################################
# Модель настроек приложения
class settings_model(abstract_reference):
    __company: company_model = None

    @property 
    def company(self) -> company_model:
        return self.__company

    def __init__(self):
        self.__company = company_model()