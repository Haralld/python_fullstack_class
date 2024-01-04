"""Генерация спиральной матрицы"""


def spiral_matrix_gen(side):
    """
    Генерирует спиральную матрицу

    args:
        side (int): длинна сторон спирали
    
    return:
        matrix (list): спиральная матрица
    """
    matrix = [[0] * side for i in range(side)]

    # инициализация переменных
    top = 0
    left = 0
    bottom = side - 1    
    right = side - 1
    step = 1

    while top <= bottom and left <= right:
        # заполнение верхнего ряда
        for i in range(left, right + 1):
            matrix[top][i] = step
            step += 1
        top += 1

        # заполнение правого столбца
        for i in range(top, bottom + 1):
            matrix[i][right] = step
            step += 1
        right -= 1

        # заполнение нижнего ряда
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = step
                step += 1
            bottom -= 1

        # заполнение левого столбца
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = step
                step += 1
            left += 1
        
    return matrix


# пример использования 
side_1 = 3
side_2 = 4

spiral_matrix_1 = spiral_matrix_gen(side_1)
spiral_matrix_2 = spiral_matrix_gen(side_2)

# вывод матрицы
print("Матрица проектов:")
for row in spiral_matrix_1:
    print(" ".join(map(str, row)))

# вывод матрицы
print("Матрица проектов:")
for row in spiral_matrix_2:
    print(" ".join(map(str, row)))

"""
Задача 5: Спиральная матрица дизайна 🔥🔥

Описание:

В дизайн студии Романа каждый новый проект получает уникальный номер. 
Роман хочет отобразить номера текущих проектов в виде квадратной спиральной матрицы по часовой стрелке, начиная с верхнего левого угла. 
Создайте программу, которая генерирует такую матрицу для заданного числа проектов. Вводится ширина матрицы!



Таблица входных и выходных данных:

| Входные данные     |      Выходные данные       |

| ------------------ | -------------------------- |

| 3                  | Матрица проектов:          |

|                    | 1 2 3                      |

|                    | 8 9 4                      |

|                    | 7 6 5                      |

| 4                  | Матрица проектов:          | 

|                    | 1  2  3  4                 |

|                    | 12 13 14 5                 |

|                    | 11 16 15 6                 |

|                    | 10 9  8  7                 |
 

"""