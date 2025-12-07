from Src.Core.abstract_logic import abstract_logic
from Src.Core.event_type import event_type
from Src.reposity import reposity


class edit_handler(abstract_logic):
    def handle(self, event: str, params: dict):
        super().handle(event, params)
        if event == event_type.EDITED_REFERENCE:
            model_type = params.get("model_type")
            unique_code = params.get("model_type")
            new_model = params.get("new_model")

            self.start_service.repo().data[model_type][unique_code] = new_model
            if model_type == "nomenclature_model":
                recipes_using_nomenclature = [
                    r for r in self.start_service.repo().recipe.ingredients.values()
                    if r.unique_code == unique_code
                ]
                transactions_using_nomenclature = [
                    t for t in self.start_service.repo().transactions.values()
                    if t.nomenclature.unique_code == unique_code
                ]

                for r in recipes_using_nomenclature:
                    for i in range(len(r.ingredients)):
                        if r.ingredients[i].unique_code == unique_code:
                            r.ingredients[i] = new_model
                for t in transactions_using_nomenclature:
                    t.nomenclature = new_model

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

                for u in unit_using_unit:
                    u.base_unit = new_model
                for n in nomenclature_using_unit:
                    n.unit = new_model
                for t in transaction_using_unit:
                    t.unit = new_model

            elif model_type == "group_nomenclature_model":
                nomenclature_using_group = [
                    n for n in self.start_service.repo().data[reposity.range_key()[1]].values()
                    if n.group_nomenclature.unique_code == unique_code
                ]

                for n in nomenclature_using_group:
                    n.group_nomenclature = new_model

            elif model_type == "storage_model":
                transaction_using_storage = [
                    n for n in self.start_service.repo().transactions.values()
                    if n.storage.unique_code == unique_code
                ]

                for t in transaction_using_storage:
                    t.storage = new_model
