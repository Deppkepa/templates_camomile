from Src.Core.validator import validator


"""
Репозиторий данных
"""
class reposity:
    __data: dict = {}
    __recipe: list = []

    @property
    def data(self):
        return self.__data
    
    """
    Ключ для единц измерений
    """
    @staticmethod
    def range_key() -> list:
        return ["unit_model", "nomenclature_model", "group_nomenclature_model"]
    
    def __setitem__(self, key, value):
        self.__data[key] = value

    @property
    def recipe(self) -> list:
        return self.__recipe
    
    @recipe.setter
    def recipe (self, recipe: list):
        validator.validate(recipe, list)
        self.__recipe = recipe
    
        