"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200_000
    assert isinstance(item.calculate_total_price(), float)
    item.price = 0
    assert item.calculate_total_price() == 0


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000


def test_name(item):
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'

def test_string_to_number(item):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5