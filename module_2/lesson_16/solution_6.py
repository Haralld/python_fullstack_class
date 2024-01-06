"""Оптимизация рабочих пространств"""

def matrix_gen(size):
    """
    Генерирует матрицу исходя из заданных параметров

    args:
        size (int): размер матрици

    return:
        matrix (list): матрицу 
    """
    matrix = [["0"] * size for _ in range(size)]
    
    for i in range(size):
        if i != size // 2:  # исключаем центральное место
            matrix[i][size - 1 - i] = 5 # заполняем от правого верхнего до левого нижнего угла
        for j in range(i + 1, size - 1 - i):
            matrix[i][j] = 1    # заполняем верхнюю часть квадрата
            matrix[j][i] = 2    # заполняем левую часть квадрата
            matrix[size - 1 - i][j] = 3 # заполняем нижнюю часть квадрата 
            matrix[j][size - 1 - i] = 4 # заполняем правую часть квадрата 
    
    return matrix

# пример использования
working_area_1 = 3
working_area_2 = 5
working_area_3 = 7

working_matrix_1 = matrix_gen(working_area_1)
working_matrix_2 = matrix_gen(working_area_2)
working_matrix_3 = matrix_gen(working_area_3)

# вывод матриц
print("Схема рабочих мест: ")
for row in working_matrix_1:
    print(" ".join(map(str, row)))

print("Схема рабочих мест: ")
for row in working_matrix_2:
    print(" ".join(map(str, row)))

print("Схема рабочих мест: ")
for row in working_matrix_3:
    print(" ".join(map(str, row)))

"""
Задача 6: Оптимизация рабочих пространств 🔥🔥

Описание:

Роман хочет оптимизировать распределение рабочих пространств в студии. 
Каждое рабочее место имеет различные характеристики (например, близость к окну, наличие дополнительного оборудования и т.д.). 



Используйте двумерный массив, чтобы создать схему расположения рабочих мест с учетом их характеристик. 
Номера в массиве представляют уровень комфорта от 0 до 5. 
По диагонали с левого верхнего края вниз должны быть места с уровнем комфорта 0. 
По диагонали от правого верхнего угола до левого нижнего должны быть места с максимальным комфортом, пропуская центральное место. 
А остальные места имеют возрастающий комфорт против движения часовой стрелки. Рабочее пространство всегда имеет форму квадрата.



Таблица входных и выходных данных:

|               Входные данные                         |        Выходные данные        |

| -----------------------------------                  | ------------------- --------- |

| Введите размер рабочей зоны: 3                       | Схема рабочих мест:           |

|                                                      | 0 1 5                         |

|                                                      | 2 0 4                         |

|                                                      | 5 3 0                         |

| Введите размер рабочей зоны: 5                       | Схема рабочих мест:           | 

|                                                      | 0 1 1 1 5                     |

|                                                      | 2 0 1 5 4                     |

|                                                      | 2 2 0 4 4                     |

|                                                      | 2 5 3 0 4                     |

|                                                      | 5 3 3 3 0                     |


"""
