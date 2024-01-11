import csv

data_file = 'client.csv'    # фаил с данными о клиентах

# отчистка файла перед началом работы
with open(data_file, 'w', newline='') as csv_file:
    csv_file.write('')

print("Добрый день! Вводите данные: ")

# вводим данные о клиенте
while True:
    name = input('Имя: ')
    if name == 'stop':
        break

    surname = input('Фамилия: ')
    birthday = input('Дата рождения: ')
    bonuses = input('Баланс бонусов: ')

    new_client = {
        'Name': name,
        'Surname': surname,
        'Birthday': birthday,
        'Bonuses': bonuses
    }

    # записываем данные о клиенте в файл
    with open(data_file, 'a', newline='') as csv_file:
        fild_names = ['Name', 'Surname', 'Birthday', 'Bonuses']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fild_names)

        if csv_file.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerow(new_client)

    print(f"Спасибо! Клиент {name} {surname} добавлен!")