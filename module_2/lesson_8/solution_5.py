input_first = input("Введите список товаров первого магазина: ")
first_store = input_first.split(", ")

input_second = input("Введите список товаров второго магазина: ")
second_store = input_second.split(", ")

only_first_store = []
only_second_store = []

for item in first_store:
    if item not in second_store:
        only_first_store.append(item)
    

for item in second_store:
    if item not in first_store:
        only_second_store.append(item)


print(f"Только в первом магазине: {only_first_store}")
print(f"Только во втором магазине: {only_second_store}")


"""
Задача 5: Уникальные товары для двух магазинов

Описание:

Роман хочет определить, какие товары являются уникальными для двух его магазинов. 
Пользователь вводит список товаров для первого и второго магазина через запятую. 
Необходимо вывести два списка: товары, которые продаются только в первом магазине, и товары, которые продаются только во втором.
"""