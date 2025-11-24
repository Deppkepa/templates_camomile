from Src.Core.abstract_response import abstract_response
from Src.Core.common import common

class response_markdown(abstract_response):
    def build(self, format: str, data: list) -> str:
        markdown_text = "# Список данных\n"
        first_item = data[0]
        headers = common.get_fields(first_item)
        markdown_text += "| " + " | ".join(headers) + " |\n"
        markdown_text += "| " + ("---|" * len(headers)) + "\n"
        for item in data:
            row_values = [getattr(item, header) for header in headers]
            markdown_text += "| " + " | ".join(map(str, row_values)) + " |\n"
        return markdown_text