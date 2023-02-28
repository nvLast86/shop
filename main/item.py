class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.all.append(self)

    def calculate_total_price(self):
        return self.item_price * self.item_quantity

    def apply_discount(self):
        self.item_price = Item.pay_rate * self.item_price
        return self.item_price


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.item_price)
print(item2.item_price)


print(Item.all)


