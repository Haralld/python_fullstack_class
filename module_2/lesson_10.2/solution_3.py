employee_dict = {
    "Анна" : 5,
    "Боб" : 7,
    "Сюзан" : 9
}


def responsible_employee(employee_dict):
    names_employee = list(employee_dict.keys())
    values_employee = list(employee_dict.values())

    max_copleted = max(values_employee)
    responsible_employees = [name for name, completed in employee_dict.items() if completed == max_copleted]

    return responsible_employees

responsible_employees = responsible_employee(employee_dict)

print("Самый ответственный сотрудник: ", responsible_employees)

"""
Задание 3: Ответственный сотрудник 🔥

Описание:

Роман хочет знать, какой из его сотрудников в студии дизайна наиболее ответственный в этом месяце.
 Напишите функцию, которая принимает количество задач, 
 выполненных каждым сотрудником, и возвращает имя самого ответственного.



Функция должна быть реализована без использования циклов. Но можно использовать list comprehension.
"""