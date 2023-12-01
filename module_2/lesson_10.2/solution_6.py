input_prices = input("Список цен: ")
price_list = [float(x) for x in input_prices.split(', ')]

def find_max_price(price_list):
    if len(price_list) != 0:
        price_list.sort()
        max_price = price_list[-1]
    return max_price

result = find_max_price(price_list)

print(result)


"""
Задача 6: Поиск максимального элемента

Описание:

Роман хочет найти самый дорогой товар в одном из своих магазинов. 
У него есть список цен товаров, но к сожалению, 
его программы не могут использовать встроенные функции Python для поиска максимального элемента.
 Напишите рекурсивную функцию `find_max_price`, которая принимает на вход список цен и возвращает максимальную цену.


"""