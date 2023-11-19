input_produсts = input("Введите товары через запятую:")
products_list = input_produсts.split(',')

new_product_index = int(input("Позиция для нового товара: "))
new_product = input("Введите новый товар: ")

products_list.insert(new_product_index, new_product)

print(f"Товары на полке:{products_list}")

"""
Задание 6: Внесение изменений в список товаров

Описание:

Роман хочет добавить новый товар в список. Напишите программу, которая вставит новый товар на указанную позицию.


"""