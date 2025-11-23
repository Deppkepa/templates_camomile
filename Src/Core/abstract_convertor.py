from abc import ABC, abstractmethod


class abstract_convertor(ABC):
    """
    Абстрактный класс-конвертор для сериализации объектов в JSON
    """

    @abstractmethod
    def convert(self, obj):
        """
        Конвертировать объект в словарь
        """
        pass