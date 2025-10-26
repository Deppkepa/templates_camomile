from Src.Core.abstract_response import abstract_response
from xml.etree.ElementTree import Element, SubElement, tostring
from Src.Core.common import common

class response_xml(abstract_response):
    def build(self, format: str, data: list) -> str:
        root = Element('Data')
        first_item = data[0]
        headers = common.get_fields(first_item)
        for item in data:
            entry = SubElement(root, 'Entry')
            for header in headers:
                SubElement(entry, header).text = str(getattr(item, header))
        return tostring(root, encoding='unicode')