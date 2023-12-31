"""Анализ расположения товаров"""


def create_shelves(data):
    """
    компилирует текстовые данные в список
    """
    items = data.split(';')  # разделяем данные на полки
    item_sales = [list(map(int, item.split(","))) for item in items]    # разделяем каждую стоку на числа и преобразуем в матрицу

    return item_sales


# пример использования
items_1 = "5,3;7,2"
items_2 = "2,6,4;3,5,7;1,2,3"

finished_shelves_1 = create_shelves(items_1)
finished_shelves_2 = create_shelves(items_2)

# вывод данных
print(f"Продажи: {finished_shelves_1}")
print(f"Продажи: {finished_shelves_2}")



"""
Задача 4: Роман анализирует эффективность расположения товаров

Описание:  

Роман подозревает, что расположение товаров на полках влияет на продажи.
 Он хочет создать матрицу, где строка будет представлять полку, столбец - товар на этой полке,
   а значение в ячейке - количество продаж. 
   Напишите программу, которая позволяет ввести продажи по каждому товару и создает соответствующий двумерный массив.



Таблица входных и выходных данных:

|             Входные данные            |         Выходные данные           |

| --------------------------------      | -------------------------------   |

| Введите количество полок: 2           | Продажи: [[5, 3], [7, 2]]|        |

| Продажи по товарам: 5,3;7,2           |                                   |

| Введите количество полок: 3           | Продажи: [[2, 6, 4], [3, 5, 7],   |                                                             

| Продажи по товарам: 2,6,4;            | [1, 2, 3]]                        |

| 3,5,7;1,2,3                           |                                   |
"""
