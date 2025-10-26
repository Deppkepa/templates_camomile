from Src.Core.abstract_convertor import abstract_convertor
from Src.Convs.basic_convertor import basic_convertor
from Src.Convs.datetime_convertor import datetime_convertor
from Src.Convs.reference_convertor import reference_convertor
from datetime import datetime


class convert_factory:
    """
    Фабрика для выбора подходящего конвертора
    """

    @staticmethod
    def get_converter(obj) -> abstract_convertor:
        if isinstance(obj, (int, float, str)):
            return basic_convertor()
        elif isinstance(obj, datetime):
            return datetime_convertor()
        elif hasattr(obj, "__dict__"):
            return reference_convertor()
        else:
            raise TypeError(f"Не найден подходящий конвертор для объекта {obj}")