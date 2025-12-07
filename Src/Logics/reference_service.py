from Src.Core.abstract_reference import abstract_reference
from Src.Core.event_type import event_type
from Src.Core.prototype import prototype
from Src.Core.validator import OperationException


class reference_service:
    def __init__(self, _start_service):
        self.start_service = _start_service

    def find_reference(self, model_type: str, unique_code: str):
        """
        Возвращает модель из репозитория с использованием прототипа
        """
        _prototype = prototype(self.start_service.repo().data.get(model_type, []))
        self.start_service.observe_service.create_event(event_type.INFO_EVENT, {"model_type":model_type, "unique_code":unique_code})
        return _prototype.find(lambda x: x.unique_code == unique_code)

    def add_reference(self, model_type: str, model: abstract_reference):
        """
        Добавляет новую модель в репозиторий
        """
        if self.find_reference(model_type, model.unique_code):
            raise OperationException(f"Entity with unique_code={model.unique_code} already exists.")

        self.start_service.repo().data.setdefault(model_type, {})
        self.start_service.repo().data[model_type][model.unique_code] = model

        self.start_service.observe_service.create_event(event_type.INFO_EVENT, {"model_type":model_type, "model_unique_code":model.unique_code})
        self.start_service.observe_service.create_event(event_type.ADDED_REFERENCE, {"model_type": model_type, "model": model})
        return True

    def edit_reference(self, model_type:str, unique_code: str, new_model: abstract_reference):
        """
        Заменяет старую модель на отредактированную новую
        """

        old_model = self.find_reference(model_type, unique_code)
        if not old_model:
            raise OperationException(f"Entity with unique_code={unique_code} does not exist.")

        self.start_service.observe_service.create_event(event_type.INFO_EVENT, {"model_type":model_type, "unique_code":unique_code, "model_unique_code":new_model.unique_code})
        self.start_service.observe_service.create_event(event_type.EDITED_REFERENCE, {"model_type": model_type, "unique_code":unique_code, "new_model":new_model})
        return True

    def remove_reference(self, model_type: str, unique_code: str):
        """
        Удаляет модель
        """

        model = self.find_reference(model_type, unique_code)
        if not model:
            self.start_service.observe_service.create_event(event_type.ERROR_EVENT,
                                                            {"model_type": model_type, "unique_code": unique_code})
            raise OperationException(f"Entity with unique_code={unique_code} does not exist.")

        self.start_service.observe_service.create_event(event_type.INFO_EVENT, {"model_type":model_type, "unique_code":unique_code})
        self.start_service.observe_service.create_event(event_type.REMOVED_REFERENCE, {"model_type":model_type, "unique_code":unique_code})