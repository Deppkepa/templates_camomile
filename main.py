import json
from collections import defaultdict
from datetime import datetime

import connexion
from flask import request, jsonify
from Src.Logics.factory_entities import factory_entities
from Src.Models.inventory_snapshot_model import inventory_snapshot_model
from Src.settings_manager import settings_manager
from Src.start_service import start_service
from Src.Logics.response_json import response_json
from Src.Convs.convert_factory import convert_factory
from Src.Core.common import common

app = connexion.FlaskApp(__name__)
service = start_service()
service.start()
factory = factory_entities()
conv_factory = convert_factory()

"""
Проверить доступность REST API
"""


@app.route("/api/accessibility", methods=['GET'])
def formats():
    return "SUCCESS"


@app.route('/api/osv', methods=['GET'])
def get_osv():
    """
    Возвращает оборотно-сальдовую ведомость за период.

    Args:
        begin_date (str): Дата начала периода (YYYY-MM-DD)
        end_date (str): Дата окончания периода (YYYY-MM-DD)
        storage_id (str): Идентификатор склада

    Responses:
        - 200 OK: Таблица оборотно-сальдовой ведомости
        - 400 Bad Request: Неправильные параметры запроса
    """
    begin_date = request.args.get('begin_date')
    end_date = request.args.get('end_date')
    storage_id = request.args.get('storage_id')

    if not all([begin_date, end_date, storage_id]):
        return "Ошибка: отсутствуют обязательные параметры", 400

    repo = service.data()
    report = generate_osv_report(repo, begin_date, end_date, storage_id)
    return jsonify(conv_factory.get_converter(report).convert(report))


def calculate_initial_balance(transactions, date, storage_id):
    """
    Рассчитывает начальный баланс на дату.
    """
    balance = {}
    for txn in transactions:
        if txn.storage.unique_code == storage_id and txn.date < date:
            key = f"{txn.nomenclature.unique_code}-{txn.unit.unique_code}"
            balance[key] = balance.get(key, 0) + txn.quantity
    return balance


def aggregate_movements(transactions, begin, end, storage_id):
    """
    Аграгирует движения за период.
    """
    movements = {}
    for txn in transactions:
        if (
                txn.storage.unique_code == storage_id
                and begin <= txn.date <= end
        ):
            key = f"{txn.nomenclature.unique_code}-{txn.unit.unique_code}"
            movement = movements.get(key, {
                'nomenclature': txn.nomenclature,
                'unit': txn.unit,
                'income': [],
                'expense': []
            })
            if txn.quantity > 0:
                movement['income'].append(txn)
            else:
                movement['expense'].append(txn)
            movements[key] = movement
    return movements

def calculate_inventories_until_block(repo, block_period, storage_id):
    """
    Рассчитывает остатки до даты блокировки.
    """
    # Сначала попробуем найти готовый инвентарный снимок
    existing_snapshot = next(
        (snap.inventory for snap in repo.inventory_snapshots if snap.snapshot_date == block_period),
        None
    )

    if existing_snapshot is None:
        # Если готового снимка нет, делаем расчет вручную
        beginning = datetime.strptime("1900-01-01", "%Y-%m-%d")
        # Возьмем все транзакции до даты блокировки
        relevant_txns = [
            txn for txn in repo.transactions
            if txn.storage.unique_code == storage_id and beginning <= txn.date <= block_period
        ]

        # Сделаем агрегирование
        inventories = defaultdict(float)
        for txn in relevant_txns:
            key = f"{txn.nomenclature.unique_code}-{txn.unit.unique_code}"
            inventories[key] += txn.quantity

        # Создаем новый инвентарный снимок и сохраняем его
        new_snapshot = inventory_snapshot_model()
        new_snapshot.snapshot_date = block_period
        new_snapshot.inventory = dict(inventories)
        repo.inventory_snapshots.append(new_snapshot)
        return new_snapshot.inventory
    else:
        return existing_snapshot

def generate_osv_report_with_block(repo, begin_date, end_date, storage_id, block_period=settings_manager().settings.block_period):
    """
    Генерирует отчет ОСВ с учетом блокировки.
    """


    # Проверяем, есть ли у нас готовность на момент блокировки
    pre_block_inventories = calculate_inventories_until_block(repo, block_period, storage_id)

    # Теперь делаем расчеты движений после блокировки
    post_block_txns = [
        txn for txn in repo.transactions
        if txn.storage.unique_code == storage_id and block_period < txn.date <= end_date
    ]

    # Строим сводку движений после блокировки
    post_block_inventories = defaultdict(float)
    for txn in post_block_txns:
        key = f"{txn.nomenclature.unique_code}-{txn.unit.unique_code}"
        post_block_inventories[key] += txn.quantity

    # Соединяем обе части вместе
    combined_inventories = pre_block_inventories.copy()
    for key, value in post_block_inventories.items():
        if key in combined_inventories:
            combined_inventories[key] += value
        else:
            combined_inventories[key] = value

    return combined_inventories

