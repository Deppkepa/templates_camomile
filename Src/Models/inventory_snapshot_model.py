from datetime import datetime
from typing import Dict

from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator

class inventory_snapshot_model(abstract_reference):
    """
    Класс для хранения остатков на дату блокировки
    """
    __snapshot_date: datetime = None
    __inventory: Dict[str, float] = {}

    @property
    def snapshot_date(self) -> datetime:
        return self.__snapshot_date

    @snapshot_date.setter
    def snapshot_date(self, value: datetime):
        validator.validate(value, datetime)
        self.__snapshot_date = value

    @property
    def inventory(self) -> Dict[str, float]:
        return self.__inventory

    @inventory.setter
    def inventory(self, value: Dict[str, float]):
        self.__inventory = value