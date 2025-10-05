from Src.Core.validator import validator
"""
Репозиторий данных
"""
class reposity:
    __data: dict = {}

    @property
    def data(self):
        return self.__data
    
    """
    Ключ для единц измерений
    """
    @staticmethod
    def range_key() -> str:
        return "unit_model"
    
    def __setitem__(self, key, value):
        self.__data[key] = value
        