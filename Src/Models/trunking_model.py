import datetime
from Src.Core.abstract_reference import abstract_reference
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.storange_model import storage_model
from Src.Models.unit_model import unit_model

class trunking_model(abstract_reference):
    # Дата, Уникальный номер, Номенклатура, Склад, Количество, Единица измерения
    date: datetime = None
    nomenclature:nomenclature_model = nomenclature_model()
    storage:storage_model = storage_model()
    count:int = 0
    unit:unit_model = unit_model()

    
