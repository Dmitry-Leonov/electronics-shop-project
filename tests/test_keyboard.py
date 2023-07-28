"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.keyboard import Keyboard


@pytest.fixture
def testing_data():
    item = Keyboard('Dark Project KD87A', 9600, 5, 'EN')
    return item


def test_init(testing_data):
    """ Тест на проверку корректности инициализации экземпляра класса Item """
    assert testing_data.name == "Dark Project KD87A"
    assert testing_data.price == 9600.0
    assert testing_data.quantity == 5
    assert testing_data.language == 'EN'


def test___str__(testing_data):
    assert str(testing_data) == 'Dark Project KD87A'


def test_change_lang(testing_data):
    with pytest.raises(AttributeError):
        testing_data.language = 'CH'
        testing_data.language = 0
