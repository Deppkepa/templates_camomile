import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.settings_manager import settings_manager
from src.Models.company_model import company_model
import unittest
import json


class test_models(unittest.TestCase):

    # Проверка создание основной модели
    # Данные после создания должны быть пустыми
    def test_empty_createmodel_companymodel(self):
        # Подготовка
        model = company_model()

        # Действие

        # Проверки
        assert model.name == ""


    # Проверить создание основной модели
    # Данные меняем. Данные должны быть
    def test_notEmpty_createmodel_companymodel(self):
        # Подготовка
        model = company_model()
        
        # Действие
        model.name = "test"

        # Проверки
        assert model.name != ""


    # Проверить создание основной модели
    # Данные загружаем через json настройки
    def test_load_createmodel_companymodel(self):
        # Подготовка
       file_name = "settings_company.json"
       manager = settings_manager()
       
       # Дейсвтие
       result = manager.load(file_name)
            
       # Проверки
       assert result == True


    # Проверить создание основной модели
    # Данные загружаем. Проверяем работу Singletone
    def test_loadCombo_createmodel_companymodel(self):
        # Подготовка
        file_name = "./settings_company.json"
        manager1 = settings_manager()
        manager1.file_name = file_name
        manager2 = settings_manager()

        # Дейсвтие
        manager1.load(file_name)

        # Проверки
        assert manager1.settings.company == manager2.settings.company

    # #Проверка на создание объекта Settings
    def test_convert_in_settings(self):
        file_name = "./settings_company.json"
        manager = settings_manager()
        with open( file_name, 'r', encoding='utf-8') as file_instance:
            data = json.load(file_instance)
            result = manager.convert(data["company"])
        assert result == True
    
    # проверка на загрузку настроек в settings
    def test_conver_init_setings(self):
        file_name = "D:/проекты с гита/templates_camomile/settings_company.json"
        manager1 = settings_manager()
        manager1.load(file_name)

        assert manager1.settings.company.name == "Ромашка"
        assert manager1.settings.company.inn == "123456789000"
        assert manager1.settings.company.acc == "12345678900"
        assert manager1.settings.company.correspondent_acc == "12345678900"
        assert manager1.settings.company.bic == "123456789"
        assert manager1.settings.company.ownership == "12345"

  
if __name__ == '__main__':
    unittest.main()   
