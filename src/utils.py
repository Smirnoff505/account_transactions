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


def last_five_transactions(transactions):
    """
    Принимает список словарей, проверяет наличие всех ключей, после чего добавляет в список
    :param transactions:
    :return: список словарей последних пять операций
    """
    result = []

    for dict_ in transactions:
        if 'date' in dict_ and 'state' in dict_ and dict_['state'] == 'EXECUTED':
            result.append(dict_)
        else:
            continue
    lst_five = sorted(result, key=lambda x: x['date'], reverse=True)

    return lst_five[:5]


def hide_number_from(dict_):
    """
    Принимает словарь, скрывает часть счета исходящего *
    :param dict_:
    :return: замаскированный номер счета/карты
    """
    if 'from' in dict_:
        lst_1 = str(dict_['from']).split(' ')
        for num_1 in lst_1:
            if num_1.isdigit() and len(num_1) == 16 and len(lst_1) == 3:
                return lst_1.pop(0) + ' ' + lst_1.pop(0) + ' ' + num_1[0:4] + ' ' + num_1[4:6] + '**' + ' ' + '****' \
                    + ' ' + num_1[-4:]
            elif num_1.isdigit() and len(num_1) == 16 and len(lst_1) == 2:
                return lst_1.pop(0) + ' ' + num_1[0:4] + ' ' + num_1[4:6] + '**' + ' ' + '****' + ' ' + num_1[-4:]
            elif num_1.isdigit() and len(num_1) == 20 and len(lst_1) == 2:
                return lst_1.pop(0) + ' ' + num_1[0:4] + ' ' + num_1[4:6] + '**' + ' ' + '****' + ' ' + '****' + ' ' \
                    + num_1[-4:]
    return ''


def hide_number_to(dict_):
    """
    Принимает словарь, скрывает часть счета входящего *
    :param dict_:
    :return: замаскированный номер счета/карты
    """
    lst_2 = str(dict_['to']).split(' ')
    for num_2 in lst_2:
        if num_2.isdigit():
            return '->' + ' ' + lst_2.pop(0) + ' ' + '**' + num_2[-4:]


def amount(dict_):
    """
    Принимает словарь
    :param dict_:
    :return: f-строку с суммой и валютой
    """
    return f"{dict_['operationAmount']['amount']} {dict_['operationAmount']['currency']['name']}"


def date_formation(dict_):
    """
    Принимает словарь, достает и преобразует дату
    :param dict_:
    :return: f - строку с датой транзакции
    """
    for date in dict_:
        item = dict_['date'][:10]
        new = tuple(item.split('-'))
        year, month, day = new
        return f"{day}.{month}.{year}"
