from Src.Core.abstract_logic import abstract_logic


class observe_service:
    handlers = []

    """
    Добавить объект под наблюдение
    """
    @staticmethod
    def add(instance):
        if instance is None:
            return

        if not isinstance(instance, abstract_logic):
            return

        if instance not in observe_service.handlers:
            observe_service.handlers.append(instance)

    """
    Убрать объект из под наблюдения
    """
    @staticmethod
    def delete(instance):
        if instance is None:
            return

        if not isinstance(instance, abstract_logic):
            return

        if instance not in observe_service.handlers:
            observe_service.handlers.remove(instance)

    """
    Вызвать события
    """
    @staticmethod
    def create_event(event: str, params):
        for instance in observe_service.handlers:
            instance.handle(event, params)