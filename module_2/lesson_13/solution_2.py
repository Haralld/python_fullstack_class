import time

def timer(func): 
    def wrapper(*args, **kwargs):    
        start = time.time() # время начала функции
        func(*args, **kwargs) # запуск функции
        end = time.time() # время окончании функции
        print(f"Execution {round(end-start, 2)} seconds")
    return wrapper

@timer
def create_design(task, pause):
    time.sleep(pause)
    print(task)
    

task_1 = "Логотип Васильевский рынок"
task_2 = "Макет сайта Логомашины"

create_design(task_1, 3)
create_design(task_2, 2)

"""
Задание 2: Отслеживание времени выполнения дизайн-проектов

Описание:

В студии Романа узнали о ИИ и уволили всех дизайнеров. 
Однако, функция `create_design`, длится непредсказуемо долго. 
Роман хочет как то замерять время работы этой функции, чтобы планировать сроки проектов более эффективно. 
Функция настолько сложная, что изменять её нельзя.
"""