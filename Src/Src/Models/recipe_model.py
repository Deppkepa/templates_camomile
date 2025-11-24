from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator
from Src.Core.entity_model import entity_model

'''
Модель рецептов
'''

class recipe_model(entity_model):
    __cooking_method:list = []
    __ingredients:list = []
    __count_portions:int = None
    __cooking_time_minutes:int = None # в минутах
    
    @property
    def cooking_method(self) -> list:
        return self.__cooking_method
    
    @cooking_method.setter
    def cooking_method(self, value:list):
        validator.validate(value, list)
        self.__cooking_method = value


    @property
    def ingredients(self) -> list:
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, value:list):
        validator.validate(value, list)
        self.__cooking_method = value
    

    @property
    def count_portions(self) -> int:
        return self.__count_portions
    
    @count_portions.setter
    def count_portions(self, count:int):
        validator.validate(count, int)
        self.__count_portions = count
    

    @property
    def cooking_time_minutes(self) -> int:
        return self.__cooking_time_minutes
    
    @cooking_time_minutes.setter
    def cooking_time_minutes(self, time:int):
        validator.validate(time, int)
        self.__cooking_time_minutes = time
        