def generate_osv_report(repo, begin_date, end_date, storage_id):
    """
    Генерирует отчет оборотно-сальдовой ведомости за указанный период.

    Args:
        repo (Reposity): Репозиторий данных
        begin_date (str): Начало периода
        end_date (str): Окончание периода
        storage_id (str): Идентификатор склада

    Returns:
        list of dict: Таблица с результатами ОСВ
    """
    # Парсим даты
    begin = datetime.strptime(begin_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    # Находим склад
    storage = next((s for s in repo["storage_model"] if s.unique_code == storage_id), None)
    if not storage:
        return [], 404

    # Найдем начальные остатки на складе на начало периода
    initial_balance = calculate_initial_balance(repo["transaction_model"], begin, storage_id)

    # Рассчитываем обороты за период
    movements = aggregate_movements(repo["transaction_model"], begin, end, storage_id)

    # Формируем финальный отчет
    report = []
    for key in movements:
        nomenclature = movements[key]['nomenclature']
        unit = movements[key]['unit']
        total_income = sum(t.quantity for t in movements[key]['income'])
        total_expense = sum(t.quantity for t in movements[key]['expense'])
        final_balance = initial_balance.get(key, 0) + total_income - total_expense

        report.append({
            'initial_balance': initial_balance.get(key, 0),
            'nomenclature': nomenclature,
            'unit': unit,
            'total_income': total_income,
            'total_expense': total_expense,
            'final_balance': final_balance
        })

    return report


def serialize_repo(repo):
    """
    Сериализирует репозиторий в словарь для последующего сохранения в файл.
    Используя имеющиеся конвертеры для корректной сериализации объектов.
    """
    data = {
        'units': [convert_factory.get_converter(u).convert(u) for u in repo().data["unit_model"]],
        'nomenclatures': [convert_factory.get_converter(n).convert(n) for n in repo().data["nomenclature_model"]],
        'groups': [convert_factory.get_converter(g).convert(g) for g in repo().data["group_nomenclature_model"]],
        'recipes': [convert_factory.get_converter(r).convert(r) for r in repo().recipe],
        'storages': [convert_factory.get_converter(s).convert(s) for s in repo().data["storage_model"]],
        'transactions': [convert_factory.get_converter(t).convert(t) for t in repo().data["transaction_model"]]
    }
    return data


@app.route('/api/save', methods=['GET'])
def save_repository_to_file():
    """
    Сохраняет все данные из репозитория в файл.

    Responses:
        - 200 OK: Операция выполнена успешно
        - 500 Internal Server Error: Произошла ошибка при сохранении
    """
    repo = service.repo
    filename = f'data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            data = serialize_repo(repo)
            json.dump(data, file, ensure_ascii=False, indent=4)
        return "Данные сохранены успешно", 200
    except Exception as e:
        print(e)
        return "Ошибка при сохранении данных", 500

@app.route('/api/settings/block_period', methods=['POST'])
def update_block_period():
    block_period_str = request.form.get('block_period')
    if not block_period_str:
        return "Ошибка: отсутствует обязательный параметр", 400

    try:
        block_period = datetime.strptime(block_period_str, "%Y-%m-%d")
    except ValueError:
        return "Ошибка: неверный формат даты", 400

    settings = settings_manager().settings
    settings.block_period = block_period
    return "Дата блокировки успешно обновлена", 200

@app.route('/api/settings/block_period', methods=['GET'])
def get_block_period():
    settings = settings_manager().settings
    return jsonify({"block_period": settings.block_period.strftime('%Y-%m-%d')})

@app.route('/api/inventory/<date_str>', methods=['GET'])
def get_inventory(date_str):
    try:
        requested_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return "Ошибка: неверный формат даты", 400

    block_period = settings_manager().settings.block_period
    if requested_date <= block_period:
        # Используем данные до блокировки
        result = calculate_inventories_until_block(service.repo(), block_period, "STORAGE_ID")
    else:
        # Используем полные данные
        result = generate_osv_report_with_block(service.repo(), "1900-01-01", requested_date, "STORAGE_ID")

    return jsonify(result)

@app.route('/api/data/<datatype>', methods=['GET'])
def get_data(datatype):
    """
    Возвращает данные заданного типа в указанном формате.

    Args:
        datatype (str): Тип данных ('nomenclature', 'units', etc.)

    Responses:
        - 200 OK: Данные успешно возвращены
        - 400 Bad Request: Неправильный запрос
    """
    factory = factory_entities()
    response_generator = factory.create_default()
    data = service.data()
    if datatype == 'nomenclature':
        filtered_data = data['nomenclature_model']
    elif datatype == 'units':
        filtered_data = data['unit_model']
    elif datatype == "storage":
        filtered_data = data["storage_model"]
    elif datatype == "transaction":
        filtered_data = data["transaction_model"]
    elif datatype == "group_nomenclature":
        filtered_data = data["group_nomenclature_model"]
    else:
        return "Неправильно указанный тип данных", 400
    return jsonify(convert_factory.get_converter(filtered_data).convert(filtered_data))


@app.route('/api/receipts', methods=['GET'])
def get_receipts():
    """
    Возвращает список всех рецептов
    """

    recipes = service.recipe()
    return response_json().build('json', recipes)


@app.route('/api/receipt/<code>', methods=['GET'])
def get_receipt(code):
    """
    Возвращает рецепт по указанному коду
    """
    recipes = service.recipe()
    receipt = next((r for r in recipes if r.unique_code == code), None)
    if receipt:
        return response_json().build('json', [receipt])
    else:
        return "Рецепт не найден", 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
