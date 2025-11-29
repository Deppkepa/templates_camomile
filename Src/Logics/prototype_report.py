from Src.Core.prototype import prototype
from Src.Models.nomenclature_model import nomenclature_model
from Src.Core.validator import validator
from Src.Dtos.filter_dto import filter_dto
from Src.Core.filter_type import filter_type

# Реализация прототипа для отчетности
class prototype_report(prototype):


    # Сделать фильтр по номенклатуре
    # Врзврат - прототип
    @staticmethod
    def filter_by_nomenclature(source:prototype, nomenclature:nomenclature_model  ) -> prototype:
        # validator.validate(source, prototype)
        # validator.validate(nomenclature, nomenclature_model)

        result = []
        for item in source.data:
            if item.nomenclature == nomenclature:
                result.append(item)

        return source.clone(result)    

    # Универасльный фильтр
    @staticmethod
    def filter(source:prototype,  filter:filter_dto  ) -> prototype:
        # validator.validate(source, prototype)
        result = prototype.filter( source.data, filter )
        return source.clone(result)

    
    @staticmethod
    def get_nested_attribute(obj, field_name):
        # Разбираем строку на составляющие
        keys = field_name.split('.')
        current_obj = obj
        for key in keys:
            if hasattr(current_obj, key):
                current_obj = getattr(current_obj, key)
            else:
                return None
        return current_obj

    @staticmethod
    def apply_filters(data_list, filters):
        result = []
        for item in data_list:
            matched_all_filters = True
            for flt in filters:
                field_value = prototype_report.get_nested_attribute(item, flt.field_name)
                if field_value is not None:
                    if flt.filter_type == filter_type.EQUALS:
                        if field_value != flt.value:
                            matched_all_filters = False
                            break
                    elif flt.filter_type == filter_type.LIKE:
                        if flt.value not in field_value:
                            matched_all_filters = False
                            break
                else:
                    matched_all_filters = False
                    break
            if matched_all_filters:
                result.append(item)
        return result