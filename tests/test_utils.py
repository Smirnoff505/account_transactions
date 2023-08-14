import pytest

from src import utils

transaction_test = {"id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {
                        "amount": "8221.37",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560"
                    },


def test_last_five_transactions():
    pass


def test_hide_number():
    assert utils.hide_number() == 'MasterCard 7158 30** **** 6758 -> Счет **5560'


def test_amount():
    assert utils.amount(transaction_test) == "8221.37 USD"


def date_formation():
    pass
