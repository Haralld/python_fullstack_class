"""Кэширование данных"""


cache = {}  # Глобальная переменная для кеша

def compiler_type(param_1, param_2):
    # Проверяем, являются ли параметры списками или множествами
    if isinstance(param_1, (list, set)):
        param_1 = tuple(sorted(param_1))
    if isinstance(param_2, (list, set)):
        param_2 = tuple(sorted(param_2))

    # Проверяем, есть ли результат для данных параметров в кеше
    key = (param_1, param_2) if isinstance(param_1, tuple) or isinstance(param_2, tuple) else (param_1, param_2)
    if key in cache:
        # Если есть, возвращаем результат из кеша и указываем, что результат взят из кеша
        return cache[key], True
    else:
        # Если нет, возвращаем None и указываем, что результат не взят из кеша
        return None, False

def cache_result(param_1, param_2, result):
    # Проверяем, являются ли параметры списками или множествами
    if isinstance(param_1, (list, set)):
        param_1 = tuple(sorted(param_1))
    if isinstance(param_2, (list, set)):
        param_2 = tuple(sorted(param_2))

    # Сохраняем результат в кеше
    key = (param_1, param_2) if isinstance(param_1, tuple) or isinstance(param_2, tuple) else (param_1, param_2)
    cache[key] = result

def calculate_project_cost(param_1, param_2):
    # Первая функция с вычислениями
    result_cached, from_cache = compiler_type(param_1, param_2)
    if result_cached is not None and from_cache:
        print(f"Результат взят из кеша: {result_cached}")
        return result_cached
    else:
        # Если результат не в кеше, проводим расчет
        if isinstance(param_1, str) or isinstance(param_2, str):
            result = str(param_1) + str(param_2)
        else:
            result = param_1 + param_2
        # Сохраняем результат в кеше
        cache_result(param_1, param_2, result)
        print(f"Результат посчитан снова: {result}")
        return result

# Пример использования с разными типами данных

# Пример 1: Строки
str_1 = "Hello"
str_2 = "World"
str_result = calculate_project_cost(str_1, str_2)

str_new_1 = "Good"
str_new_2 = "Morning"
str_new_result = calculate_project_cost(str_new_1, str_new_2)

str_cached_1 = "Hello"
str_cached_2 = "World"
str_cached_result = calculate_project_cost(str_cached_1, str_cached_2)

# Пример 2: Числа
num_1 = 15
num_2 = 300
num_result = calculate_project_cost(num_1, num_2)

num_new_1 = 5
num_new_2 = 10
num_new_result = calculate_project_cost(num_new_1, num_new_2)

num_cached_1 = 15
num_cached_2 = 300
num_cached_result = calculate_project_cost(num_cached_1, num_cached_2)

# Пример 3: Списки
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_result = calculate_project_cost(list_1, list_2)

list_new_1 = [7, 8, 9]
list_new_2 = [10, 11, 12]
lest_result_new = calculate_project_cost(list_new_1, list_new_2)

list_cached_1 = [1, 2, 3]
list_cached_2 = [4, 5, 6]
list_cached_result = calculate_project_cost(list_cached_1, list_cached_2)

# Пример 4: Множества
set_1 = {1, 2, 3}
set_2 = {4, 5, 6}
set_result = calculate_project_cost(set_1, set_2)

set_new_1 = {7, 8, 9}
set_new_2 = {10, 11, 12}
set_new_result = calculate_project_cost(set_new_1, set_new_2)

set_cached_1 = {1, 2, 3}
set_cached_2 = {4, 5, 6}
set_cached_result = calculate_project_cost(set_cached_1, set_cached_2)


"""
Задание 3: Кеширование результатов расчёта стоимости проектов

Описание:  

Роман использует функцию `calculate_project_cost` для оценки стоимости проектов. 
Однако расчёт требует значительных ресурсов.
 Роман ещ не знает про возможности кеширования. 
Помогите Роману кэшировать результаты, чтобы повторные вызовы с теми же параметрами не требовали дополнительных вычислений.
"""
