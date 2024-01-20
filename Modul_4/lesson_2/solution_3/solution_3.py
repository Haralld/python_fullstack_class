import json
import csv
from datetime import datetime
import re

class Client:
    def __init__(self, name, surname, birthday, bonuses):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    def verification_client(self):
        """проверка клиента по необходимым параметрам"""

        if not (0 <= self.bonuses <= 10000000): # проверка бонусов
            return False

        if not (re.match(r'^[А-Яа-я\s]+$', self.name) and re.match(r'^[А-Яа-я\s]+$', self.surname)):  # проверка на кирилицу
            return False
        
        try:
            date = datetime.strptime(self.birthday, '%d.%m.%Y').year
            if not (1950 <= date):
               return False
        except ValueError:
            return False

        return True
    
def cvs_to_json(file):
    processed_rec = 0   # обрабонанные клиенты
    missing_rec = 0 # пропущенные клиенты

    with open(file, 'r', encoding='utf-8') as csv_file: # читаем csv фаил
        csv_reader = csv.DictReader(csv_file)

        clients = []        
        for row in csv_reader:
            try:
                name = row['name'].lower()
                surname = row['surname'].lower()
                birthday = row['birthday']
                bonuses = int(row['bonuses'])

                client = Client(name, surname, birthday, bonuses)

                if client.verification_client():    # проверка клиента
                    clients.append({
                        'name': client.name,
                        'surname': client.surname,
                        'birthday': client.birthday,
                        'bonuses': client.bonuses
                    })
                    processed_rec += 1

                else:
                    missing_rec += 1

            except (ValueError, KeyError):
                missing_rec += 1

    with open('clients.json', 'w', encoding='utf-8') as json_file: # запись прошедших клиентов в json фаил
        json.dump({'clients': clients}, json_file, ensure_ascii=False, indent=2)

    print(f'Было обработано(клиентов): {processed_rec} \nБыло пропущено(клиентов): {missing_rec}') # вывод результатов записи


cvs_to_json('clients.csv')

