from utils.item import Item
import os

def main():
    item1 = Item("Смартфон", 10000, 20)
    Item('Смартфон', 10000, 20)
    print(item1)


"""
def main():
    path = os.sep.join(['files', 'items.csv'])

    #item = Item('Телефон', 10000, 5)
    #item.item_name = 'Смартфон'
    #print(item.item_name)

    #item.item_name = 'СуперСмартфон'

    Item.load_from_csv(path)  # создание объектов из данных файла
    print(len(Item.all))  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    print(item1.item_name)

    print(Item.is_number_integer(5))
    print(Item.is_number_integer(5.0))
    print(Item.is_number_integer(5.5))
"""

if __name__ == "__main__":
    main()
