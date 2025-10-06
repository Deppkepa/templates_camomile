import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model
from Src.Models.storange_model import storage_model
from Src.Core.validator import ArgumentException
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.recipe_model import recipe_model
import unittest, json, uuid



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
       file_name = "settings.json"
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
        file_name = "./settings_company.json"
        manager1 = settings_manager()
        manager1.file_name = file_name
        manager2 = settings_manager()

        # Дейсвтие
        manager1.load()

        # Проверки
        assert manager1.settings.company == manager2.settings.company
        assert manager1 is manager2

    #Проверка на создание объекта Settings
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
        manager1.file_name = file_name
        manager1.load()

        assert manager1.settings.company.name == "Ромашка"
        assert manager1.settings.company.inn == 123456789000
        assert manager1.settings.company.acc == 12345678900
        assert manager1.settings.company.correspondent_acc == 12345678900
        assert manager1.settings.company.bic == 123456789
        assert manager1.settings.company.ownership == "12345"
    
    # Проверка что путь загружается абсолютным
    def test_file_name_absolute_path(self):
        manager = settings_manager()
        file_name = "settings_company.json"
        manager.file_name = file_name
        assert manager.file_name != file_name
        assert os.path.isabs(manager.file_name) == True

    # проверка на вывод ошибок не корректных данных
    def test_data_in_model_valid(self):
        manager = settings_manager()

        with self.assertRaises(ArgumentException):
            manager.settings.company.name = ""
        
        with self.assertRaises(ArgumentException):
            manager.settings.company.inn = "nhnd"
        
        with self.assertRaises(ArgumentException):
            manager.settings.company.acc = 123
        
        with self.assertRaises(ArgumentException):
            manager.settings.company.correspondent_acc = True
        
        with self.assertRaises(ArgumentException):
            manager.settings.company.bic = list()
        
        with self.assertRaises(ArgumentException):
            manager.settings.company.ownership = "too long ownership"

    # проверка на дефолтные настройки
    def test_default_settings(self):
        file_name = "D:/проекты с гита/templates_camomile/settings.json"
        manager1 = settings_manager()
        manager1.file_name = file_name
        assert manager1.settings.company.name == "Noname"
        assert manager1.settings.company.inn == 123456789000
        assert manager1.settings.company.acc == None
        assert manager1.settings.company.correspondent_acc == None
        assert manager1.settings.company.bic == None
        assert manager1.settings.company.ownership == ""

    #задача: Добавить UUID и сделать сравнение двух моделей
    # переопределить сравнение
    # проверка на сравнение двух по значению одинаковых моделей (по ссылке)
    def test_epnals_storage_model_create(self):
        # подготовка
        id = uuid.uuid4().hex
        storage1 = storage_model()
        storage1.unique_code = id
        storage2 = storage_model()
        storage2.unique_code = id
        # Действие
        
        # Проверка
        assert storage1 == storage2
    
    # Проверка на создания storange model
    def test_create_storage_model(self):
        storage = storage_model()
        storage.unique_code = uuid.uuid4().hex
        storage.name = "Ромашка"
        assert storage.name != ""
        assert storage.unique_code != ""
    

    # проверка на создания unit model
    def test_create_unit_model(self):
        base_range = unit_model("грамм", 1)
        base_range.unique_code = uuid.uuid4().hex

        new_range = unit_model("кг", 1000, base_range)
        new_range.unique_code = uuid.uuid4().hex

        assert new_range.name == "кг"
        assert new_range.base_unit == base_range
        
    

    #Проверка на создание nomenclature model
    def test_create_nomenclature_model(self):
        nomenclature = nomenclature_model()
        nomenclature.name = "Полное имя"
        group = group_nomenclature_model("группа")
        nomenclature.group_nomenclature = group
        assert nomenclature.name != ""
        assert nomenclature.group_nomenclature == group

        with self.assertRaises(ArgumentException):
            nomenclature.name = "В современном мире технологии развиваются очень быстро, " \
                                    "и каждые несколько лет происходят значительные изменения, " \
                                    "влияющие на все сферы жизни человека. Это приводит к появлению " \
                                    "новых возможностей, облегчает выполнение повседневных задач и расширяет" \
                                    " горизонты знаний и творчества.fbhvfyre"
        with self.assertRaises(ArgumentException):
            nomenclature.name = "В современном мире технологии развиваются очень быстро."

    #Проверка на создание group_nomenclature model
    def test_create_groupNomenclature_model(self):
        group = group_nomenclature_model("группа")
        assert group.name != ""

    #Проверка на создание recipe model
    def test_create_recipe_model(self):
        recipe = recipe_model()
        recipe.cooking_time_minutes = 30
        assert recipe.cooking_time_minutes != None 

if __name__ == '__main__':
    unittest.main()   
