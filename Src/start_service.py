import json
import os
from datetime import datetime

from Src.Models.storange_model import storage_model
from Src.Models.transaction_model import transaction_model
from Src.reposity import reposity
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.recipe_model import recipe_model

STATUS_FILE_PATH = 'run_status.json'


class start_service:
    __repo: reposity = reposity()
    __is_first_run: bool = True

    def __init__(self):
        self.__repo[reposity.range_key()[0]] = []
        self.__repo[reposity.range_key()[1]] = []
        self.__repo[reposity.range_key()[2]] = []
        self.__repo[reposity.range_key()[3]] = []
        self.__repo[reposity.range_key()[4]] = []

    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(start_service, cls).__new__(cls)
        return cls.instance

    def __default_create_storages(self):
        stg1 = storage_model().create("Центральный склад")
        stg1.unique_code = "stg1"
        self.__repo.data[reposity.range_key()[3]].append(stg1)

    def __default_create_transactions(self):
        storage = self.__repo.data[reposity.range_key()[3]][0]
        nomenclature = self.__repo.data[reposity.range_key()[1]][0]
        unit = self.__repo.data[reposity.range_key()[0]][0]

        tx1 = transaction_model()
        tx1.date = datetime.now()
        tx1.unique_code = "TXN-001"
        tx1.nomenclature = nomenclature
        tx1.storage = storage
        tx1.quantity = 100.0
        tx1.unit = unit

        self.__repo.data[reposity.range_key()[4]].append(tx1)

    def __default_create_ranges(self):
        self.__repo.data[reposity.range_key()[0]].append(unit_model.create_gramm())
        self.__repo.data[reposity.range_key()[0]].append(unit_model.create_kill())

    """
    Стартовый набор номенклатур
    """

    def __default_create_nomenclature(self):
        unit = unit_model("грамм", 200)
        group = group_nomenclature_model("Макаронные изделия")
        self.__repo.data[reposity.range_key()[1]].append(nomenclature_model().create("спагетти", group, unit))

        unit = unit_model("грамм", 12)
        group = group_nomenclature_model("Овощи")
        self.__repo.data[reposity.range_key()[1]].append(nomenclature_model().create("Чеснок", group, unit))

        unit = unit_model("мл", 45)
        group = group_nomenclature_model("Масло")
        self.__repo.data[reposity.range_key()[1]].append(nomenclature_model.create("Оливковое масло", group, unit))

        unit = unit_model("грамм", 15)
        group = group_nomenclature_model("Специи")
        self.__repo.data[reposity.range_key()[1]].append(nomenclature_model.create("Соль", group, unit))

        unit = unit_model("грамм", 15)
        group = group_nomenclature_model("Специи")
        self.__repo.data[reposity.range_key()[1]].append(nomenclature_model.create("Перец", group, unit))

    """
    Стартовый набор групп номенклатур
    """

    def __default_create_nomenclature_group(self):
        self.__repo.data[reposity.range_key()[2]].append(group_nomenclature_model("Продукты"))
        self.__repo.data[reposity.range_key()[2]].append(group_nomenclature_model("Упаковка"))

    """
    Стартовый набор рецептов
    """

    def __default_create_receipts(self):
        # 1 вариант: с урока
        recipe_lesson = recipe_model()
        recipe_lesson.name = "ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ"
        recipe_lesson.count_portions = 10
        recipe_lesson.cooking_time_minutes = 20
        recipe_lesson.ingredients = [
            nomenclature_model.create("Пшеничная мука", group_nomenclature_model("Сыпучее"), unit_model("грамм", 100)),
            nomenclature_model.create("Сахар", group_nomenclature_model("Сыпучее"), unit_model("грамм", 80)),
            nomenclature_model.create("Сливочное масло", group_nomenclature_model("Масло"), unit_model("грамм", 70)),
            nomenclature_model.create("Куриные яйца", group_nomenclature_model("Яйца"), unit_model("шт", 1)),
            nomenclature_model.create("Ванилин", group_nomenclature_model("Специи"), unit_model("грамм", 5))]
        recipe_lesson.cooking_method = [
            "Как испечь вафли хрустящие в вафельнице? Подготовьте необходимые продукты. Из данного количества у меня получилось 8 штук диаметром около 10 см.",
            "Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.",
            "Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.",
            "Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может свариться. Перемешайте яйцо с маслом до однородности.",
            "Всыпьте муку, добавьте ванилин.",
            "Перемешайте массу венчиком до состояния гладкого однородного теста.",
            "Разогрейте вафельницу по инструкции к ней. У меня очень старая, "
            "еще советских времен электровафельница. Она может и не очень красивая, "
            "но печет замечательно!Я не смазываю вафельницу маслом, в тесте достаточно "
            "жира, да и к ней уже давно ничего не прилипает. Но вы смотрите по своей модели."
            " Выкладывайте тесто по столовой ложке.Можно класть немного меньше теста, тогда вафли будут меньше и их получится больше.",
            "Пеките вафли несколько минут до золотистого цвета. Осторожно откройте вафельницу, она очень горячая! Снимите вафлю лопаткой. Горячая она очень мягкая, как блинчик.",
        ]
        self.__repo.recipe.append(recipe_lesson)

        # 2 варинат: мой
        recipe_my = recipe_model()
        recipe_my.name = "ПАСТА С ЧЕСНОКОМ И ОЛИВКОВЫМ МАСЛОМ"
        recipe_my.count_portions = 1
        recipe_my.cooking_time_minutes = 20
        recipe_my.ingredients = [nomenclature_model.create("спагетти", group_nomenclature_model("Макаронные изделия"),
                                                           unit_model("грамм", 200)),
                                 nomenclature_model.create("Чеснок", group_nomenclature_model("Овощи"),
                                                           unit_model("грамм", 12)),
                                 nomenclature_model.create("Оливковое масло", group_nomenclature_model("Масло"),
                                                           unit_model("мл", 45)),
                                 nomenclature_model.create("Соль", group_nomenclature_model("Специи"),
                                                           unit_model("грамм", 15)),
                                 nomenclature_model.create("Перец", group_nomenclature_model("Специи"),
                                                           unit_model("грамм", 15))]
        recipe_my.cooking_method = [
            "Отварите пасту в подсоленной воде согласно инструкции на упаковке до состояния «аль денте».",
            "В это время очистите чеснок и порежьте его тонкими пластинками.",
            "В сковороде разогрейте оливковое масло и добавьте чеснок. Обжаривайте на среднем огне около 1 минуты до золотистого цвета — не пережарьте, чтобы не горчил.",
            "Вылейте готовую пасту в сковороду к чесноку и маслу, перемешайте.",
            "Посолите по вкусу, по желанию добавьте немного перца.",
            "Переложите на тарелку и подавайте горячим."]
        self.__repo.recipe.append(recipe_my)

    """
    Стартовый набор данных
    """

    def repo(self):
        return self.__repo

    def data(self):
        return self.__repo.data

    def recipe(self):
        return self.__repo.recipe

    def load_run_status(self):
        if os.path.exists(STATUS_FILE_PATH):
            with open(STATUS_FILE_PATH, 'r') as file:
                status = json.load(file)
                self.__is_first_run = status.get('is_first_run', True)
        else:
            self.__is_first_run = True

    def save_run_status(self):
        with open(STATUS_FILE_PATH, 'w') as file:
            json.dump({'is_first_run': self.__is_first_run}, file)

    """
    Основной метод для генерации эталонных данных
    """

    def start(self):
        if self.__is_first_run:
            self.__default_create_ranges()
            self.__default_create_nomenclature()
            self.__default_create_nomenclature_group()
            self.__default_create_receipts()
            self.__default_create_storages()
            self.__default_create_transactions()
            self.__is_first_run = False
            self.save_run_status()
