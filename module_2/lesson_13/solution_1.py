def price_change(func):
    def wrapper(item, old_price, new_price):
        result = func(item, old_price, new_price)
        print(f"Цена на {item} изменилась! {old_price} > {new_price}")
        return result

    return wrapper


@price_change
def change_price(item, old_price, new_price):
     return new_price

new_price_1 = change_price("Кресло", 5000, 4500)
new_price_2 = change_price("Стол", 6000, 5500)
"""
Задание 1: Логирование изменений стоимости товаров

Описание:  

Роман заметил, что один из сотрудников покупает товаров в магазине на сумму превышающую его зарплату и даже зарплату Романа. 
Роман решил добавить логирование изменения стоимости товаров.
 В кассовой программе уже есть функция `change_price`, он хочет, 
 чтобы после изменения цены выводилось сообщение с информацией о товаре и его новой цене, не изменяя исходный код функции.


"""
