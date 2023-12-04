units_list = ([1, 2], 'meter')

def convert_units_with_while(units_list):
    units = units_list[0]
    units_list_len = 0
    measursystem = units_list[1]

    while units_list_len < len(units):
        print(f"{units[units_list_len]} {measursystem}(s) = {units[units_list_len] * 3.28084} foot(feet)")
        units_list_len += 1


convert_units_with_while(units_list)
   


"""
Задача 9: Перевод единиц измерения

Роман импортирует товары из разных стран и ему необходимо переводить единицы измерения.
 Создайте функцию `convert_units_with_while`, которая преобразует значения из списка из метрической системы 
 в имперскую и выводит результат с указанием обеих единиц измерения. Вывод должен быть отдельными строками.

Ограничения:

- Использовать только цикл `while`.
"""