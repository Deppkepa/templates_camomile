from Src.Core.abstract_convertor import abstract_convertor
from Src.Convs.basic_convertor import basic_convertor
from Src.Convs.datetime_convertor import datetime_convertor
from Src.Convs.reference_convertor import reference_convertor
from datetime import datetime


class convert_factory:
    """
    Фабрика для выбора подходящего конвертора
    """

    _handlers = {
        (int, float, str): basic_convertor(),
        datetime: datetime_convertor(),
        object: reference_convertor()
    }

    @staticmethod
    def get_converter(obj) -> abstract_convertor:
        for types, handler in convert_factory()._handlers.items():
            if isinstance(obj, types):
                return handler

        raise TypeError(f"Не найден подходящий конвертор для объекта {obj}")