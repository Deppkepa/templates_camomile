from enum import Enum

class filter_type(Enum):
    EQUALS = "EQUALS" # полное совпадение
    LIKE = "LIKE" # вхождение строки