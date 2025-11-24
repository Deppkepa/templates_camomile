import os, pathlib

"""
Исключение при проверки аргумента
""" 

class ArgumentException(Exception):
    pass     
    
"""
Исключение при выполнении бизнес операции
"""  
class OperationException(Exception):
    pass   

class ErrorProxy(Exception):
    pass 

class validator:

    # Проверка на пустату значения 
    @staticmethod    
    def check_empty_value(value):
        if str(value).strip() == "":
            raise ArgumentException("Error: Пустое значение!")
        return True

    # Проверка на тип значения    
    @staticmethod   
    def check_type_value(value, type_) -> bool:
        if type_ != type(value):
            raise ArgumentException(f"Error: Тип значения: '{type(value)}' не равен представленому типу: '{type_}'")
        return True
    
    # Проверка на количество знаков строго равно (например inn = 12)
    @staticmethod
    def check_count_value_eq(value, length=None) -> bool:
        if length is not None and length != len(str(value)):
            raise ArgumentException(f"Error: Колличество знаков значения: '{value}' не равна представленному колличеству знаков: '{length}'")
        return True

    #сборка методов
    @staticmethod
    def validate(value, type_, length=None, flag="eq"):
        validator.check_type_value(value, type_)
        validator.check_empty_value(value)
        if flag == "le":
            validator.check_count_value_le(value, length)
        else:
            validator.check_count_value_eq(value, length)

    # Проверка существования файла по указанному пути
    @staticmethod
    def check_search_path(path: pathlib) -> bool:
        if not os.path.exists(path):
            raise ErrorProxy(f"Error: Не найден файл настроек по данному пути '{path}'!")
        return True
    
    # Проверка на количество знаков если оно не строго равно (например:полное наименное <= 255)
    @staticmethod
    def check_count_value_le(value, length=None) -> bool:
        if length is not None and len(str(value)) >= length:
            raise ArgumentException(f"Error: Колличество знаков в значении: '{len(value)}' больше чем представленном колличестве знаков: '{length}'")
        return True
    

