import connexion
from flask import request
from Src.Logics.factory_entities import factory_entities
from Src.settings_manager import settings_manager
from Src.start_service import start_service
from Src.Logics.response_json import response_json

app = connexion.FlaskApp(__name__)
service = start_service()
service.start()

"""
Проверить доступность REST API
"""


@app.route("/api/accessibility", methods=['GET'])
def formats():
    return "SUCCESS"


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
    service = start_service()
    service.start()
    data = service.data()
    if datatype == 'nomenclature':
        filtered_data = data['nomenclature_model']
    elif datatype == 'units':
        filtered_data = data['unit_model']
    else:
        return "Неправильно указанный тип данных", 400
    return response_generator.build('csv', filtered_data)


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
