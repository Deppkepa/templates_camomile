from Src.Models.settings_model import settings_model
from Src.Core.validator import validator
import json, pathlib


####################################################
# Менеджер настроек. 
# Предназначен для управления настройками и хранения параметров приложения
class settings_manager:
    __file_name:str = "" # Наименование файла (полный путь)
    __settings:settings_model = None # Настройки

    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance 
    
    def __init__(self):
        self.set_default()

    @property
    def file_name(self) -> str:
        return self.__file_name
    
    @property
    def settings(self) -> settings_model:
        return self.__settings

    # Полный путь к файлу настроек
    @file_name.setter
    def file_name(self, value:str):
        validator.check_empty_value(value)
        path = pathlib.Path(value).absolute()
        validator.check_search_path(path)
        self.__file_name = path

    # Загрузить настройки из Json файла
    def load(self) -> bool:
        validator.check_search_path(self.__file_name)
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file_instance:
                data = json.load(file_instance)
                if "company" in data.keys():
                    item = data["company"]
                    self.convert(item)
                if "response_format" in data.keys():
                    self.settings.response_format=data["response_format"].lower()
            return True
        except:
            return False

    # Обработать полученный словарь     
    def convert(self, value: dict) -> bool:
        validator.check_type_value(value, dict)
        fields = list(filter(lambda x: not x.startswith("_") , dir(self.__settings.company))) 
        matching_keys = list(filter(lambda key: key in fields, value.keys()))
        try:
            for key in matching_keys:
                setattr(self.__settings.company, key, value[key])
        except:
            return False        
        return True

    # Настроек по умолчанию
    def set_default(self):
        self.__settings = settings_model()
        self.__settings.company.name = "Noname"
        self.__settings.company.inn = 123456789000
        self.__settings.response_format="csv"
