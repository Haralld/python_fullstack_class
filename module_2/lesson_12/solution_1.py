data_1 = [1, 2, 3, 4, 5]
data_2 = [10, 15, 5, 20]


def collect_data(data):
    return data 

def process_data(data):
    average = sum(data) / len(data)
    return average

def summarize_data(average):
    return print(f"Итог: Среднее значение: {average}")


data_result = collect_data(data_1)
average_result = process_data(data_result)
summarize_data(average_result)

data_result = collect_data(data_2)
average_result = process_data(data_result)
summarize_data(average_result)


"""
Задача 1: Цепочка функций обработки данных

Описание: 

Роман реализует систему аналитики для магазинов.
 Создайте три функции: `collect_data`, `process_data` и `summarize_data`. 
 Функция `process_data` должна принимать результат работы `collect_data` как аргумент, 
 а `summarize_data` должна принимать результат работы `process_data`.

Примечание:

`collect_data` собирает данные и вызывает функцию`process_data`

`process_data` находит среднее значение и вызывает `summarize_data`

 `summarize_data` создает отчет
"""