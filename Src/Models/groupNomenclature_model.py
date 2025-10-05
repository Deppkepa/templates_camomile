from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator

class groupNomenclature_model(abstract_reference):
    def __init__(self, name:str= None):
        super().__init__()
        validator.validate(name, str)
        self.name = name