from Src.Core.validator import validator, OperationException
from abc import ABC, abstractmethod
from Src.Core.event_type import event_type


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
    

    """
    Обработка события
    """
    def handle(self, event: str, params):
        validator.check_type_value(event, str)
        events = event_type.events()

        if event not in events:
            raise OperationException(f"{events} - не является событием!")