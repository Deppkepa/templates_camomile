from Src.Logics.response_csv import response_csv
from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator, OperationException

class factory_entities:
    __match = {
        "csv": response_csv
    }


    def create(self, format: str) -> abstract_reference:
        if format not in self.__match.keys():
            raise OperationException("Формат не верный")
        
        return self.__match[format]