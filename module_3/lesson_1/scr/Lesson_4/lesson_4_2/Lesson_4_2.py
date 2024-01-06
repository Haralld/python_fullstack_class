from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: str):
        pass


class TextFileHandler(FileHandler):

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'r') as file:
            content = file.read()
            print(f"Содержание текстового файла: {content}")

    def write(self, data: str):
        with open(self.file_name, 'w') as file:
            file.write(data)
            print('Текст был записан в файл')


class BinaryFileHandler(FileHandler):

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'rb') as file:
            content = file.read()
            print(f'Содержание бинарного файла: {content}')

    def write(self, data: bytes):
        with open(self.file_name, 'wb') as file:
            file.write(data.encode('utf-8'))
            print('Бинарные данные были записаны в файл')


def save_data(handler: FileHandler, data: str):
    handler.write(data)
    handler.read()


text_handler = TextFileHandler('text.txt')
binary_handler = BinaryFileHandler('binar.bin')

save_data(text_handler, "Пока вы не сделали что то лучшее чем остальные, не критикуйте их. Леонардо да Винчи")
save_data(binary_handler,
          '10000011111100001111101000011101010000110000100000100001100101000100101110000010000111101100001101011000001000100000110000110100100001101011000011101110000110000100001110111000011100010000010001000111100010000101000011111010000010001000010100001111101000001000011101110001000011100010001111000100100010000110101100001101011000001000100011110000110101100001111001000001000011111010001000001100010000101000011000010000111011100010011001000011110110001001011100001101011011001000001000011110110000110101100000100001110101000100000010000111000100010000101000011100010000111010100010000111000011100110001000010100001101011000001000011100010001000101101110100000100000110111000011010110000111110100001111011000011000010001000000100001101001000011111010000010000110100100001100001000001000001001010000111000100001111011000100011110000111000')


"""
Задание 2: Работа с файлами (Использование протоколов)
Создайте протокол FileHandler с методами read() и write(data: str).
Реализуйте два класса, TextFileHandler и BinaryFileHandler, которые реализуют этот протокол.
TextFileHandler должен читать и писать текстовые файлы, а BinaryFileHandler — бинарные файлы.
В реализации не обязательно действительно использовать файлы, но вы можете добавить такой функционал.
В качестве решения достаточно вывести информацию, что файл был прочитан и записан
Создайте функцию save_data(handler: FileHandler, data: str),
которая сохраняет данные, используя переданный "обработчик файлов".
"""
