from Src.reposity import reposity
from Src.Models.unit_model import unit_model

class start_service:
    __repo: reposity = reposity()

    def __init__(self):
        self.__repo[ reposity.range_key() ] = []

    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(start_service, cls).__new__(cls)
        return cls.instance 

    def __default_create_ranges(self):
        self.__repo.data[ reposity.range_key() ] = unit_model.create_gramm()
        self.__repo.data[ reposity.range_key() ] = unit_model.create_kill()
        
    """
    Стартовый набор данных
    """
    def data(self):
        return self.__repo.data   

    """
    Основной метод для генерации эталонных данных
    """
    def start(self):
        self.__default_create_ranges()

    