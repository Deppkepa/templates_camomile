import random
import string
import timeit
from datetime import timedelta, datetime
from Src.Models.transaction_model import transaction_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.storange_model import storage_model
from Src.Models.unit_model import unit_model
from Src.reposity import reposity
from main import generate_osv_report_with_block


def generate_random_transactions(num_transactions):
    repo = reposity()
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 10, 1)

    for i in range(num_transactions):
        tx = transaction_model()
        tx.date = start_date + timedelta(days=random.randint(0, 270))
        tx.nomenclature = nomenclature_model()
        tx.nomenclature.unique_code = f"Nom_{i}"
        tx.storage = storage_model()
        tx.storage.unique_code = "STORAGE_ID"
        tx.quantity = random.uniform(-100, 100)
        tx.unit = unit_model.create_kill()
        tx.unit.unique_code = f"Unit_{i}"
        repo.transactions.append(tx)
    return repo


def measure_performance(num_transactions, block_period):
    repo = generate_random_transactions(num_transactions)
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 10, 1)

    execution_time = timeit.timeit(
        lambda: generate_osv_report_with_block(repo, start_date, end_date, "STORAGE_ID", block_period),
        number=1,
    )
    return execution_time


def benchmark_osv_calculation():
    num_transactions = 100000
    results = []

    # Различные варианты даты блокировки
    block_dates = [
        datetime(2024, 1, 1),  # Блокировка сразу
        datetime(2024, 3, 1),  # Через три месяца
        datetime(2024, 6, 1),  # Через полгода
        datetime(2024, 10, 1),  # В конце периода
    ]

    for block_date in block_dates:
        exec_time = measure_performance(num_transactions, block_date)
        results.append((block_date, exec_time))

    # Выводим результаты в Markdown
    md_results = f"# Результаты нагрузочных тестов для {num_transactions} транзакций\n\n| Дата блокировки | Время выполнения (секунды) |\n|-----------------|----------------------------|\n"
    for block_date, exec_time in results:
        md_results += f"| {block_date:%Y-%m-%d} | {exec_time:.2f} |\n"

    print(md_results)


benchmark_osv_calculation()