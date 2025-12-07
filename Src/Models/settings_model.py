from datetime import datetime
from typing import Optional, Dict

from Src.Core.validator import validator
from Src.Models.company_model import company_model
from Src.Core.abstract_reference import abstract_reference


######################################
# Модель настроек приложения
class settings_model(abstract_reference):
    __company: company_model = None
    __response_format: str = ""
    __block_period: Optional[datetime] = datetime.now()
    __inventory_cache: Dict[str, Dict[str, float]] = {}  # Кэш остатков

    @property
    def inventory_cache(self) -> Dict[str, Dict[str, float]]:
        return self.__inventory_cache

    @inventory_cache.setter
    def inventory_cache(self, value):
        self.__inventory_cache = value

    @property
    def block_period(self) -> Optional[datetime]:
        return self.__block_period

    @block_period.setter
    def block_period(self, value: datetime):
        validator.validate(value, datetime)
        self.__block_period = value

    @property
    def company(self) -> company_model:
        return self.__company

    @property
    def response_format(self) -> str:
        return self.__response_format

    @response_format.setter
    def response_format(self, value: str):
        allowed_formats = ['csv', 'markdown', 'json', 'xml']
        if value.lower() not in allowed_formats:
            raise ValueError(f"Invalid response format: {value}. Allowed values are {allowed_formats}")
        self.__response_format = value.lower()

    def __init__(self):
        self.__company = company_model()
        self.__response_format = ''
