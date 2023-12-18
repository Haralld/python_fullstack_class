def validate_input(func):
    def wrapper(project_name, num_tasks, *agrs, **kwargs):
        if len(args) != 0 or len(kwargs) != 0:  # Проверка количества аргументов
            raise ValueError("Функция должна состоять из двух аргументов")
        
        if not isinstance(project_name, str):# Проверка типа первого аргумента
            raise TypeError("Название проекта должно быть строкой")
        
        if not isinstance(num_tasks, int):# Проверка типа второго аргумента
            raise TypeError("Количество задач должно быть целым числом")

        return func(project_name, num_tasks)

    return wrapper

@validate_input
def estimate_time(project_name, num_tasks):
    result = "Estimated time calculated successfully"
    return result

try:
    project_1 = estimate_time("Веб-сайт", "пять", 3)
    print(project_1)
except ValueError as ve:
    print(f"Ошибка: {ve}")
except TypeError as te:
    print(f"Ошибка: {te}")

try:
    project_2 = estimate_time("Визитка", 10)
    print(project_2)
except ValueError as ve:
    print(f"Ошибка: {ve}")
except TypeError as te:
    print(f"Ошибка: {te}")


"""
Задание 4: Валидация входных данных для расчёта сроков

Описание:

Функция `estimate_time` используется для расчёта времени выполнения проекта.
 Роман хочет быть уверенным, что в функцию подаются данные правильного типа (название проекта - строка, количество задач - целое число),
   и в противном случае получать соответствующее предупреждение.
 Сначала проверяется количество аргументов, потом тип первого и затем тип второго аргумента.
"""
