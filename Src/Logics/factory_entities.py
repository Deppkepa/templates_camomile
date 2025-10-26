from Src.Logics.response_csv import response_csv
from Src.Logics.response_markdown import response_markdown
from Src.Logics.response_json import response_json
from Src.Logics.response_xml import response_xml
from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator, OperationException
from Src.settings_manager import settings_manager
from Src.Core.abstract_response import abstract_response
class factory_entities:
    __match = {
        "csv": response_csv(),
        "markdown":response_markdown(),
        "json":response_json(),
        "xml":response_xml()
    }


    def create(self, format: str) -> abstract_reference:
        if format not in self.__match.keys():
            raise OperationException("Формат не верный")
        
        return self.__match[format]

    def create_default(self) -> abstract_response:
        settings = settings_manager().settings
        return self.create(settings.response_format)