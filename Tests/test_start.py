import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Src.Models.unit_model import unit_model
from Src.start_service import start_service
from Src.reposity import reposity
import unittest



class test_start(unittest.TestCase):

    __start_service: start_service = start_service()

    def setUp(self):
        self.__start_service = start_service()
        self.__start_service.start()

    # проверка на наличие данные в эталонных данных
    def test_start_service_start_dataRecipeNotEmpty(self):
        #Подготовка

        #Действие
    
        #Проверка
        assert len(self.__start_service.data()) > 0
        assert unit_model.create_kill().base_unit == unit_model.create_gramm().base_unit
        #assert Киллограмм.БазоваяЕдиница.Код = Грамм.Код
        assert len(self.__start_service.data()["unit_model"]) == 2
        assert len(self.__start_service.data()["nomenclature_model"]) == 5
        assert len(self.__start_service.data()["groupNomenclature_model"]) == 2
        assert len(self.__start_service.recipe()) == 2

    if __name__ == '__main__':
        unittest.main()   