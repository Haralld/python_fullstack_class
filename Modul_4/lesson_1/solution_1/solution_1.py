import os

first_file_name = input("Введите название первого файла: ")
last_file_name = input("Введите название последнего файла: ")

# Извлекаем номера из имен файлов
start_number = int(first_file_name.split('.')[0])
end_number = int(last_file_name.split('.')[0])

# Проверяем и создаём папку files
folder_path = "files"   # Папка с файлами
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Папка {folder_path} успешно создана.")

# Создаем файлы и записываем названия файлов в каждый файл в папке 'files' - для эмитации работы по заданию
for number in range(start_number, end_number + 1):
    current_file_name = f"files/{number}.txt"
    
    with open(current_file_name, 'w', encoding="utf-8") as file:
        file.write(f"Содержимое файла {current_file_name}")
    print(f"Файл {current_file_name} создан успешно.")

# Переносим информацию из файлов об оплате в файл for_buh.txt
def copy_file(source_path, destination_path):
    """Функция переноса данных из одного файла в другой"""
    try:
        with open(source_path, 'r', encoding="utf-8") as source_file:
            content = source_file.read()

        with open(destination_path, 'a', encoding="utf-8") as destination_file:
            destination_file.write(content + '\n')  # Добавляем символ новой строки после каждого файла

        print(f"Данные успешно скопированы из {source_path} в {destination_path}.")
    except IOError:
        print("Ошибка при копировании данных")

buh_file = "for_buh.txt"   # Файл для бухгалтерии

file_list = sorted([file for file in os.listdir(folder_path) if file.endswith('.txt')], key=lambda x: int(x.split('.')[0]))

for file_name in file_list:
    source_file_path = os.path.join(folder_path, file_name)
    copy_file(source_file_path, buh_file)
