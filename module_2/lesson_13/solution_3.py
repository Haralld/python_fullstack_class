from functools import lru_cache

@lru_cache(maxsize=None)
def calculate_project_cost(project_name, busines_type):
    result = f"Стоимость проэкта {project_name} для {busines_type}: 3000"
    return result

project_1 = ("Логотип", "малый бизнес")
project_2 = ("Логотип", "малый бизнес")
project_3 = ("Логотип", "крупный бизнес")

print(calculate_project_cost(*project_1)) 
print(calculate_project_cost(*project_2)) # результат будет взят из кэша
print(calculate_project_cost(*project_3)) # результат будет пересчитан из за изменения параметров


"""
Задание 3: Кеширование результатов расчёта стоимости проектов

Описание:  

Роман использует функцию `calculate_project_cost` для оценки стоимости проектов. 
Однако расчёт требует значительных ресурсов.
 Роман ещ не знает про возможности кеширования. 
Помогите Роману кэшировать результаты, чтобы повторные вызовы с теми же параметрами не требовали дополнительных вычислений.
"""