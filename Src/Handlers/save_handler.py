import json

from Src.Core.abstract_logic import abstract_logic
from Src.Core.event_type import event_type


class save_handler(abstract_logic):
    def handle(self, event: str, params: dict):
        super().handle(event, params)
        unique_code = ""
        if event == event_type.ADDED_REFERENCE:
            unique_code = params.get("model").unique_code
        else:
            unique_code = params.get("unique_code")
        config_file = "appsettings.json"
        with open(config_file, "r+") as f:
            config = json.load(f)
            config[event] = unique_code
            f.seek(0)
            json.dump(config, f, indent=4)
            f.truncate()