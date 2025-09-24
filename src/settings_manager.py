# from src.Models.company_model import company_model
from src.Models.settings import Settings
import os
import json
import pathlib

####################################################
# Менеджер настроек. 
# Предназначен для управления настройками и хранения параметров приложения
class settings_manager:
    __file_name:str = ""
    __settings:Settings = None

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
    def settings(self) -> Settings:
        return self.__settings

    # Полный путь к файлу настроек
    @file_name.setter
    def file_name(self, value:str):
        if value.strip() == "":
            return
        path = pathlib.Path(value).absolute()
        if os.path.exists(path):
            self.__file_name = path
        else:
            raise Exception("Не найден файл настроек!")
    
    # Загрузить настройки из Json файла
    def load(self) -> bool:
        if not self.file_name.exists():
            raise Exception("Не найден файл настроек!")
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file_instance:
                data = json.load(file_instance)
                if "company" in data.keys():
                    item = data["company"]
                    return self.convert(item)
            return False
        except:
            return False
        
    def convert(self, value: dict) -> bool:
        self.settings.company.name = value["name"]
        self.settings.company.inn = value["inn"]
        self.settings.company.acc = value["acc"]
        self.settings.company.correspondent_acc = value["correspondent_acc"]
        self.settings.company.bic = value["bic"]
        self.settings.company.ownership = value["ownership"]
        return True
        
    # Параметры настроек по умолчанию
    def set_default(self):
        self.__settings = Settings()
        self.__settings.company.name = "Noname"
        self.__settings.company.inn = 123456789000
        self.__settings.company.acc = 12345678900
        self.__settings.company.correspondent_acc = 12345678900
        self.__settings.company.bic = 123456789
        self.__settings.company.ownership = "12A45"