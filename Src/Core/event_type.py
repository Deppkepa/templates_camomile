"""
Типы событий
"""


class event_type:
    ADDED_REFERENCE = "ADDED_REFERENCE"
    EDITED_REFERENCE = "EDITED_REFERENCE"
    REMOVED_REFERENCE = "REMOVED_REFERENCE"

    """
    Событие - смена даты блокировки
    """

    @staticmethod
    def change_block_period() -> str:
        return "change_block_period"

    """
    Событие - сформирован Json
    """

    @staticmethod
    def convert_to_json() -> str:
        return "convert_to_json"

    """
    Получить список всех событий
    """

    @staticmethod
    def events() -> list:
        result = [event_type.ADDED_REFERENCE, event_type.REMOVED_REFERENCE, event_type.EDITED_REFERENCE]
        methods = [method for method in dir(event_type) if
                   callable(getattr(event_type, method)) and not method.startswith('__') and method != "events"]
        for method in methods:
            key = getattr(event_type, method)()
            result.append(key)
        return result