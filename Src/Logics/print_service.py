from Src.Core.abstract_response import abstract_response
from Src.Core.observe_service import ObserveService
from Src.Core.event_type import event_type

class print_service(abstract_response):
    def __init__(self):
        super().__init__()
        ObserveService.add(self)

    def handle(self, event, params):
        super().handle(event, params)

        if event == event_type.convert_to_json:
            print(params)