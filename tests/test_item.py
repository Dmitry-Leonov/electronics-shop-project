"""Здесь надо написать тесты с использованием pytest для модуля item."""


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
