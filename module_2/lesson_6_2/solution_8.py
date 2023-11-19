input_produсts = input("Введите товары через запятую:")
products_list = input_produсts.split(',')

product_index_1 = int(input("Первый продукт: "))
product_index_2 = int(input("Второй продукт: "))

products_list[product_index_1 - 1], products_list[product_index_2 - 1] = products_list[product_index_2 - 1], products_list[product_index_1 - 1]

print(f"товары на полке:{products_list}")
"""
Задание 8: Перестановка товаров

Описание:

Роман хочет переставить товары на полке. Напишите программу, которая меняет местами два товара на указанных позициях.


"""