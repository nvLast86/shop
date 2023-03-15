import csv


class Item:
    """
    Класс для представления товара в магазине.
    Аттрибуты класса:
    - pay_rate - уровень цен с учетом скидки
    - all - список хранения созданных экземпляров класса
    """
    pay_rate = 1.0
    all = []

    def __init__(self, item_name='', item_price=0.0, item_quantity=0):
        """
        :param __item_name: название товара
        :param item_price: цена товара за единицу
        :param item_quantity: количество товара
        """
        self.__item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.all.append(self)

    @property
    def item_name(self):
        """
        Возвращает значение приватного атрибута экземпляра item_name
        """
        return self.__item_name

    @item_name.setter
    def item_name(self, item_name):
        """
        Запись значения приватного атрибута экземпляра item_name
        """
        if len(item_name) <= 10:
            self.__name = item_name
        else:
            raise Exception('wrong name')

    def __repr__(self):
        return f"Товар: {self.__item_name}. Цена: {self.item_price}. Количество: {self.item_quantity}"

    def __str__(self):
        return f'{self._item_name}'

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

    @classmethod
    def load_from_csv(cls, path):
        """
        Создаёт новые экземпляры из csv файла
        """
        with open(path, 'r', encoding='windows-1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))

    @staticmethod
    def is_number_integer(number):
        return ((type(number) == int) or (type(number) == float)) and (round(number) == number)


