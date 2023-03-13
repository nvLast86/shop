import pytest
from utils.item import Item

@pytest.fixture()
def some_item():
    return Item('test_position', 100, 10)

def test_calculate_total_price(some_item):
    """
    Создаем тестовый экземпляр класса с ценой за единицу в 100 и количестве 10.
    Метод экземпляра calculate_total_price() должен вернуть 1000
    """
    assert some_item.calculate_total_price() == 1000

def test_apply_discount(some_item):
    """
    Создаем тестовый экземпляр класса с ценой за единицу в 100 и количестве 10.
    Метод экземпляра apply_discount() должен вернуть новую цену за единицу в 50
    """
    Item.pay_rate = 0.5
    assert some_item.apply_discount() == 50

def test_is_number_integer() -> bool:
    item = Item("name", 50, 2)
    assert item.is_number_integer(5) is True
    assert item.is_number_integer(5.0) is True
    assert item.is_number_integer(5.5) is False
    assert item.is_number_integer("5") is False

def test_item_name():
    item = Item("asus_asus_asus", 5, 2)
    assert item.item_name == 'wrong name'
