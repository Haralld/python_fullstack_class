input_items_price = input("Введите цены и скидку: ")
price_list = [float(x) for x in input_items_price.split(', ')]

def calculate_discount(prices):
    price_list = prices[:-1]
    sum_price = sum(price_list)
    discount = sum_price * (prices[-1] / 100)
    return discount

total_discount = calculate_discount(price_list)

print(f"Сумма скидки: {total_discount}")

"""
Задача 1: Подсчет скидки

Описание:

Роман хочет узнать, какую сумму он сэкономит покупателям, если предложит скидку на товары в его магазине. 
Напишите функцию `calculate_discount`, которая принимает на вход список цен товаров и процент скидки, 
при вводе скидка будет последним числом.
 Функция должна возвращать сумму скидки на все товары.
"""
