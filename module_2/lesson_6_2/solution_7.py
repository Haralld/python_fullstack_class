input_produсts = input("Введите товары через запятую:")
products_list = input_produсts.split(',')

product_index = int(input("Позиция товара для удаления: "))

products_list.pop(product_index)

print(f"Товары на полке:{products_list}")

"""
Задание 7: Удаление товаров

Описание:

Роман хочет временно убрать один из товаров с полки. Программа должна удалять товар с указанной позиции.


"""