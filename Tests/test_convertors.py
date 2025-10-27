import unittest
from datetime import datetime
from Src.Convs.basic_convertor import basic_convertor
from Src.Convs.datetime_convertor import datetime_convertor
from Src.Convs.reference_convertor import reference_convertor
from Src.Convs.convert_factory import convert_factory
from Src.Models.unit_model import unit_model

'''Набор тестов для конверторов'''


class test_convertors(unittest.TestCase):

    # Проверка basic_convertor
    def test_basic_convertor(self):
        # Подготовка
        converter = basic_convertor()
        # Действие
        # Проверки
        self.assertEqual(converter.convert(123), {'value': 123})
        self.assertEqual(converter.convert("hello"), {'value': 'hello'})

    # Проверка датавремя конвертора
    def test_datetime_convertor(self):
        # Подготовка
        dt = datetime.now()
        converter = datetime_convertor()
        # Действие
        # Проверки
        self.assertIn('timestamp', converter.convert(dt))

    # Проверка референс конвертора
    def test_reference_convertor(self):
        # Подготовка
        um = unit_model("граммы", 1)
        converter = reference_convertor()
        # Действие
        converted = converter.convert(um)
        # Проверки
        self.assertIn('name', converted)
        self.assertIn('coeff_recalculation', converted)

    # Проверка convert_factory для basic
    def test_basic_convertor_factory(self):
        # Подготовка
        converter_num = convert_factory.get_converter(123)
        converter_str = convert_factory.get_converter("hello")
        # Действие
        # Проверки
        self.assertEqual(converter_num.convert(123), {'value': 123})
        self.assertEqual(converter_str.convert("hello"), {'value': 'hello'})

    # Проверка convert_factory для datetime
    def test_datetime_convertor_factory(self):
        # Подготовка
        dt = datetime.now()
        # Действие
        converter = convert_factory.get_converter(dt)
        # Проверки
        self.assertIn('timestamp', converter.convert(dt))

    #Проверка convert_factory для reference
    def test_reference_convertor_factory(self):
        #Подготовка
        um = unit_model("граммы", 1)
        #Действие
        converter=convert_factory.get_converter(um)
        result=converter.convert(um)
        #Проверки
        self.assertIn('name',result)
        self.assertIn('coeff_recalculation', result)

    # Проверка конверт фактори
    def test_convert_factory(self):
        # Подготовка
        conv = convert_factory.get_converter(123)
        dt = datetime.now()
        um = unit_model("граммы", 1)
        # Действие
        conv_dt = convert_factory.get_converter(dt)
        conv_ref = convert_factory.get_converter(um)
        # Проверки
        self.assertIsInstance(conv, basic_convertor)
        self.assertIsInstance(conv_dt, datetime_convertor)
        self.assertIsInstance(conv_ref, reference_convertor)


if __name__ == '__main__':
    unittest.main()
