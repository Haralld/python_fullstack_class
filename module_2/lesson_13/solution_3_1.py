cash = {
    'args': None,
    'result': None
}  # Словарь для хранения кэшированных результатов

def check_args(func):
    def wrapper(*args):
        # Проверяем, есть ли результат в кэше
        if cash['args'] == args:
            # Возвращаем кэшированный результат
            return f"Загрузили из кэша: {cash['result']}"
        else:
            # Если результат не найден в кэше, вызываем оригинальную функцию
            result = func(*args)
            cash['args'] = args
            cash['result'] = result
            return f"Посчитали цену: {result}"

    return wrapper

@check_args
def calculate_project_cost(*args):
    # Функция, которая вычисляет результат
    return 3000

# Примеры использования
print(calculate_project_cost(('Логотип', 'Малый бизнес')))
print(calculate_project_cost(('Логотип', 'Малый бизнес')))
print(calculate_project_cost(('Логотип', 'Большой бизнес')))
print(calculate_project_cost(('Логотип', 'Большой бизнес')))
print(calculate_project_cost({'Логотип', 'Малый бизнес'}))

