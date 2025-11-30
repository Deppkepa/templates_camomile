from Src.Core.abstract_logic import abstract_logic
from Src.start_service import start_service


class observe_service:
    handlers = []

    def __init__(self, _start_service: start_service):
        self.start_service = _start_service

    """
    Добавить объект под наблюдение
    """
    @staticmethod
    def add(instance):
        if instance is None:
            return

        if not isinstance(instance, abstract_logic):
            return

        if instance not in ObserveService.handlers:
            ObserveService.handlers.append(instance)

    """
    Убрать объект из под наблюдения
    """
    @staticmethod
    def delete(instance):
        if instance is None:
            return

        if not isinstance(instance, abstract_logic):
            return

        if instance not in ObserveService.handlers:
            ObserveService.handlers.remove(instance)

    """
    Вызвать события
    """
    @staticmethod
    def create_event(event: str, params):
        for instance in ObserveService.handlers:
            instance.handle(event, params)