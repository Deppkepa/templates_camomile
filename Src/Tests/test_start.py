

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Src.Models.unit_model import unit_model
from Src.start_service import start_service
from Src.reposity import reposity
import unittest
from main import app


class test_start(unittest.TestCase):
    __start_service: start_service = start_service()

    def setUp(self):
        self.__start_service = start_service()
        self.__start_service.first_run_setup()
        self.__start_service.start()


    # проверка на наличие данные в эталонных данных
    def test_start_service_start_dataRecipeNotEmpty(self):
        # Подготовка
        try:
            os.remove("run_status.json")
        except OSError:
            pass

        # Действие

        # Проверка
        assert len(self.__start_service.data()) > 0
        assert unit_model.create_kill().base_unit == unit_model.create_gramm().base_unit
        # assert Киллограмм.БазоваяЕдиница.Код = Грамм.Код
        assert len(self.__start_service.data()["unit_model"]) >= 2
        assert len(self.__start_service.data()["nomenclature_model"]) >= 5
        assert len(self.__start_service.data()["group_nomenclature_model"]) >= 2
        assert len(self.__start_service.recipe()) >= 2

    # проверка на уникальность каждого элемента unit_model
    def test_unique_check_unit_model(self):
        # Подготовка
        data = self.__start_service.data()["unit_model"]
        unique_set = set()
        # Действие
        for i in data:
            unique_set.add(i.unique_code)
        # Проверка

        assert len(unique_set) == len(data)

    # проверка на уникальность каждого элемента nomenclature_model
    def test_unique_check_nomenclature_model(self):
        # Подготовка
        data = self.__start_service.data()["nomenclature_model"]
        unique_set = set()
        # Действие
        for i in data:
            unique_set.add(i.unique_code)
        # Проверка

        assert len(unique_set) == len(data)

    # проверка на уникальность каждого элемента group_nomenclature_model
    def test_unique_check_group_nomenclature_model(self):
        # Подготовка
        data = self.__start_service.data()["group_nomenclature_model"]
        unique_set = set()
        # Действие
        for i in data:
            unique_set.add(i.unique_code)
        # Проверка

        assert len(unique_set) == len(data)

    # проверка на уникальность каждого рецепта
    def test_unique_check_recipe(self):
        # Подготовка
        recipe = self.__start_service.recipe()
        unique_set = set()
        # Действие
        for i in recipe:
            unique_set.add(i.unique_code)
        # Проверка
        assert len(unique_set) == len(recipe)

    if __name__ == '__main__':
        unittest.main()