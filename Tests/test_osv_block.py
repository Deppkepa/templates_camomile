import unittest
from datetime import datetime

from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.storange_model import storage_model
from Src.Models.transaction_model import transaction_model
from Src.Models.unit_model import unit_model
from Src.reposity import reposity
from Src.start_service import start_service
from main import calculate_inventories_until_block, generate_osv_report_with_block

"""
Набор тестов для проверки osv_block_period
"""


class test_osv_block_Logic(unittest.TestCase):
    def test_calculate_inventories_until_block(self):
        # Проверим расчет остатков до блокировки
        # Подготовка
        repo = reposity()

        tr1 = transaction_model()
        tr1.date = datetime(2024, 1, 1)
        tr1.nomenclature = nomenclature_model()
        tr1.nomenclature.unique_code = "PROD-B"
        tr1.unit = unit_model.create_kill()
        tr1.unit.unique_code = "KG"
        tr1.quantity = 100.0
        tr1.storage = storage_model()
        tr1.storage.unique_code = "STORE_A"

        tr2 = transaction_model()
        tr2.date = datetime(2024, 1, 15)
        tr2.nomenclature = nomenclature_model()
        tr2.nomenclature.unique_code = "PROD-B"
        tr2.unit = unit_model.create_kill()
        tr2.unit.unique_code = "KG"
        tr2.quantity = -50.0
        tr2.storage = storage_model()
        tr2.storage.unique_code = "STORE_A"

        tr3 = transaction_model()
        tr3.date = datetime(2024, 2, 1)
        tr3.nomenclature = nomenclature_model()
        tr3.nomenclature.unique_code = "PROD-B"
        tr3.unit = unit_model.create_kill()
        tr3.unit.unique_code = "KG"
        tr3.quantity = 30.0
        tr3.storage = storage_model()
        tr3.storage.unique_code = "STORE_A"

        repo.transactions.extend([tr1, tr2, tr3])

        block_period = datetime(2024, 1, 15)
        # Действие
        result = calculate_inventories_until_block(repo, block_period, "STORE_A")
        # Проверки
        self.assertIn(("PROD-B-KG", 50), result.items())

    def test_generate_osv_report_with_block(self):
        # Проверим генерацию ОСВ-отчета с учетом блокировки
        # Подготовка

        repo = reposity()

        tr1 = transaction_model()
        tr1.date = datetime(2024, 1, 1)
        tr1.nomenclature = nomenclature_model()
        tr1.nomenclature.unique_code = "PROD-A"
        tr1.unit = unit_model.create_kill()
        tr1.unit.unique_code = "KG"
        tr1.quantity = 100.0
        tr1.storage = storage_model()
        tr1.storage.unique_code = "STORE_A"

        tr2 = transaction_model()
        tr2.date = datetime(2024, 1, 15)
        tr2.nomenclature = nomenclature_model()
        tr2.nomenclature.unique_code = "PROD-A"
        tr2.unit = unit_model.create_kill()
        tr2.unit.unique_code = "KG"
        tr2.quantity = -50.0
        tr2.storage = storage_model()
        tr2.storage.unique_code = "STORE_A"

        tr3 = transaction_model()
        tr3.date = datetime(2024, 2, 1)
        tr3.nomenclature = nomenclature_model()
        tr3.nomenclature.unique_code = "PROD-A"
        tr3.unit = unit_model.create_kill()
        tr3.unit.unique_code = "KG"
        tr3.quantity = 30.0
        tr3.storage = storage_model()
        tr3.storage.unique_code = "STORE_A"

        repo.transactions.extend([tr1, tr2, tr3])

        block_period = datetime(2024, 3, 2)
        end_date = datetime(2024, 2, 2)

        print("HELLO IM HERE!!!", len(repo.transactions))
        # Действие
        result = generate_osv_report_with_block(repo, "1900-01-01", end_date, "STORE_A", block_period=block_period)
        # Проверки
        self.assertIn(("PROD-A-KG", 80), result.items())


if __name__ == '__main__':
    unittest.main()
