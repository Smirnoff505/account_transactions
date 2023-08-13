import json

OPERATION_DATA = 'operation.json'


def load_operation():
    """
    Функция открытия json файла
    :return: словарь
    """
    with open(OPERATION_DATA, 'r', encoding='utf-8') as file:
        data_operation = json.load(file)
    return data_operation

