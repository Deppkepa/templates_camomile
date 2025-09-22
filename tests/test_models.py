from src.settings_manager import settings_manager
from src.Models.company_model import company_model
import unittest


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
       file_name = "D:/проекты с гита/templates_camomile/settings.json"
       manager = settings_manager()
       manager.file_name = file_name
       
       # Дейсвтие
       result = manager.load()
            
       # Проверки
       assert result == True


    # Проверить создание основной модели
    # Данные загружаем. Проверяем работу Singletone
    def test_loadCombo_createmodel_companymodel(self):
        # Подготовка
        file_name = "./settings.json"
        manager1 = settings_manager()
        manager1.file_name = file_name
        manager2 = settings_manager()


        # Дейсвтие
        manager1.load()

        # Проверки
        assert manager1.company == manager2.company

    # #Проверка на создание объекта Settings
    def test_convert_in_settings(self):
        file_name = "./settings.json"
        manager = settings_manager()
        manager.file_name = file_name

        result = manager.convert()

        assert result == True
    
    # проверка на загрузку настроек в settings
    def test_conver_init_setings(self):
        file_name = "./settings_company.json"
        manager = settings_manager()
        manager.file_name = file_name
        manager.convert()
        settings = manager.settings

        assert settings.company_name == "Ромашка"
        assert settings.inn == "123456789000"
        assert settings.acc == "12345678900"
        assert settings.correspondent_acc == "12345678900"
        assert settings.bic == "123456789"
        assert settings.ownership == "12345"
        
  
if __name__ == '__main__':
    unittest.main()   
