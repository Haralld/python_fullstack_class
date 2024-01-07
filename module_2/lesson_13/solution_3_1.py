"""Кэширование данных"""

cache_calls = {}    # Словарь для хранения кэшированных результатов

def cache(func):

    def wrapper(*args, **kwargs):
        tuple_args = args + tuple(kwargs.items())
        # Проверяем, есть ли результат в кэше
        if tuple_args in cache_calls:
            # Возвращаем кэшированный результат
            return cache_calls[tuple_args]
        # Если результат не найден в кэше, вызываем оригинальную функцию
        result = func(*args, **kwargs)
        # Сохраняем результат в кэше
        cache_calls[tuple_args] = result
        return result
    
    return wrapper

@cache
def calculate_project_cost(a=1, b=2, c=3):
    # Функция, которая вычисляет результат
    for i in range(100_000_000):
        i += a + b + c
    return i

# Примеры использования
print(calculate_project_cost(10, c=30))
print(calculate_project_cost(10, c=30))
print(calculate_project_cost(10, c=30))

print(calculate_project_cost(5, 15, 20))
print(calculate_project_cost(5, 15, 20))
print(calculate_project_cost(5, 15, 20))

print(calculate_project_cost({5, 15, 20}))
print(calculate_project_cost({5, 15, 20}))