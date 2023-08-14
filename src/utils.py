import json

OPERATION_DATA = 'operation.json'


def load_operation():
    """
    Функция открытия json файла
    :return: список словарей
    """
    with open(OPERATION_DATA, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def hide_number():
    pass


def amount():
    pass