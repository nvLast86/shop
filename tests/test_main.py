import pytest
from main.item import Item

@pytest.fixture()
def some_item():
    return Item('test_position', 100, 10)

def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 1000

def test_apply_discount(some_item):
    Item.pay_rate = 0.5
    assert some_item.apply_discount() == 50





