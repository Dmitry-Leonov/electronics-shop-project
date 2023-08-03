import pytest

from src.item import Item


@pytest.fixture
def testing_data():
    return Item("Samsung", 100.0, 10)