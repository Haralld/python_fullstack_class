""" Управление складом"""


def update_stock(item, quantity, stock):
    """ обновляет количество товара в складе """

    if item in stock:
        stock[item]['quantity'] += quantity
    else:
        stock[item] = {'quantity': quantity}


def get_item_quantity(item_name, stock):
    """ возвращает количество конкретного товара в складе"""

    return stock[item_name]['quantity']


def remove_item(item, stock):
    """ удаляет товар из склада"""

    if item in stock:
        del stock[item]


# пример использования
stock_list = {}

update_stock('Apple', 50, stock_list)
update_stock('Banana', 30, stock_list)
update_stock('Coffee', 20, stock_list)

print(get_item_quantity('Apple', stock_list))

remove_item('Banana', stock_list)

print(stock_list)
