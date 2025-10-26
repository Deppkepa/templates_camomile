from Src.Core.abstract_convertor import abstract_convertor


class basic_convertor(abstract_convertor):
    """
    Конвертирует базовые типы (числа, строки)
    """

    def convert(self, obj) -> dict:
        if isinstance(obj, (int, float, str)):
            return {'value': obj}
        else:
            raise TypeError(f"Объект {obj} не является базовым типом")