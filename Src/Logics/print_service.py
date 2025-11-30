from Src.Core.abstract_logic import abstract_logic
from Src.Core.observe_service import ObserveService
from Src.Core.event_type import event_type
from Src.start_service import start_service


class print_service(abstract_logic):
    def __init__(self, _start_service: start_service):
        super().__init__(_start_service)
        ObserveService.add(self)

    def handle(self, event, params):
        super().handle(event, params)

        if event == event_type.convert_to_json:
            print(params)