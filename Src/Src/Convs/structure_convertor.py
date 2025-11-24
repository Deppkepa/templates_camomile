from Src.Core.abstract_convertor import abstract_convertor

"""Конвертер структур

Обрабатывает объекты, являющиеся списками, кортежами и словарями"""

class structure_convertor(abstract_convertor):
    def __init__(self, conv_factory=None):
        self.__conv_factory = conv_factory

    def convert(self, obj: [list, tuple, dict]):
        # Проверяем тип объекта
        if isinstance(obj, (list, tuple)):
            return [self.__conv_factory.get_converter(x).convert(x) for x in obj]
        elif isinstance(obj, dict):
            return {k: self.__conv_factory.get_converter(v).convert(v) for k, v in obj.items()}
        else:
            raise TypeError("Объект не является последовательностью.")