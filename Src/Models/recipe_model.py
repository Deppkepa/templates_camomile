from Src.Core.abstract_reference import abstract_reference
from Src.Core.validator import validator
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.groupNomenclature_model import groupNomenclature_model

class recipe_model(abstract_reference):
    __cooking_method:list = []
    __ingredients:list = []
    __count_portions:int = None
    __cooking_time_minutes:int = None # в минутах
    
    @property
    def cooking_method(self) -> list:
        return self.__cooking_method
    
    @cooking_method.setter
    def cooking_method(self, value:list):
        validator.validate(value, list)
        self.__cooking_method = value


    @property
    def ingredients(self) -> list:
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, value:list):
        validator.validate(value, list)
        self.__cooking_method = value
    

    @property
    def count_portions(self) -> int:
        return self.__count_portions
    
    @count_portions.setter
    def count_portions(self, count:int):
        validator.validate(count, int)
        self.__count_portions = count
    

    @property
    def cooking_time_minutes(self) -> int:
        return self.__cooking_time_minutes
    
    @cooking_time_minutes.setter
    def cooking_time_minutes(self, time:int):
        validator.validate(time, int)
        self.__cooking_time_minutes = time

    def create_recipe_lesson():
        recipe_lesson = recipe_model()
        recipe_lesson.name = "ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ"
        recipe_lesson.count_portions = 10
        recipe_lesson.cooking_time_minutes = 20
        recipe_lesson.ingredients = [nomenclature_model.create("Пшеничная мука", groupNomenclature_model("Сыпучее"), unit_model("грамм", 100)),
                                    nomenclature_model.create("Сахар", groupNomenclature_model("Сыпучее"), unit_model("грамм", 80)),
                                    nomenclature_model.create("Сливочное масло", groupNomenclature_model("Масло"), unit_model("грамм", 70)),
                                    nomenclature_model.create("Куриные яйца", groupNomenclature_model("Яйца"), unit_model("шт", 1)),
                                    nomenclature_model.create("Ванилин", groupNomenclature_model("Специи"), unit_model("грамм", 5))]
        recipe_lesson.cooking_method = ["Как испечь вафли хрустящие в вафельнице? Подготовьте необходимые продукты. Из данного количества у меня получилось 8 штук диаметром около 10 см.",
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
        
    def create_recipe_my():
        recipe_my = recipe_model()
        recipe_my.name = "ПАСТА С ЧЕСНОКОМ И ОЛИВКОВЫМ МАСЛОМ"
        recipe_my.count_portions = 1
        recipe_my.cooking_time_minutes = 20
        recipe_my.ingredients = [nomenclature_model.create_spaghetti(), 
                              nomenclature_model.create_garlic(), 
                              nomenclature_model.create_olive_oil(),
                              nomenclature_model.create_salt(),
                              nomenclature_model.create_pepper()]
        recipe_my.cooking_method = ["Отварите пасту в подсоленной воде согласно инструкции на упаковке до состояния «аль денте».",
                                 "В это время очистите чеснок и порежьте его тонкими пластинками.",
                                 "В сковороде разогрейте оливковое масло и добавьте чеснок. Обжаривайте на среднем огне около 1 минуты до золотистого цвета — не пережарьте, чтобы не горчил.",
                                 "Вылейте готовую пасту в сковороду к чесноку и маслу, перемешайте.",
                                 "Посолите по вкусу, по желанию добавьте немного перца.",
                                 "Переложите на тарелку и подавайте горячим."]
        