input_price = input("Введите цены: ")
price_list = [int(x) for x in input_price.split(',')]
price_list.sort()

price_list[0], price_list[-1] = price_list[-1], price_list[0]

print(f"Новые цены:{price_list}")

"""
Задание 5: Обмен цен

Описание:

Роман хочет временно поменять цены на самый дорогой и самый дешевый товары. 
Программа должна выводить новый список цен с обмененными значениями.
"""