products_dict = {
    'Яблоко' : 100,
    'Банан' : 80,
    'Кофе' : 250,
    'Чай' : 150
}

product = input("Введите товар: ")

if product in products_dict:
    print("Цена: ", products_dict[product])
else:
    print("Данный товар отсутствует.")
    
"""
Задача 1: Словарь цен

Описание:

Роман имеет магазин и хочет быстро узнать стоимость определенных товаров.
 Данные для словаря: {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}. 
 Пользователь вводит название товара, и программа должна вывести его цену.


"""
