from Src.Core.entity_model import entity_model
from Src.Core.validator import validator
from datetime import datetime
from Src.Models.storange_model import storage_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model

"""
Модель транзакции
"""


class transaction_model(entity_model):
    __date: datetime = None
    __nomenclature: nomenclature_model = None
    __storage: storage_model = None
    __quantity: float = None
    __unit: unit_model = None

    @property
    def date(self) -> datetime:
        return self.__date

    @date.setter
    def date(self, value: datetime):
        validator.validate(value, datetime)
        self.__date = value

    @property
    def nomenclature(self) -> nomenclature_model:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        validator.validate(value, nomenclature_model)
        self.__nomenclature = value

    @property
    def storage(self) -> storage_model:
        return self.__storage

    @storage.setter
    def storage(self, value: storage_model):
        self.__storage = value

    @property
    def quantity(self) -> float:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: float):
        validator.validate(value, float)
        self.__quantity = value

    @property
    def unit(self) -> unit_model:
        return self.__unit

    @unit.setter
    def unit(self, value: unit_model):
        validator.validate(value, unit_model)
        self.__unit = value