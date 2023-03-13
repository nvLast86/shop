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
    def item_name(self, name):
        """
        Запись значения приватного атрибута экземпляра item_name
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

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
        with open(path, 'r', newline='') as file:
            csv_data = csv.DictReader(file)
            items_list = []
            for i in csv_data:
                if i['name'] == 'name':
                    continue
                else:
                    items_list.append(cls(i['name'], int(i['price']), int(i['quantity'])))
        return items_list

    @staticmethod
    def is_number_integer(number):
        return ((type(number) == int) or (type(number) == float)) and (round(number) == number)


