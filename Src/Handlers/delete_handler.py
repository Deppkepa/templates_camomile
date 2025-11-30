from Src.Core.abstract_logic import abstract_logic
from Src.Core.event_type import event_type
from Src.Core.validator import OperationException
from Src.reposity import reposity


class delete_handler(abstract_logic):
    def handle(self, event: str, params: dict):
        super().handle(event, params)
        if event == event_type.REMOVED_REFERENCE:
            model_type = params.get("model_type")
            unique_code = params.get("unique_code")

            if model_type == "nomenclature_model":
                recipes_using_nomenclature = [
                    r for r in self.start_service.repo().recipe.ingredients.values()
                    if r.unique_code == unique_code
                ]
                transactions_using_nomenclature = [
                    t for t in self.start_service.repo().transactions.values()
                    if t.nomenclature.unique_code == unique_code
                ]
                if recipes_using_nomenclature or transactions_using_nomenclature:
                    raise OperationException(
                        f"Невозможно удалить номенклатуру {unique_code}, "
                    )
            elif model_type == "unit_model":
                unit_using_unit = [
                    u for u in self.start_service.repo().data[reposity.range_key()[0]].values()
                    if u.base_unit.unique_code == unique_code
                ]
                nomenclature_using_unit = [
                    n for n in self.start_service.repo().data[reposity.range_key()[1]].values()
                    if n.unique_code == unique_code
                ]
                transaction_using_unit = [
                    t for t in self.start_service.repo().transactions.values()
                    if t.unit.unique_code == unique_code
                ]
                if unit_using_unit or nomenclature_using_unit or transaction_using_unit:
                    raise OperationException(
                        f"Невозможно удалить единицу измерения {unique_code}, "
                    )
            elif model_type == "group_nomenclature_model":
                nomenclature_using_group = [
                    n for n in self.start_service.repo().data[reposity.range_key()[1]].values()
                    if n.group_nomenclature.unique_code == unique_code
                ]
                if nomenclature_using_group:
                    raise OperationException(
                        f"Невозможно удалить группу номенклатуры {unique_code}, "
                    )
            elif model_type == "storage_model":
                transaction_using_storage = [
                    n for n in self.start_service.repo().transactions.values()
                    if n.storage.unique_code == unique_code
                ]
                if transaction_using_storage:
                    raise OperationException(
                        f"Невозможно удалить склад {unique_code}, "
                    )

            del self.start_service.repo().data[model_type][unique_code]