from typing import List

from Src.Core.validator import validator
from Src.Models.inventory_snapshot_model import inventory_snapshot_model

"""
Репозиторий данных
"""
class reposity:
    __data: dict = {}
    __recipe: list = []
    __transactions: list = []
    __storages: list = []

    __inventory_snapshots: List[inventory_snapshot_model] = []

    @property
    def inventory_snapshots(self) -> List[inventory_snapshot_model]:
        return self.__inventory_snapshots

    @inventory_snapshots.setter
    def inventory_snapshots(self, value: List[inventory_snapshot_model]):
        validator.validate(value, List[inventory_snapshot_model])
        self.__inventory_snapshots = value
    @property
    def transactions(self) -> list:
        return self.__transactions

    @transactions.setter
    def transactions(self, transactions: list):
        validator.validate(transactions, list)
        self.__transactions = transactions

    @property
    def storages(self) -> list:
        return self.__storages

    @storages.setter
    def storages(self, storages: list):
        validator.validate(storages, list)
        self.__storages = storages

    @property
    def data(self):
        return self.__data
    
    """
    Ключ для единц измерений
    """
    @staticmethod
    def range_key() -> list:
        return ["unit_model", "nomenclature_model", "group_nomenclature_model","storage_model","transaction_model"]
    
    def __setitem__(self, key, value):
        self.__data[key] = value

    @property
    def recipe(self) -> list:
        return self.__recipe
    
    @recipe.setter
    def recipe(self, recipe: list):
        validator.validate(recipe, list)
        self.__recipe = recipe
    
        