import json
import csv
from datetime import datetime, date
import re

class Client:
    def __init__(self, name, surname, birthday, bonuses):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    @staticmethod
    def verification_client(name, surname, birthday, bonuses):
        """Проверка клиента по необходимым параметрам."""
        
        # Проверка бонусов
        if not (0 <= bonuses <= 10000000):
            return False

        # Проверка имени и фамилии на наличие только символов кириллицы
        if not (re.match(r'^[А-Яа-яЁё\s]+$', name) and re.match(r'^[А-Яа-яЁё\s]+$', surname)):
            return False
        
        try:
            # Проверка даты рождения
            birth_date = datetime.strptime(birthday, '%d.%m.%Y').date()
            current_date = date.today()
            if birth_date > current_date or birth_date.year < 1950:
               return False
        except ValueError:
            return False

        return True
    
def cvs_to_json(file):
    """Функция для переформатирования данных из csv файла в json."""
    processed_rec = 0   # Обработанные клиенты
    missing_rec = 0     # Пропущенные клиенты

    with open(file, 'r', encoding='utf-8') as csv_file: # Читаем csv файл
        csv_reader = csv.DictReader(csv_file)

        clients = [] 
        for row in csv_reader:
            try:
                name = row['Name'].lower()
                surname = row['Surname'].lower()
                birthday = row['Birthday']
                bonuses = int(row['Bonuses'])

                if Client.verification_client(name, surname, birthday, bonuses):    # Проверка клиента
                    clients.append({
                        'name': name,
                        'surname': surname,
                        'birthday': birthday,
                        'bonuses': bonuses
                    })
                    processed_rec += 1

                else:
                    missing_rec += 1

            except (ValueError, KeyError):
                missing_rec += 1

    with open('clients.json', 'w', encoding='utf-8') as json_file: # Запись прошедших клиентов в json файл
        json.dump({'clients': clients}, json_file, ensure_ascii=False, indent=2)

    # Вывод результатов обработки
    print(f'Было обработано(клиентов): {processed_rec} \nБыло пропущено(клиентов): {missing_rec}')


cvs_to_json('clients.csv')
