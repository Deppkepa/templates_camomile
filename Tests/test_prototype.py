
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest, datetime
from Src.Core.prototype import prototype
from Src.Logics.prototype_report import prototype_report
from Src.start_service import start_service
from Src.reposity import reposity
from Src.Core.validator import OperationException
from Src.Dtos.filter_dto import filter_dto
from Src.Core.filter_type import filter_type
from Src.Models.nomenclature_model import nomenclature_model
from Src.Dtos.group_nomenclature_dto import group_nomenclature_dto
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.unit_model import unit_model
from Src.Models.recipe_model import recipe_model

class test_prototype(unittest.TestCase):
    
    # проверка метода фильтрации на номенклатурах
    def test_filter_nomeclature(self):
        products = [
            nomenclature_model.create("спагетти", group_nomenclature_model("Макаронные изделия"), unit_model("грамм", 200)),
            nomenclature_model.create("рожки", group_nomenclature_model("Макаронные изделия"), unit_model("грамм", 200))
        ]
        exact_filter = filter_dto()
        exact_filter.field_name = "name"
        exact_filter.value = "спагетти"
        exact_filter.filter_type = filter_type.EQUALS
        result = prototype_report.apply_filters(products, [exact_filter])
        assert len(result) == 1
        assert result[0].name == "спагетти"


    # проверка метода фильтрации на единицах измерениях
    def test_filter_unit(self):
        units = [
            unit_model("граммы", 1000, base_unit=None),
            unit_model("литры", 1000, base_unit=None)
        ]
        exact_filter = filter_dto()
        exact_filter.field_name = "name"
        exact_filter.value = "граммы"
        exact_filter.filter_type = filter_type.EQUALS
        result = prototype_report.apply_filters(units, [exact_filter])
        assert len(result) == 1
        assert result[0].name == "граммы"


    # проверка метода фильтрации на граппах номенклатур
    def test_filter_group_nomeclature(self):
        products = [
            group_nomenclature_model("Макаронные изделия"),
            group_nomenclature_model("Хлебобулочные изделия")
        ]
        exact_filter = filter_dto()
        exact_filter.field_name = "name"
        exact_filter.value = "изделия"
        exact_filter.filter_type = filter_type.LIKE
        result = prototype_report.apply_filters(products, [exact_filter])
        assert len(result) == 2
        assert result[0].name == "Макаронные изделия"
        assert result[1].name == "Хлебобулочные изделия"

    # проверка метода фильтрации на рецептах
    # def test_filter_recipe(self):
    #     recipes = [
    #         recipe_model.create("Салат Оливье", [], [], 4, 15),
    #         recipe_model.create("Борщ", [], [], 6, 30)
    #     ]
    #     like_filter = filter_dto()
    #     like_filter.field_name = "name"
    #     like_filter.value = "Салат"
    #     like_filter.filter_type = filter_type.LIKE
    #     result = prototype_report.apply_filters(recipes, [like_filter])
    #     self.assertEqual(len(result), 1)
        # self.assertEqual(result[0].name, "Салат Оливье")

    # проверка ENUM-типа фильтра
    def test_filter_type_enum(self):
        assert filter_type.EQUALS.value == "EQUALS"
        assert filter_type.LIKE.value == "LIKE"

    def test_any_prototype_filter(self):
        # Подготовка
        start1 = start_service()
        # start1.is_first_run = True
        start1.start()
       
        start_prototype = prototype_report(start1.repo().data[reposity.range_key()[4]])
        nomenclatures = start1.repo().data[reposity.range_key()[1]]
        if len(nomenclatures) == 0:
            raise OperationException("List is empty!")
        first_nomenclature = nomenclatures[0]

        # Действие

        next_prototype = start_prototype.filter_by_nomenclature( start_prototype, first_nomenclature )
        
        # Проверка
        assert len(next_prototype.data) > 0
        assert len(start_prototype.data) > 0
        assert len(start_prototype.data) >= len(next_prototype.data)

    def test_any_prototype_universal_filter(self):
        # Подготовка
        start = start_service()
        start.start()
        start_prototype = prototype_report(  start.data()[reposity.range_key()[1]] )
        nomenclatures =  start_prototype.data
        if len(nomenclatures) == 0:
            raise OperationException("List is empty!")

        first_nomenclature = nomenclatures[0]
        dto = filter_dto()
        dto.field_name = "name"
        dto.value = first_nomenclature.name

        # Действие
        next_prototype = start_prototype.filter( start_prototype, dto )

        # Проверка
        assert len(next_prototype.data) == 1 


     
  
if __name__ == '__main__':
    unittest.main()  