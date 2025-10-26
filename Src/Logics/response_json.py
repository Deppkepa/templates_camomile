from Src.Core.abstract_response import abstract_response
from Src.Core.common import common
import json

class response_json(abstract_response):
    def build(self, format: str, data: list) -> str:
        output = []
        first_item = data[0]
        headers = common.get_fields(first_item)
        for item in data:
            obj = {header: getattr(item, header) for header in headers}
            output.append(obj)
        return json.dumps(output, ensure_ascii=False, indent=4)