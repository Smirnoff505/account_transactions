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


def get_executed_only(list_operations):
    """Делает выборку словарей только с полем EXECUTED"""
    result = []
    for item in list_operations:
        if item.get('state') == 'EXECUTED':
            result.append(item)
        else:
            continue
    return result


def get_sorted(list_operations, count=5):
    """Получает список словарей и возвращает отсортированные по убыванию операции.
    По умолчанию 5 последних операций"""
    last = sorted(list_operations, key=lambda x: x['date'], reverse=True)
    return last[:count]


def hide_number(bill_info):
    if bill_info is None:
        return ''
    bill_parts = bill_info.split()
    number = bill_parts[-1]
    if bill_info.lower().startswith('счет'):
        hided_number = f'**{number[-4:]}'
    else:
        hided_number = f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
    return hided_number


def amount(dict_):
    """
    Принимает словарь
    :param dict_:
    :return: f-строку с суммой и валютой
    """
    return f"{dict_['operationAmount']['amount']} {dict_['operationAmount']['currency']['name']}"


def date_formation(operation):
    """
    Принимает словарь, достает и преобразует дату
    :return: f - строку с датой транзакции
    """
    item = operation['date'][:10]
    year, month, day = item.split('-')

    return f"{day}.{month}.{year}"
