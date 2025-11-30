from abc import ABC
from Src.Core.validator import OperationException as operation_exception
from Src.Core.event_type import event_type
from Src.start_service import start_service

"""
Абстрактный класс для обработки логики
"""


class abstract_logic(ABC):
    __error_text: str = ""

    def __init__(self, _start_service: start_service):
        self.start_service = _start_service

    """
    Описание ошибки
    """

    @property
    def error_text(self) -> str:
        return self.__error_text.strip()

    @error_text.setter
    def error_text(self, message: str):
        self.__error_text = message.strip()

    """
    Флаг. Есть ошибка
    """

    @property
    def is_error(self) -> bool:
        return self.error_text != ""

    def _inner_set_exception(self, ex: Exception):
        self.__error_text = f"Ошибка! Исключение {ex}"

    """
    Метод для загрузки и обработки исключений
    """

    def set_exception(self, ex: Exception):
        self.__error_text = f"Ошибка! Исключение {ex}"

    """
    Обработка события
    """

    def handle(self, event: str, params: dict):
        events = event_type.events()
        if event not in events:
            raise operation_exception(f"{events} - не является событием!")