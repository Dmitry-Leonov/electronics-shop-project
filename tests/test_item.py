"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def testing_data():
    item = Item("Samsung", 100.0, 10)
    return item


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


def test_string_to_number(testing_data):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test___repr__(testing_data):
    assert repr(testing_data) == "Item('Samsung', 100.0, 10)"


def test___str__(testing_data):
    assert str(testing_data) == 'Samsung'
