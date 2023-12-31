person = 0
supply = {}
design = {}

while person < 6:
    input_person = input("Введите Отдел, Должность, Фамилию нового сотрудника: ")
    person_list = input_person.split(", ")
    person += 1

    if person_list[0] == "Снабжение":
        supply.clear()
        supply.update({person_list[1]: person_list[2]})
    elif person_list[0] == "Дизайн":
        design.clear()
        design.update({person_list[1]: person_list[2]})
    else:
        continue
    
print(f"Снабжение: {supply}")
print(f"Дизайн: {design}")

"""
Задача 4: Управление персоналом

Описание:

Роман нанял слишком много сотрудников и забыл, какие должности заняты, а какие нет в отделах "Снабжение" и "Дизайн". 
Пользователь вводит 6 строк в формате: Отдел, Должность, Фамилия. 
Последний нанятый сотрудник на должность, которая была ранее занята, приводит к увольнению прошлого сотрудника.
 Программа должна вывести два словаря с актуальным составом сотрудников по отделам "Снабжение" и "Дизайн".


"""
