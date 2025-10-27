from Src.Core.abstract_convertor import abstract_convertor
from Src.Core.common import common


class reference_convertor(abstract_convertor):
    """
    Конвертирует объекты модели
    """

    def convert(self, obj) -> dict:
        if hasattr(obj, "__dict__"):
            result = {}
            attributes = common.get_fields(obj)
            for attr in attributes:
                value = getattr(obj, attr)
                if callable(value):
                    continue
                if hasattr(value, "__dict__"):
                    result[attr] = self.convert(value)
                else:
                    result[attr] = value
            return result
        else:
            raise TypeError(f"Объект {obj} не имеет атрибутов для сериализации")