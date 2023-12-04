products_dict = {
    'apples': 50,
    'bananas': 10,
    'cherries': 3
    } 
min_reserve = 15

def track_low_stock_with_for(products_dict, min_reserve):
    print('Низкий запас: ')

    for product in products_dict:
        if products_dict.get(product) < min_reserve:
            print(f'{product} - {products_dict[product]}')

track_low_stock_with_for(products_dict, min_reserve)

"""
Задача 3: Отслеживание запасов
Роман хочет знать, какие товары скоро закончатся на складе. 
Напишите функцию `track_low_stock_with_for`, которая принимает словарь с товарами и их количеством,
 использует цикл `for` для идентификации товаров с количеством меньше заданного порога и выводит их в формате "Товар - Количество",
   каждого товара в отдельной строке.

   Ограничения:
- Использовать только цикл `for`.
"""