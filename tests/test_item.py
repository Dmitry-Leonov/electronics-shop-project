"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os

import pytest

from src.item import Item, InstantiateCSVError


def test_init(testing_data):
    """ Тест на проверку корректности инициализации экземпляра класса Item """
    assert testing_data.name == "Samsung"
    assert testing_data.price == 100.0
    assert testing_data.quantity == 10


def test_all_items(testing_data):
    """ Тест на проверку добавления экземпляра класса Item в список all """
    assert testing_data in Item.all


def test_calculate_total_price(testing_data):
    """ Тест на проверку корректности выводимого значения
    при вызове calculate_total_price  """
    assert testing_data.calculate_total_price() == 1000
    assert isinstance(testing_data.calculate_total_price(), float)
    testing_data.price = 0
    assert testing_data.calculate_total_price() == 0


def test_apply_discount(testing_data):
    testing_data.apply_discount()
    assert testing_data.price == 100
    testing_data.pay_rate = 0.8
    testing_data.apply_discount()
    assert testing_data.price == 80


def test_name(testing_data):
    testing_data.name = 'СуперСмартфон'
    assert testing_data.name == 'СуперСмарт'
    testing_data.name = 'Samsung'
    assert testing_data.name == 'Samsung'


def test_instantiate_from_csv():
    """ Тест на соответствие содержания файла данным из списка"""
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    item2 = Item.all[3]
    assert item1.name == 'Смартфон'
    assert item2.price == 50
    assert item1.quantity == 1
    assert len(Item.all) == 5


def test_instantiate_from_csv_file_not_found():
    Item.data_path = 'path'
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_brak():
    Item.data_path = os.path.join(os.path.dirname(__file__), "items_test.csv")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()



@pytest.mark.parametrize('test_input, expected', [
    ('10', 10),
    ('5.5', 5),
    ('105.8', 105),
    ('abc', None),
    ('apple', None)
])
def test_string_to_number(test_input, expected):
    """ Тест на проверку корректности перевода строки в целое число """
    if expected is not None:
        assert Item.string_to_number(test_input) == expected
    else:
        with pytest.raises(ValueError):
            Item.string_to_number(test_input)


def test___repr__(testing_data):
    assert repr(testing_data) == "Item('Samsung', 100.0, 10)"


def test___str__(testing_data):
    assert str(testing_data) == 'Samsung'
