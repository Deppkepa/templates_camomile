from Src.Core.abstract_response import abstract_response
from Src.Convs.convert_factory import convert_factory
from Src.Core.common import common
import json

class response_json(abstract_response):
    def build(self, format: str, data: list) -> str:
        output = []
        for item in data:
            converter = convert_factory.get_converter(item)
            serialized = converter.convert(item)
            output.append(serialized)
        return json.dumps(output, ensure_ascii=False, indent=4)