from Src.Core.validator import validator, OperationException
from abc import ABC, abstractmethod


# Абстрактный класс для формирования ответов
class abstract_response(ABC):
    def __init__(self):
        super().__init__()
    # Сформировать нужный ответ
    @abstractmethod
    def build(self, format: str, data: list) -> str:
        validator.validate(format, str)
        validator.validate(data, list)

        if len(data) == 0:
            raise OperationException("Нет данных!")

        return f""