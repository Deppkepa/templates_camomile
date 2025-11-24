import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Src.Logics.response_csv import response_csv
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Logics.factory_entities import factory_entities
from Src.Core.response_format import response_formats
from Src.Core.validator import validator
from Src.Core.abstract_response import abstract_response

class TestStorageModel(unittest.TestCase):

    # Проверим формирование CSV
    def test_not_none_response_csv_build(self):
        # Подготовка
        response = response_csv()
        data = []
        entity = group_nomenclature_model.create("test")
        data.append(entity)
        
        # Действие
        result = response.build("csv", data)
        
        # Проверка
        assert result is not None



if __name__ == '__main__':
    unittest.main()  