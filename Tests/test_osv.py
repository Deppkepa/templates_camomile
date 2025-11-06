import json
import sys
import os
import unittest
from main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class test_osv(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_osv_report(self):
        # Подготовка
        try:
            os.remove("run_status.json")
        except OSError:
            pass
        start_date = '2023-01-01'
        end_date = '2027-12-31'
        storage_id = 'strg1'

        # Действие
        response = self.client.get(
            f"/api/osv?begin_date={start_date}&end_date={end_date}&storage_id={storage_id}")
        result = json.loads(response.text)
        # Проверки
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(result)
