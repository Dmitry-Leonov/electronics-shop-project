import pytest

from src.phone import Phone


@pytest.fixture
def testing_data():
    item = Phone("Samsung", 100.0, 10, 2)
    return item


def test_init(testing_data):
    """ Тест на проверку корректности инициализации экземпляра класса Item """
    assert testing_data.name == "Samsung"
    assert testing_data.price == 100.0
    assert testing_data.quantity == 10
    assert testing_data.number_of_sim == 2


def test___repr__(testing_data):
    assert repr(testing_data) == "Phone('Samsung', 100.0, 10, 2)"


def test___str__(testing_data):
    assert str(testing_data) == 'Samsung'


def test_number_of_sim(testing_data):
    with pytest.raises(ValueError):
        testing_data.number_of_sim = -1
        testing_data.number_of_sim = 0
        testing_data.number_of_sim = 1.2
