import pytest
import json

from src import utils


def test_get_executed_only():
    data = [
        {
            'id': 1,
            'state': 'EXECUTED'
        },
        {
            'id': 2,
            'state': 'CANCELED'
        },
        {
            'id': 3,
            'state': 'CANCELED'
        },
    ]

    expected = [
        {
            'id': 1,
            'state': 'EXECUTED'
        },
    ]
    assert utils.get_executed_only(data) == expected

def test_get_sorted():
    date = [
        {
            "date": "2018-08-19T16:30:41.967497",
        },
        {
            "date": "2019-08-19T16:30:41.967497",
        },
        {
            "date": "2019-08-18T16:30:41.967497",
        },
        {
            "date": "2018-03-19T16:30:41.967497",
        },
        {
            "date": "2017-08-19T16:30:41.967497",
        },
        {
            "date": "2017-05-18T16:30:41.967497",
        },
    ]

    date_sort = [
        {
            "date": "2019-08-19T16:30:41.967497",
        },
        {
            "date": "2019-08-18T16:30:41.967497",
        },
        {
            "date": "2018-08-19T16:30:41.967497",
        },
        {
            "date": "2018-03-19T16:30:41.967497",
        },
        {
            "date": "2017-08-19T16:30:41.967497",
        },
    ]
    assert utils.get_sorted(date) == date_sort

def test_hide_number():
    assert utils.hide_number('Maestro 7810846596785568') == 'Maestro 7810 84** **** 5568'


def test_amount():
    assert utils.amount(
        {
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }
        }, ) == "31957.58 руб."


def test_date_formation():
    assert utils.date_formation(
        {
            "date": "2019-08-26T10:50:58.294041",
        },
    ) == '26.08.2019'
