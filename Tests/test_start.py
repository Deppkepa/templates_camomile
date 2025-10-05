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
        self._start_service = start_service()
        self._start_service.start()

    # def __init__(self, methodName = "runTest"):
    #     super().__init__(methodName)
    #     self.__start_service.start()

    def test_start_service_start_rangeNotEmpty(self):
        #Подготовка

        #Действие
        

        #Проверка
        assert len(self.__start_service.data()) > 0
        assert unit_model.create_kill().base_unit == unit_model.create_gramm().base_unit
        #assert Киллограмм.БазоваяЕдиница.Код = Грамм.Код

    if __name__ == '__main__':
        unittest.main()   