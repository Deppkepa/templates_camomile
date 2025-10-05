from Src.reposity import reposity
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.groupNomenclature_model import groupNomenclature_model
from Src.Models.recipe_model import recipe_model

class start_service:
    __repo: reposity = reposity()

    def __init__(self):
        self.__repo[ reposity.range_key()[0] ] = []
        self.__repo[ reposity.range_key()[1] ] = []
        self.__repo[ reposity.range_key()[2] ] = []

    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(start_service, cls).__new__(cls)
        return cls.instance 

    def __default_create_ranges(self):
        self.__repo.data[ reposity.range_key()[0] ].append(unit_model.create_gramm())
        self.__repo.data[ reposity.range_key()[0] ].append(unit_model.create_kill())

    def __default_create_nomenclature(self):
        self.__repo.data[ reposity.range_key()[1] ].append(nomenclature_model.create_spaghetti())
        self.__repo.data[ reposity.range_key()[1] ].append(nomenclature_model.create_garlic())
        self.__repo.data[ reposity.range_key()[1] ].append(nomenclature_model.create_salt())
        self.__repo.data[ reposity.range_key()[1] ].append(nomenclature_model.create_olive_oil())
        self.__repo.data[ reposity.range_key()[1] ].append(nomenclature_model.create_pepper())

    def __default_create_nomenclature_group(self):
        self.__repo.data[ reposity.range_key()[2] ].append(groupNomenclature_model("Продукты"))
        self.__repo.data[ reposity.range_key()[2] ].append(groupNomenclature_model("Упаковка"))

    def __default_create_receipts(self):
        self.__repo.recipe.append(recipe_model.create_recipe_lesson())
        self.__repo.recipe.append(recipe_model.create_recipe_my())

    """
    Стартовый набор данных
    """
    def data(self):
        return self.__repo.data

    def recipe(self):
        return self.__repo.recipe   

    """
    Основной метод для генерации эталонных данных
    """
    def start(self):
        self.__default_create_ranges()
        self.__default_create_nomenclature()
        self.__default_create_nomenclature_group()
        self.__default_create_receipts()

    