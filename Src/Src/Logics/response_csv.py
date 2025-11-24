from Src.Core.abstract_response import abstract_response
from Src.Core.common import common

class response_csv(abstract_response):

    def __init__(self):
        super().__init__()

    # Сформировать CSV 
    def build(self, format: str, data: list):
        text = super().build(format, data)

        # Шапка
        item = data[0]

        fields = common.get_fields(item)

        for field in fields:
            text += f"{field};"

        # Данные
        return text