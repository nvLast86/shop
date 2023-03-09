class Item:
    """
    Класс для представления товара в магазине.
    Аттрибуты класса:
    - pay_rate - уровень цен с учетом скидки
    - all - список хранения созданных экземпляров класса
    """
    pay_rate = 1.0
    all = []

    def __init__(self, item_name, item_price, item_quantity):
        """
        :param item_name: название товара
        :param item_price: цена товара за единицу
        :param item_quantity: количество товара
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.all.append(self)

    def calculate_total_price(self):
        """
        Метод подсчета общей стоимости товара
        :return: Общая стоимость товара
        """
        return self.item_price * self.item_quantity

    def apply_discount(self):
        """
        Метод подсчета стоимости единицы товара с учетом скидки
        :return: Стоимость единицы товара с учетом скидки
        """
        self.item_price = Item.pay_rate * self.item_price
        return self.item_price





