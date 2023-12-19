from functools import lru_cache

def calculate_and_print_cost(func):
    @lru_cache(maxsize=None)
    def wrapper(project_name, business_type):
        cost_result = func(project_name, business_type)
        cache_info = wrapper.cache_info()
        if cache_info.hits:
            print(f"Загрузили из кеша цену: {cost_result}")
        else:
            print(f"Посчитали цену: {cost_result}")
        return cost_result

    return wrapper

@calculate_and_print_cost
def calculate_project_cost(project_name, business_type):
    return 3000

project_1 = ("Логотип", "малый бизнес")
project_2 = ("Логотип", "малый бизнес")

calculate_project_cost(*project_1)
calculate_project_cost(*project_2)  
"""
Задание 3: Кеширование результатов расчёта стоимости проектов

Описание:  

Роман использует функцию `calculate_project_cost` для оценки стоимости проектов. 
Однако расчёт требует значительных ресурсов.
 Роман ещ не знает про возможности кеширования. 
Помогите Роману кэшировать результаты, чтобы повторные вызовы с теми же параметрами не требовали дополнительных вычислений.
"""
