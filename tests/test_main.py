import pytest
from utils.item import Item


def test_load_from_csv():
    Item.load_from_csv('file.csv')
    assert len(Item.all) == 5

def test_repr_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == repr(Item("Смартфон", 10000, 20))
    assert str(item1) == "Смартфон"

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

def test_is_number_integer():
    item = Item("name", 50, 2)
    assert item.is_number_integer(5) is True
    assert item.is_number_integer(5.0) is True
    assert item.is_number_integer(5.5) is False
    assert item.is_number_integer("5") is False


def test_load_from_csv():
    Item.load_from_csv('file.csv')
    assert len(Item.all) == 5





