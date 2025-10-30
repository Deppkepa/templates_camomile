from datetime import datetime
from Src.Core.abstract_convertor import abstract_convertor
from Src.Core.validator import validator

class datetime_convertor(abstract_convertor):
    """
    Конвертирует объекты типа datetime
    """

    def convert(self, obj) -> dict:
        validator.validate(obj,datetime)

        return {'timestamp': obj.isoformat()}